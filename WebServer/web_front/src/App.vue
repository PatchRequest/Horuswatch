<template>
  <NavBar/>
  <StatusPage v-if="true" />

 
</template>

<script>

import NavBar from './components/NavBar.vue'
import StatusPage from './components/StatusPage.vue'


export default {
  name: 'App',
  components: {
    NavBar,
    StatusPage
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
