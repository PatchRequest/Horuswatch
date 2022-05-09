<template>


    <div class="md:flex md:justify-center">
        <form @submit.prevent="onSubmit" class="w-1/2">
            <div class="mb-6">
                <label for="dc_ip" class="sr-only block mb-2 text-xl font-medium text-gray-900 dark:text-gray-300">Domain Controller IP</label>
                <input placeholder="Domain Controller IP" v-model="this.dc_ip" type="text" id="dc_ip" class="bg-gray-50 border border-gray-300 text-gray-900 text-xl rounded-lg focus:ring-gray-500 focus:border-gray-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-gray-500 dark:focus:border-gray-500"  required>
            </div>
            <div class="mb-6">
                <label for="username" class="sr-only block mb-2 text-xl font-medium text-gray-900 dark:text-gray-300">Username</label>
                <input placeholder="Username" v-model="this.username" type="text" id="username" class="bg-gray-50 border border-gray-300 text-gray-900 text-xl rounded-lg focus:ring-gray-500 focus:border-gray-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-gray-500 dark:focus:border-gray-500"  required>
            </div>
            <div class="mb-6">
                <label for="password" class="sr-only block mb-2 text-xl font-medium text-gray-900 dark:text-gray-300">Password</label>
                <input placeholder="Password" v-model="this.password" type="password" id="password" class="bg-gray-50 border border-gray-300 text-gray-900 text-xl rounded-lg focus:ring-gray-500 focus:border-gray-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-gray-500 dark:focus:border-gray-500"  required>
            </div>
            <div class="mb-6">
                <label for="domain" class="sr-only block mb-2 text-xl font-medium text-gray-900 dark:text-gray-300">Domain</label>
                <input placeholder="Domain" v-model="this.domain" type="text" id="domain" class="bg-gray-50 border border-gray-300 text-gray-900 text-xl rounded-lg focus:ring-gray-500 focus:border-gray-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-gray-500 dark:focus:border-gray-500"  required>
            </div>




           
            <button type="submit" class="tracking-widest text-white bg-gray-700 hover:bg-gray-800 focus:ring-4 focus:outline-none focus:ring-gray-300 font-medium rounded-lg text-xl w-full sm:w-auto px-5 py-2.5 text-center dark:bg-gray-600 dark:hover:bg-gray-700 dark:focus:ring-gray-800">Submit</button>
        </form>
    </div>


 
</template>

<script>
export default {
    name: 'CreatePage',
    data () {
        return {
            dc_ip: '',
            username : '',
            password : '',
            domain : ''
        }
    },
    methods: {
        onSubmit() {
            this.axios.post(process.env.VUE_APP_BACKEND+"/createassessment",{
                dc_ip: this.dc_ip,
                target: this.domain+"/"+this.username+":"+this.password+"@"+this.dc_ip,
            })
            .then(response => {
                if (response.data.state == "Startet") {
                    this.$emit('clicked', 'statuspage')
                }else {
                    console.log(response.data)
                }
            })
        }
    }
}
</script>