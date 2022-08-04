<template>
  <div>
    <button @click="addSurvey">문항 추가</button>
    <hr>
    <form action="">
      <div v-for="survey in surveyList" :key="survey">
        <select name="" id="" @change="selectedSurvey" v-model="selected">
          <option value="">==문항 선택==</option>
          <option value="choice">객관식 설문조사</option>
          <option value="question">주관식 설문조사</option>
        </select>

        <select name="" id="" @change="selectedSurvey" v-model="selected">
          <option value="">==문항 선택==</option>
          <option value="choice">객관식 설문조사</option>
          <option value="question">주관식 설문조사</option>
        </select>

        <br>

        <div v-if="selected === 'question'">
          <input type="text">주관식 문제
        </div>

        <div v-else-if="selected === 'choice'">
          <div class="q-pa-md">
            <div class="q-gutter-sm" disabled>
              <q-radio v-model="shape" val="0" label="매우 좋음" />
              <q-radio v-model="shape" val="1" label="좋음" />
              <q-radio v-model="shape" val="2" label="중간" />
              <q-radio v-model="shape" val="3" label="나쁨" />
              <q-radio v-model="shape" val="4" label="매우 나쁨" />
            </div>
          </div>
        </div>
      </div>

    </form>
  </div>
</template>

<script>
import {ref} from 'vue'

export default {
  name: 'SurveyCreateView',
  setup () {
    return {
      shape: ref('')
    }
  },
  data() {
    // const surveyList = this.choices + this.questions
    // const surveyTitle = this.surveyList.length
    return {
      selected : '',
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