<template>
  <div>
    <button @click="addSurvey">문항 추가</button>
    <hr>
    <form action="">
      <div v-for="survey in surveyList" :key="survey">
        <survey-item :survey="survey"/>
      </div>

    </form>
  </div>
</template>

<script>
import SurveyItem from '../components/SurveyItem.vue'

export default {
  components: { SurveyItem },
  name: 'SurveyCreateView',
  data() {
    // const surveyList = this.choices + this.questions
    // const surveyTitle = this.surveyList.length
    return {
      surveyList : 1
      // questions: 1,
      // surveyList: [],
      // surveyTitle
    }
  },
  methods: {
    addSurvey() {
      this.surveyList++
    }
    // selectedSurvey() {
    //   this.surveyList.push(this.selected1)
    // }
    // addChoice() {
    //   this.choices++ 
    // },
    // deleteChoice() {
    //   this.choices--
    // },
    // addquestion() {
    //   this.questions++
    // },
    // deletequestion() {
    //   this.questions--
    // }
  }
}
</script>

<style>

</style>