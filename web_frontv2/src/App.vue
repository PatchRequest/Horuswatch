<template >

  <div class="dark">
  
    <NavBar @clicked="onClickChild" />
    <StatusPage v-if="currentPage=='statuspage'"  />
    <CreatePage @clicked="onClickChild"  v-if="currentPage=='createpage'" />
    <HomePage v-if="currentPage=='homepage'" />
    <StatisticPage v-if="currentPage=='statisticpage'" />
    <AddPage  v-if="currentPage=='addpage'" />
    <FooterBar class="absolute inset-x-0 bottom-0"/>
  </div>
</template>

<script>

import NavBar from './components/NavBar.vue'
import StatusPage from './components/StatusPage.vue'
import CreatePage from './components/CreatePage.vue'
import HomePage from './components/HomePage.vue'
import FooterBar from './components/FooterBar.vue'
import StatisticPage from './components/StatisticPage.vue'
import AddPage from './components/AddPage.vue'

export default {
  name: 'App',
  components: {
    NavBar,
    StatusPage,
    CreatePage,
    HomePage,
    FooterBar,
    StatisticPage,
    AddPage


  },
  data() {
    return {
      currentPage : "createpage",
    }
  },
   methods: {
    onClickChild (value) {
      this.currentPage = value
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
