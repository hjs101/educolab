<template>
  <div class="q-mx-xl">
    <h1>설문조사 상세</h1>
    <div v-for="surveyItem in surveyItem" :key="surveyItem.pk">
      <h3>{{ surveyItem.survey_name }}</h3>
      <div v-if="surveyItem.question_number">
        <p>{{ surveyItem.question_number }} . {{ surveyItem.survey_question }}</p>

        <survey-bogi
        :bogi="surveyItem.multiple_bogi"
        :surveyItem="surveyItem"
        :qusNumber="surveyItem.question_number"></survey-bogi>
      </div>
    </div>
    <button @click="deleteSurvey(surveyPk)">설문조사 삭제</button>
    <button @click="updateSurvey(surveyPk)">수정하러 가기!</button>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
// import SurveyBogi from '@/components/SurveyBogi.vue'

export default {
  name : 'SurveyDetailView',
  // props: {
  //   surveyPk : Number
  // },
  // components: { SurveyBogi, },
  data() {
    return {
      surveyPk : this.$route.params.surveyPk
    }
  },
  computed: {
    ...mapGetters(['surveyItem', 'surveyBogi'])
  },
  methods: {
    ...mapActions(['getSurveyDetail', 'deleteSurvey']),
    updateSurvey(surveyPk) {
      this.$router.push({name:'SurveyCreate', params:{surveyPk:surveyPk}})
    }
  },
  created() {
    this.getSurveyDetail(this.surveyPk)
  }
}
</script>

<style>

</style>