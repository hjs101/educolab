<template>
<<<<<<< HEAD
  <div>
    <!-- 로그인된 경우 nav bar-->
    
    <!-- 로그인 안 된 경우 login 페이지로 push ?? beforeEach 사용-->
    <router-view></router-view>
  </div>
</template>

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

<script>
// import TheNavBar from './components/TheNavBar.vue'
// import {created} from 'vue'
=======
  <div container style="height: 2000px">
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
  <router-view />
  </div>
</template>

<script>
>>>>>>> 5e670de1b5c58d54295585ebb410f86cf4e1f95f
export default {
  name: 'theNavbar',

<<<<<<< HEAD
  components: {
    // TheNavBar,
  }
=======
>>>>>>> 5e670de1b5c58d54295585ebb410f86cf4e1f95f
}
</script>
