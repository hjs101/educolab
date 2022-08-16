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

    <div class="row">
      <main-notice class="col-md-6 col-xs-12 q-py-lg flex justify-center" :mainNotice="mainNotice"></main-notice>
      <main-homework class="col-md-6 col-xs-12 q-py-lg flex justify-center" :mainHomework="mainHomework"></main-homework>
      <main-acc-rank class="col-md-6 col-xs-12 q-py-lg flex justify-center"  :mainAccRank="mainAccRank"></main-acc-rank>
      <main-week-rank class="col-md-6 col-xs-12 q-py-lg flex justify-center" :mainWeekRank="mainWeekRank"></main-week-rank>
    </div>

    <div class="row justify-evenly">
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
    ...mapGetters(['mainNotice', 'mainHomework', 'mainWeekRank', 'mainAccRank', 'isLoggedIn'])
  },
  methods: {
    ...mapActions(['getMainPage'])
  },
  mounted() {
    if (this.isLoggedIn) {
      this.getMainPage()
    }
  }
}
</script>