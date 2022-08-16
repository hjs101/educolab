<template>
  <div class="baseStyle">
    <div v-for="surveyItem in surveyItem" :key="surveyItem">
      <h4 class="title-size">{{ surveyItem.survey_name }}</h4>
      <q-card class="row" v-if="surveyItem.question_number" style="width:80%">
        <q-card-section>
          <p class="text-size">설문문항 {{ surveyItem.question_number }} . {{ surveyItem.survey_question }}</p>
          <survey-bogi
          :bogi="surveyItem.multiple_bogi"
          :surveyItem="surveyItem"
          :qusNumber="surveyItem.question_number"></survey-bogi>
        </q-card-section>
      </q-card>
    </div>

    <div class="row justify-center q-mt-xl q-gutter-md">
      <q-btn @click="deleteSurvey(surveyPk)" class="text-size q-px-xl q-py-md" color="red-6">삭제</q-btn>
      <q-btn @click="updateSurvey(surveyPk)" class="text-size q-px-xl q-py-md" color="blue-6">수정</q-btn>
    </div>
    
    <div class="btn-mag row justify-center">
      <q-btn @click="goSurvey" class="text-size q-px-xl q-py-md" color="grey-8" label="목록"></q-btn>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import SurveyBogi from '@/components/SurveyBogi.vue'
// import { ref } from 'vue'

export default {
  name : 'SurveyDetailView',
  components: { SurveyBogi, },
  // setup() {
  //   return {
  //     alert: ref(false)
  //   }
  // },
  data() {
    return {
      surveyPk : this.$route.params.surveyPk
    }
  },
  computed: {
    ...mapGetters(['surveyItem', 'surveyBogi', 'isLoggedIn', 'currentUser'])
  },
  methods: {
    ...mapActions(['getSurveyDetail', 'deleteSurvey']),
    updateSurvey(surveyPk) {
      this.$router.push({name:'SurveyCreate', params:{surveyPk:surveyPk}})
    },
    goSurvey() {
      this.$router.push({name:'Survey'})
    }
    
  },
  created() {
    if (!this.isLoggedIn) {
      this.$router.push('/educolab/login')
    } else if (!this.currentUser.userflag) {
      this.$router.push('/educolab')
    } else {
      this.getSurveyDetail(this.surveyPk)
    }
  }
}
</script>

<style scoped>
  .title-size {
    font-size : 3vmin;
  }
  .text-size {
    font-size: 2vmin;
  }
  p {
    margin: 0;
  }
  .btn-mag {
    margin-top: 100px;
  }
</style>