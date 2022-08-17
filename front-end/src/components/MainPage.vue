<template>
  <div class="mainStyle">
    <div class="mar-bottom">
      <div class="row">
        <main-notice class="col-md-6 col-xs-12 q-py-lg flex justify-center" :mainNotice="mainNotice"></main-notice>
        <main-homework class="col-md-6 col-xs-12 q-py-lg flex justify-center" :mainHomework="mainHomework"></main-homework>
        <main-acc-rank class="col-md-6 col-xs-12 q-py-lg flex justify-center"  :mainAccRank="mainAccRank"></main-acc-rank>
        <main-week-rank class="col-md-6 col-xs-12 q-py-lg flex justify-center" :mainWeekRank="mainWeekRank"></main-week-rank>
      </div>
    </div>
  </div>  
</template>

<script>
import MainNotice from '@/components/MainNotice.vue'
import MainHomework from '@/components/MainHomework.vue'
import MainWeekRank from '@/components/MainWeekRank.vue'
import MainAccRank from '@/components/MainAccRank.vue'
import drf from '@/api/drf.js'
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'MainPage',
  components: { MainNotice, MainHomework, MainWeekRank, MainAccRank},
  // setup() {
  //   let ProImg = drf.file.path() + this.currentUser?.profil
  //   return {
  //     ProImg
  //   }
  // },
  computed: {
    ...mapGetters(['mainNotice', 'mainHomework', 'mainWeekRank', 'mainAccRank', 'isLoggedIn', 'currentUser']),
    ProImg() {
      return drf.file.path() + this.currentUser.profil
    }
  },
  methods: {
    ...mapActions(['getMainPage'])
  },
<<<<<<< HEAD
  mounted() {
    if (this.isLoggedIn) {
      this.getMainPage()
    } else {
      this.$router.push({ name: 'login'})
=======
  created() {
    if (!this.isLoggedIn) {
      this.$router.push('/educolab/login')
    } else {
      this.getMainPage()
<<<<<<< HEAD
>>>>>>> c8c893f (Feat: 로그인 여부 & 사용자 여부에 따른 접근 제한)
=======
>>>>>>> 21e52d3 (Fix : 오류  수정2)
    }
  }
}
</script>

<style scoped>
 .text-size {
  font-size: 1rem;
 }
 .profil-size {
  font-size: 0.5rem;
 }
 .mar-bottom {
  margin-top: 100px;
 }
</style>