<template>
  <div style="height: 2000px">
    <!-- 교사 navbar -->
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
  
  <notice-view></notice-view>
  <router-view />
  </div>
</template>

<script>
import NoticeView from '@/views/NoticeView.vue'  

export default {
  name: 'theNavbar',
  props : {
    NoticeView,
  }
}
</script>