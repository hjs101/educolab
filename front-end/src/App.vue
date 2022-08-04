<template>
  <div style="height: 2000px">
    <!-- 교사 navbar -->
    <div v-if="isLoggedIn && currentUser.userflag">
      <div class="q-pa-md q-gutter-sm">
        <q-bar style="height:100px;" >
          <a href="/"><img src="@/assets/educolab.png" alt="educolab" style="width:100px; height:100px;"></a>
          <div class="cursor-pointer"><router-link to="/notice">공지사항</router-link></div>
          <div class="cursor-pointer"><router-link to="/teacher/task">과제</router-link></div>
          <div class="cursor-pointer"><router-link to="/quiz">퀴즈</router-link></div>
          <div class="cursor-pointer"><router-link to="/search">설문조사</router-link></div>
          <div class="cursor-pointer"><router-link to="/teacher">마이페이지</router-link></div>
          <button @click="logoutBtn">로그아웃</button>
        </q-bar>
        <hr>
      </div>
    </div>

    <!-- 학생 navbar -->
    <div v-if="isLoggedIn && !currentUser.userflag">
      <div class="q-pa-md q-gutter-sm">
        <q-bar style="height:100px;" >
          <a href="/"><img src="@/assets/educolab.png" alt="educolab" style="width:100px; height:100px;"></a>
          <div class="cursor-pointer"><router-link to="/notice">공지사항</router-link></div>
          <div class="cursor-pointer"><router-link to="/student/task">과제</router-link></div>
          <div class="cursor-pointer"><router-link to="/student/writing">내 필기</router-link></div>
          <div class="cursor-pointer"><router-link to="/student/store">포인트 상점</router-link></div>
          <div class="cursor-pointer"><router-link to="/student">마이페이지</router-link></div>
          <button @click="logoutBtn">로그아웃</button>
        </q-bar>
        <hr>
      </div>
    </div>

  <router-view />
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'MainPage',
  computed: {
    ...mapGetters(['isLoggedIn', 'currentUser'])
  },
  methods: {
    ...mapActions(['logout']),
    logoutBtn() {
      if (this.isLoggedIn) {
        this.logout()
      } else {
        this.$router.back()
      }
    },
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
  margin: 100px 0px;
  }
  .center {
    text-align: center;
  }
</style>