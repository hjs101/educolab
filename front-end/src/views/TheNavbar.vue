<template>
  <div>
    <!-- <div>
      <div class="q-pa-md q-gutter-sm">
        <q-bar style="height:100px;" >
          <a href="/"><img src="@/assets/educolab.png" alt="educolab" style="width:100px; height:100px;"></a>
          <div class="cursor-pointer"><router-link to="/notice">공지사항</router-link></div>
          <div class="cursor-pointer"><router-link to="/teacher/task">과제</router-link></div>
          <div class="cursor-pointer"><router-link to="/quiz">퀴즈</router-link></div>
          <div class="cursor-pointer"><router-link to="/search">설문조사</router-link></div>
          <div class="cursor-pointer"><router-link to="/teacher">마이페이지</router-link></div>
        </q-bar>
        <hr>
      </div>
    </div>
    <button @click="logoutBtn">로그아웃</button>
    <div>
      <div class="q-pa-md q-gutter-sm">
        <q-bar style="height:100px;" >
          <a href="/"><img src="@/assets/educolab.png" alt="educolab" style="width:100px; height:100px;"></a>
          <div class="cursor-pointer"><router-link to="/notice">공지사항</router-link></div>
          <div class="cursor-pointer"><router-link to="/student/task">과제</router-link></div>
          <div class="cursor-pointer"><router-link to="/student/writing">내 필기</router-link></div>
          <div class="cursor-pointer"><router-link to="/student/store">포인트 상점</router-link></div>
          <div class="cursor-pointer"><router-link to="/student">마이페이지</router-link></div>
        </q-bar>
        <hr>
      </div>
    </div> -->
  </div>
  <!-- <router-view /> -->
</template>

<script>
// import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'theNavbar',
  // computed: {
  //   ...mapGetters(['isLoggedIn'])
  // },
  // methods: {
  //   ...mapActions(['logout']),
  //   logoutBtn() {
  //     if (this.isLoggedIn) {
  //       this.logout()
  //     } else {
  //       this.$router.back()
  //     }
  //   }
  // }
}
</script>