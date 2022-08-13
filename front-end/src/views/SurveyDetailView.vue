<template>
  <div class="baseStyle">
    <div v-for="surveyItem in surveyItem" :key="surveyItem">
      <h4>{{ surveyItem.survey_name }}</h4>
      <div class="q-mx-md" v-if="surveyItem.question_number">
        <p class="title-size">설문문항 {{ surveyItem.question_number }} : {{ surveyItem.survey_question }}</p>
        <survey-bogi
        :bogi="surveyItem.multiple_bogi"
        :surveyItem="surveyItem"
        :qusNumber="surveyItem.question_number"></survey-bogi>
      </div>
    </div>

    <div class="row justify-center q-mt-xl q-gutter-md">
      <q-btn @click="deleteSurvey(surveyPk)" class="text-size q-px-xl q-py-sm" color="red-6">삭제</q-btn>
      <q-btn @click="updateSurvey(surveyPk)" class="text-size q-px-xl q-py-sm" color="blue-6">수정</q-btn>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import SurveyBogi from '@/components/SurveyBogi.vue'

export default {
  name : 'SurveyDetailView',
  components: { SurveyBogi, },
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

<style scoped>
  .title-size {
    font-size : 1.5rem;
  }
  .text-size {
    font-size: 1.2rem;
  }

</style>