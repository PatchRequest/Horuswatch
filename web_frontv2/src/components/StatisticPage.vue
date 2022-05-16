<template>
    <div class="flex justify-center text-3xl pb-10 pt-10">
            Statistic Overview
    </div>    
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
                        <th>Download</th>
                    </tr>
                    </thead>
                    <tbody>
                    <!-- row 1 -->
                    <tr v-for="(assessment,i) in assessments" :key="i">
                        <th>{{assessment[0]}}</th>
                        <td>{{assessment[1]}}</td>
                        <td>{{assessment[6]}}</td>
                        <td>{{assessment[5] == "3" ? "Running" : "Finished"}}</td>
                        <td v-if="assessment[5] == '5'"><button class="btn btn-primary" @click="downloadData(assessment[0])"> Download Results</button></td>
                    </tr>
                    <!-- row 2 -->
                    
                    </tbody>
                </table>
            </div>
        </div>
    </div>



 
</template>

<script>
import { saveAs } from 'file-saver';
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
        
    },
    methods: {
       
            downloadData (assessment_id) {
                this.axios.post(process.env.VUE_APP_BACKEND+"/getAssessment",{
                    assessment_id: assessment_id
                })
                .then(response => {
                    let users = response.data.users
                    
                    let stringList = ""
                    users.forEach(user => {
                        stringList += user[1] + "\n"
                    })
                    
                    let blob = new Blob([stringList], {type: "text/plain;charset=utf-8"});
                    // add stringList into the file
                    
                    saveAs(blob, "result"+assessment_id+".txt");

                })
            }
        
    } 

}
</script>