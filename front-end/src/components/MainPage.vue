<template>
  <div class="baseStyle">
    <div class="q-pa-md row justify-center q-gutter-md">
      <q-card class="my-card bg-secondary text-white">
        <q-card-section>
          <div class="text-h6">name님 환영합니다</div>
          <div class="text-subtitle2">학교 정보</div>
        </q-card-section>
  
        <q-card-section>
          <p>이미지, 칭호, 업적 들어갈 자리</p>
        </q-card-section>
  
        <q-separator dark />
  
        <q-card-actions>
          <q-btn flat>로그아웃</q-btn>
          <q-btn flat>프로필 수정</q-btn>
        </q-card-actions>
      </q-card>
    </div>

    <div class="row justify-evenly q-py-xl">
      <main-notice :mainNotice="mainNotice"></main-notice>
      <main-homework :mainHomework="mainHomework"></main-homework>
    </div>

    <div class="row justify-evenly q-py-xl">
      <main-acc-rank :mainAccRank="mainAccRank"></main-acc-rank>
      <main-week-rank :mainWeekRank="mainWeekRank"></main-week-rank>
    </div>
  </div>  
</template>

<script>
import MainNotice from '@/components/MainNotice.vue'
import MainHomework from '@/components/MainHomework.vue'
import MainWeekRank from '@/components/MainWeekRank.vue'
import MainAccRank from '@/components/MainAccRank.vue'
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'MainPage',
  components: { MainNotice, MainHomework, MainWeekRank, MainAccRank},
  computed: {
    ...mapGetters(['mainNotice', 'mainHomework', 'mainWeekRank', 'mainAccRank'])
  },
  methods: {
    ...mapActions(['getMainPage'])
  },
  created() {
    this.getMainPage()
  }
}
</script>

<style scoped>
  /* footer {
    width: 100%;
    height: 100px; footer의 높이 */
    /* position: absolute;  
    bottom: 0;
  } */
</style>