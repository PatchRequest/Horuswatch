<template>
    <div class="md:flex md:justify-center text-3xl pb-10 pt-10">
            Latest Status
    </div>
    <div class="text-xl">
        <div class="pb-10">
            <ul class="steps w-full">
                <li class="step" v-bind:class="{ 'step-primary': status > 0 }">Receive Hashes</li>
                <li class="step" v-bind:class="{ 'step-primary': status > 2 }">Test Hashes</li>
                <li class="step" v-bind:class="{ 'step-primary': status > 3 }">Analyze Findings</li>
                <li class="step" v-bind:class="{ 'step-primary': status > 3 }">Display Results</li>
            </ul>
        </div>
        
        
        <div class="stats shadow">
  
            <div class="stat">
                <div class="stat-title">Total Possible Hashes</div>
                <div class="stat-value">{{ humanReadableNumber(total) }}</div>
            </div>
        
        </div>
        <div class="stats shadow">
  
            <div class="stat">
                <div class="stat-title">Date</div>
                <div class="stat-value">{{ date }}</div>
            </div>
        
        </div>
        <div class="stats shadow">
  
            <div class="stat">
                <div class="stat-title">Hashes Tested</div>
                <div class="stat-value">{{ humanReadableNumber(progress) }}</div>
            </div>
        
        </div>
        <div class="stats shadow">
  
            <div class="stat">
                <div class="stat-title">Hashes per Second</div>
                <div class="stat-value">{{ humanReadableNumber(speed)  }}</div>
            </div>
        
        </div>
        <div class="stats shadow">
  
            <div class="stat">
                <div class="stat-title">Percentage</div>
                <div class="stat-value">{{ percentage }}%</div>
            </div>
        
        </div>
        <div class="flex justify-center w-full pt-10">
        
            <div class="w-3/4">
                <progress class="progress progress-secondary h-16" :value="progress" :max="total"></progress>
            </div>
        </div>
        <div class="flex justify-center w-full pt-10 text-xl"  v-if="status > 3">
            <button class="btn btn-primary" @click="downloadData(this.id)"> Download Results</button>
        </div>

        <div class="flex justify-center w-full pt-3" >
        
            <div class="overflow-x-auto  w-3/4" v-if="status > 3">
                <table class="table w-full">
                    <!-- head -->
                    <thead>
                    <tr>
                        <th>Username</th>
                        <th>Password</th>
                    </tr>
                    </thead>
                    <tbody>
                    <!-- row 1 -->
                    <tr v-for="(user,i) in pwnduser" :key="i">
                        <th>{{user[1]}}</th>
                        <td>{{user[3]}}</td>
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
    name: 'StatusPage',
    data () {
        return {
            id: 0,
            date : "loading...",
            total : "loading...",
            progress : "loading...",
            status : 3,
            speed : "loading...",
            currenPhase : 2, 
            pwnduser : []
        }
    },
    computed: {
        percentage () {
            return Math.floor(this.progress / this.total * 100)
        }
    },
    mounted(){
        this.axios.post(process.env.VUE_APP_BACKEND+"/result")
        .then(response => {
            
            this.total = response.data.assessment[3]
            this.progress = response.data.assessment[2]
            this.speed = response.data.assessment[4]
            this.status = response.data.assessment[5]
            this.date = response.data.assessment[1]
            if (this.status > 3) {
                this.pwnduser = response.data.users
                
                
            }
        })
        
        setInterval(() => {
            this.axios.post(process.env.VUE_APP_BACKEND+"/result")
            .then(response => {
                this.id = response.data.assessment[0]
                this.total = response.data.assessment[3]
                this.progress = response.data.assessment[2]
                this.speed = response.data.assessment[4]
                this.status = response.data.assessment[5]
                this.date = response.data.assessment[1]
                if (this.status > 3) {
                    this.pwnduser = response.data.users
                    
                    
                }
            })

        }, 3000);
        
    },
    methods : {
        
        checkForUpdate(){
            fetch(process.env.VUE_APP_CRACKER_REMOTE_URL+"/update")
            .then(response => response.json())
            .then(response => {
                this.total = response.total;
                this.progress = response.progress;
                this.status = response.status;
                this.temp = this.humanReadableNumber(response.temp);
                this.speed = response.speed;
                this.percentage = Math.round(this.progress / this.total * 100)
                if (this.status == 5){
                    clearInterval(this.intervalID);
                    this.currenPhase = 3;
                    this.sleep(3000);

                    fetch(process.env.VUE_APP_CRACKER_REMOTE_URL+"/result")
                    .then(response => response.json())
                    .then(response => {
                        console.log(response)
                        this.pwnduser = response.user;
                        this.currenPhase = 4;
                    })

                }
            console.log(response.status)
            });
        },
        humanReadableNumber (value, lang = null)  {
            if (!value) return;
            const locale = lang || document.documentElement.lang || 'en'
            const number = parseFloat(value, 10)
            return number.toLocaleString(locale);
        },
        sleep(ms) {
            var start = new Date().getTime(), expire = start + ms;
            while (new Date().getTime() < expire) { 1 == 1}
            return;
        },
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