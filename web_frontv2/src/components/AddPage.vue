<template>

    <div>

        <div class="md:flex md:justify-center">
            <form @submit.prevent="onSubmit" class="w-1/2">
                <div class="mb-6">
                    <label for="dc_ip" class="sr-only block mb-2 text-xl font-medium text-gray-900 dark:text-gray-300">Custom Wordslist entries</label>
                    <textarea placeholder="Custom Wordslist entries" v-model="this.field_input" type="text" id="dc_ip" class="bg-gray-50 border border-gray-300 text-gray-900 text-xl rounded-lg focus:ring-gray-500 focus:border-gray-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-gray-500 dark:focus:border-gray-500"  required />
                </div>
            
                <button type="submit" class="tracking-widest text-white bg-gray-700 hover:bg-gray-800 focus:ring-4 focus:outline-none focus:ring-gray-300 font-medium rounded-lg text-xl w-full sm:w-auto px-5 py-2.5 text-center dark:bg-gray-600 dark:hover:bg-gray-700 dark:focus:ring-gray-800">Submit</button>
            </form>
        </div>
        <div class="text-xl">
            <div class="flex justify-center w-full pt-10" >
                <div class="overflow-x-auto  w-3/4" >
                    <table class="table w-full">

                        <thead>
                        <tr>
                            <th>#</th>
                            <th>Word</th>

                        </tr>
                        </thead>
                        <tbody>

                        <tr v-for="(word,i) in knownWords" :key="i">
                            <th>{{word[0]}}</th>
                            <td>{{word[1]}}</td>
                        </tr>
               
                        
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

    </div>
 
</template>

<script>
export default {
    name: 'AddPage',
    data () {
        return {
            field_input: '',
            knownWords: [],
        }
    },
     mounted(){
        
        this.axios.post(process.env.VUE_APP_BACKEND+"/words")
        .then(response => {
            this.knownWords = response.data.words
            
        })
        setInterval(() => {
            this.axios.post(process.env.VUE_APP_BACKEND+"/words")
            .then(response => {
                this.knownWords = response.data.words
            
            })

        }, 3000);
        
    },
    methods: {
        onSubmit() {
            this.axios.post(process.env.VUE_APP_BACKEND+"/addwords",{
                field_input: this.field_input
            })
            .then(response => {
                console.log(response.data)
                // TODO: feedback
            })
        }
    }
}
</script>