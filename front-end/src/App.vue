<template>
  <div style="height: 2000px">
    <!-- 로그인 했을 때 -->
    <!-- <the-navbar v-if="isLoggedIn"></the-navbar> -->
    
  <router-view />
  </div>
</template>

<script>
// import TheNavbar from '@/views/TheNavbar.vue'

export default {
  name: 'MainPage',
  // data() {
  //   return {
  //     isLoggedIn : false,
  //   }
  // },
  // components: {
  //   TheNavbar
  // },
}
</script>

<style>
/* 모든 페이지에서 공통으로 사용할 스타일 정의 */
  h3 {
    text-align: center;
  }
  .button {
    text-decoration: none;
  }
  .buttonGroup {
  display: flex;
  justify-content: center;
  text-align: center;
  gap: 10px;
  }
  .center {
    text-align: center;
  }
</style>