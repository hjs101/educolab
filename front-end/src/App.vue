<template>
  <div style="height: 2000px">
    <!-- 교사 navbar -->
    <div class="q-pa-md q-gutter-sm">
      <q-bar container style="height: 100px">
        <div class="cursor-pointer"><router-link to="/notice">공지사항</router-link></div>
        <div class="cursor-pointer"><router-link to="/teacher/task">과제</router-link></div>
        <div class="cursor-pointer"><router-link to="/quiz">퀴즈</router-link></div>
        <div class="cursor-pointer"><router-link to="/search">설문조사</router-link></div>
        <div class="cursor-pointer"><router-link to="/teacher">마이페이지</router-link></div>      
      </q-bar>
    </div>

    <!-- 로그인 했을 때 -->
    <the-navbar v-if="isLoggedIn"></the-navbar>

    <!-- 로그인 안했을 때 -->
    <login-view v-else-if="!isLoggedIn"></login-view>
    
  <router-view />
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