<template>
    <div class="text-xl">
        <div class="flex justify-center w-full pt-10" >
            <div class="overflow-x-auto  w-3/4" >
                <table class="table w-full">
                    <!-- head -->
                    <thead>
                    <tr>
                        <th>#</th>
                        <th>Date</th>
                        <th>Bad Password Count</th>
                        <th>Status</th>
                    </tr>
                    </thead>
                    <tbody>
                    <!-- row 1 -->
                    <tr v-for="(assessment,i) in assessments" :key="i">
                        <th>{{assessment[0]}}</th>
                        <td>{{assessment[1]}}</td>
                        <td>{{assessment[6]}}</td>
                        <td>{{assessment[5] == "3" ? "Running" : "Finished"}}</td>
                    </tr>
                    <!-- row 2 -->
                    
                    </tbody>
                </table>
            </div>
        </div>
    </div>



 
</template>

<script>

export default {
    name: 'StatisticPage',
    data () {
        return {

            assessments : []
        }
    },
    mounted(){
        
        this.axios.post(process.env.VUE_APP_BACKEND+"/assessments")
        .then(response => {
            this.assessments = response.data.assessments
            
        })
        setInterval(() => {
            this.axios.post(process.env.VUE_APP_BACKEND+"/assessments")
            .then(response => {
                this.assessments = response.data.assessments
                
            })

        }, 3000);
        
    }

    

}
</script>