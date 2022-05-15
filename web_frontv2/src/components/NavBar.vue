<template>
    <div class="navbar bg-base-100">
  <div class="flex-1">
    <a class="btn btn-ghost normal-case text-xl" @click="this.$emit('clicked', 'statuspage')">Horuswatch</a>
  </div>
  <div class="flex-none">
    <ul class="menu menu-horizontal p-0">
      <li><a @click="this.$emit('clicked', 'statisticpage')">Statistics</a></li>
      <li><a @click="this.$emit('clicked', 'createpage')">Create Job</a></li>
      <li><a @click="this.$emit('clicked', 'statuspage')">Latest Status</a></li>
      <li><a @click="this.$emit('clicked', 'addpage')">Custom Words</a></li>
      
      
    </ul>
  </div>
</div>
</template>

<script>
export default {
    name: 'NavBar'
  

    
}
</script>