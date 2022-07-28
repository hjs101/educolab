<template>
  <div style="height:2000px;">

    <!-- 로그인 했을 때 -->
    <the-navbar v-if="isLoggedIn"></the-navbar>

    <!-- 로그인 안했을 때 -->
    <login-view v-else-if="!isLoggedIn"></login-view>
    
  </div>

</template>

<script>
import TheNavbar from '@/views/TheNavbar.vue'
import LoginView from '@/views/LoginView.vue'

export default {
  name: 'MainPage',
  data() {
    return {
      isLoggedIn : true,
    }
  },
  components: {
    TheNavbar, LoginView
  }
}
</script>
