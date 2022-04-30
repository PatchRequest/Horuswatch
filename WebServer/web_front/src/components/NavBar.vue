<template>
    <h1>hi! </h1>
</template>

<script>
export default {
    name: 'NavBar',
    data () {
        return {
            msg: 'Welcome to Your Vue.js App'
        }
    },

    methods: {
        onClick () {
            this.msg = 'You clicked the button!'
        }
    }
}
</script>