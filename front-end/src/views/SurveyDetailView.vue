<template>
  <div>
    <button @click="getSurveyDetail(surveyPk)">상세보기</button>
    <div v-for="survey in surveyItem" :key=survey>
      <p>{{ survey.question_number }}. {{ survey.survey_question }}</p>
      <p>{{ survey.multiple_bogi }}</p>
    </div>

    <!-- <p>{{ surveyPk }}</p> -->
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name : 'SurveyDetailView',
  props: {
    surveyPk : Number
  },
  data() {
  },
  computed: {
    ...mapGetters(['surveyItem'])
  },
  methods: {
    ...mapActions(['getSurveyDetail'])
  },
}
</script>

<style>

</style>