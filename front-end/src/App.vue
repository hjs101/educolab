<template>
  <!-- 로그인된 경우-->
  <!-- <the-nav-bar/> -->
  <!-- 로그인 안 된 경우 -->
  <login-view/>
</template>

<script>
// import TheNavBar from './components/TheNavBar.vue'
import LoginView from './views/LoginView.vue'
export default {
  name: 'LayoutDefault',

  components: {
    // TheNavBar,
    LoginView
  },
}
</script>
