<template>
    <div class="navbar bg-base-100">
  <div class="flex-1">
    <a class="btn btn-ghost normal-case text-xl" @click="this.$emit('clicked', 'home')">AD Spy</a>
  </div>
  <div class="flex-none">
    <ul class="menu menu-horizontal p-0">
      <li><a @click="this.$emit('clicked', 'create')">Create Job</a></li>
      <li><a @click="this.$emit('clicked', 'status')">Current Status</a></li>
    </ul>
  </div>
</div>
</template>

<script>
export default {
    name: 'NavBar'
  

    
}
</script>