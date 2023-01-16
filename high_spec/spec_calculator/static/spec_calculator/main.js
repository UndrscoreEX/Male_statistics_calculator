const app = Vue.createApp({
    data(){
        return {
            head :  'Bachelor Calculator',
            min_age_val : 0, 
            max_age_val : 70, 
            inc_val : 0,
            ht_if: false,
            ht_val: 0,
            obese: false,
            mar : false,
            final_error : false,
            smoke : false,
            age_error : null,
            o_button: null,
            m_button: null,
            s_button: null,
            results_max_age:null
            

        }
    },
    methods:{
        check(){
            this.text = 'dfsdausdhf;ds' 

        },
        age_error_check(){
            if (this.min_age_val>= this.max_age_val) {
                this.age_error = true
                console.log(this.age_error)
            }
            else{
                this.age_error = false
                console.log(this.age_error)
            }
        },
        checkForm(e) {
            console.log(e)
            if (this.age_error){
                this.final_error = true;

                // needed to stop error form from being sent
                e.preventDefault();

            }
        }
    },
    computed: {
        
    },
    // super important. Outside of data and methods and computed, you can access the lifehooks like this. 
    mounted(){
        if(document.getElementById('ob_b').textContent == 'on') {
            this.o_button = '<p class="result-text unchecked"> Obese men: excluded</p>'
        }
        else{
            this.o_button = '<p class="result-text "> Obese men : included</p>'
        };

        if(document.getElementById('mar_b').textContent == 'on') {
            this.m_button = '<p class="result-text unchecked"> Married : excluded</p>'
        }
        else{
            this.m_button = '<p class="result-text "> Married men: included</p>'

        };

        // some reason the button's 'on' has some extra space but the others do not
        if(document.getElementById('sm_b').textContent.trim() == 'on') {
            this.s_button = '<p class="result-text unchecked"> Smoking men: excluded</p>'
        }
        else{
            this.s_button = '<p class="result-text "> Smoking men: included</p>'
        };

    }
})

app.config.compilerOptions.delimiters = ['$[', ']'];


const mountedApp = app.mount('#app')