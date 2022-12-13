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

        height_per = Height_groups.objects.filter(height_cm__gte= results['height']).aggregate(Sum('ht_per'))

        pop_range = Age_ref.objects.filter(age__gte=results['min_age'],age__lte=results['max_age'])
        total_pop = 0
        not_married_num = 0
        income_num = 0
        n_obese_total = 0
        n_smoke_num = 0

        for x in pop_range:
            this_age_group_pop = x.age_group_pop
            this_age_g_inc_per_ = 0
            print('this age groups age is: ',this_age_group_pop)
            if results['n_obese']:
                n_obese_total += ((x.not_obese_rate/100) * x.age_group_pop)
            if results['n_married']:
                not_married_num += x.n_yet_married
            if results['n_smoker']:
                n_smoke_num += ((x.not_smoke_rate/100) *x.age_group_pop)
            inc_yr_groups = x.income_groups.filter(income_yr__gte=results['income'])
            for inc in inc_yr_groups:
                print(inc, inc.income_ratio)
                this_age_g_inc_per_ += inc.income_ratio/100

            total_pop += this_age_group_pop
            income_num += (this_age_g_inc_per_*this_age_group_pop)
            print(f'there are {this_age_g_inc_per_} out of {this_age_group_pop}')

        n_marr_final_per = not_married_num/total_pop
        obese_final_per = n_obese_total/total_pop
        n_smoke_final_per = n_smoke_num/total_pop
        abv_inc_range_per = income_num/total_pop
        print('total pop============== ',total_pop)
        final_amount_of_people = total_pop

        print('non-marr per',n_marr_final_per)
        print('non-obs per',obese_final_per)
        print('non-smoke per',n_smoke_final_per)
        print('non-smoke per',n_smoke_final_per)
        print('enough income per',abv_inc_range_per)
        if n_marr_final_per: 
            final_amount_of_people *= n_marr_final_per
        if obese_final_per:
            final_amount_of_people *= obese_final_per
        if n_smoke_final_per:
            final_amount_of_people *= n_smoke_final_per
        if abv_inc_range_per:
            final_amount_of_people *= abv_inc_range_per
        



        print('all percent on total pop',final_amount_of_people, 'out of :', total_pop )

        

        # print(results)
        
        return render(request, 'results.html', {'results':results} )


