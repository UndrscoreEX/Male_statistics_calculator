from django.shortcuts import render
from django.views import View
from .models import Height_groups, Income_groups, Age_ref
from django.db.models import Sum

# Create your views here.


# keep adding the filtering perc and then find the amount for that age group, smoking 


# notes of my plan:
# 5-year groups from 20-80 (this means we will have a lower pop than JP total)
# 


class Calculate_spec(View):

    def get(self, request):
        
        return render(request, 'index.html')

    def post(self, request):
        results = {
            'min_age': request.POST['mn_age_value'],
            'max_age':str(int(request.POST['mx_age_value']) -1),
            'income' :request.POST['income_value'],
            'n_obese':request.POST.get('n_obese_value', False),
            'height':request.POST.get('height_value'),
            'n_married': request.POST.get('n_married_value',False),
            'n_smoker': request.POST.get('n_smoke',False),
        }
        


        pop_range = Age_ref.objects.filter(age__gte=results['min_age'],age__lte=results['max_age'])
        total_pop = 0
        not_married_num = 0
        income_num = 0
        n_obese_total = 0
        n_smoke_num = 0

        for x in pop_range:

            this_age_group_pop = x.age_group_pop
            print('this age groups age is: ',x.age)


            this_age_g_inc_perc = 0

            if results['n_obese']:
                n_obese_total += ((x.not_obese_rate/100) * x.age_group_pop)
            if results['n_married']:
                not_married_num += x.n_yet_married
            if results['n_smoker']:
                n_smoke_num += ((x.not_smoke_rate/100) *x.age_group_pop)

            inc_yr_groups = x.income_groups.filter(income_yr__gte=results['income'])
            for inc in inc_yr_groups:
                # print(this_age_g_inc_perc,' plus: ',inc.income_ratio)
                this_age_g_inc_perc = round((this_age_g_inc_perc + inc.income_ratio),1) 
                # print('now it is :',this_age_g_inc_perc)

            total_pop += this_age_group_pop
            income_num += this_age_g_inc_perc*this_age_group_pop
            # print(f'there are {round(this_age_g_inc_perc,4)} within inc, out of {this_age_group_pop}')
            # print(f'there are {this_age_g_inc_perc} within inc, out of {this_age_group_pop}')

        n_marr_final_per = not_married_num/total_pop
        obese_final_per = n_obese_total/total_pop
        n_smoke_final_per = n_smoke_num/total_pop
        abv_inc_range_per = income_num/total_pop
        # print('total pop============== ',total_pop)
        final_amount_of_people = total_pop

        # print('non-marr per',n_marr_final_per)
        # print('non-obs per',obese_final_per)
        # print('non-smoke per',n_smoke_final_per)
        # print('enough income per',abv_inc_range_per)

        if n_marr_final_per: 
            final_amount_of_people *= n_marr_final_per
        if obese_final_per:
            final_amount_of_people *= obese_final_per
        if n_smoke_final_per:
            final_amount_of_people *= n_smoke_final_per
        if abv_inc_range_per:
            final_amount_of_people *= abv_inc_range_per
        
        print(type(results['height']))
        if results['height'] != '139':
            height_per = Height_groups.objects.filter(height_cm__gte= results['height']).aggregate(Sum('ht_per'))
            print(height_per['ht_per__sum'])
            final_amount_of_people *= (height_per['ht_per__sum'] /100)
        else:
            height_per = 100
        
        
        ultimate_num = final_amount_of_people/total_pop
        results['final'] = round(ultimate_num,2)
        print('all percent on total pop',final_amount_of_people, 'out of :', total_pop, f'which is : {round(ultimate_num,2)} %',  )

        print(results['max_age'])
        # results['max_age'] = str(int(results['max_age'])+1) 
        print(results['max_age'])
        print(results['income'])
        return render(request, 'results.html', {'results':results} )


