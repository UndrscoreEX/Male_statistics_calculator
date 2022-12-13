const app = Vue.createApp({
    data(){
        return {
            head :  'of all the things i\'ve lost, i miss my mind the most',
            min_age_val : 0, 
            max_age_val : 70, 
            inc_val : 0,
            ht_val: 0,
            obese: false,
            mar : false,
            final_error : false,
            smoke : false,
            age_error : null,

            // ----------------

    
        }
    },
    methods:{

        check(){
            console.log(this.min_age_val)

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
                e.preventDefault();

            }

        },
        
       
    // watch: {
    //     max_age_val(e) {
    //         console.log(e)
            
    //     },
    // }
    //     age_val(){},
    //     // inc_val: function(val){
    //     //     this.inc_val = val
    //     //     // let x = val.toLocaleString();
    //     //     // this.inc_val = x;
    //     //     console.log(val)
    //     }

    }
})

app.config.compilerOptions.delimiters = ['$[', ']'];


const mountedApp = app.mount('#app')