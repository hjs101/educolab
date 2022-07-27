<template>
  <div>
  <div v-if='isLoggedIn'><router-link to='/'></router-link></div>
  <div v-else><router-link to='/quiz'></router-link></div>  

    <router-view />
  </div>
</template>

<script>

export default {
  name: 'theNavbar',
  data() {
    let isLoggedIn = true
    if (isLoggedIn == false) {
      isLoggedIn = false
    }
    return {
      isLoggedIn
    }
  }
}
</script>
