<template>
    <div >
        <div>
            <ul class="steps">
                <li class="step" v-bind:class="{ 'step-primary': currenPhase > 0 }">Receive Hashes</li>
                <li class="step" v-bind:class="{ 'step-primary': currenPhase > 1 }">Test Hashes</li>
                <li class="step" v-bind:class="{ 'step-primary': currenPhase > 2 }">Analyze Findings</li>
                <li class="step" v-bind:class="{ 'step-primary': currenPhase > 3 }">Display Results</li>
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
                <div class="stat-value">{{percentage  }}%</div>
            </div>
        
        </div>
        
        <div>
            <progress class="progress progress-secondary w-56" value="30" max="100"></progress>
        </div>
        <div class="overflow-x-auto">
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
                    <th>{{user.username}}</th>
                    <td>{{user.password}}</td>
                </tr>
                <!-- row 2 -->
                
                </tbody>
            </table>
        </div>
    </div>



 
</template>

<script>



export default {
    name: 'StatusPage',
    props : ['phase'],
    data () {
        return {
            total : 0,
            progress : 0,
            status : 0,
            temp : 0,
            speed : 0,
            intervalID : 0,
            percentage : 0,
            currenPhase : 0, 
            pwnduser : []
        }
    },
    watch: { 
        phase: function(newVal, oldVal) { // watch it
            this.currenPhase = newVal
            // do something with newVal, oldVal
            if (newVal == 2) {
                this.intervalID =  setInterval(this.checkForUpdate, 2000)
            }
            console.log('Prop changed: ', newVal, ' | was: ', oldVal)
        }
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
        }

    }

    

}
</script>