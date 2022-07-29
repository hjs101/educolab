<template>
  <div>
    <!-- 교사 navbar -->
    <div v-if="flag==='teacher'">
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

    <!-- 학생 navbar -->
    <div v-else-if="flag==='student'">
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
    </div>

  </div>
  <router-view />
</template>

<script>

export default {
  name: 'theNavbar',
  data() {
    // return {
    //   flag : 'teacher'
    // }
  }
}
</script>