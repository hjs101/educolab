<template>
  <div>
    <div class="center">
      설문조사 제목 : <input class="inputWidth" type="text" placeholder="설문조사 제목을 입력해주세요." v-model="credential.survey.title"><br>
    </div>

    <!-- 학년 선택-->
    <select v-model="credential.survey.grade">
      <option value="0">전체</option>
      <option value="1">1학년</option>
      <option value="2">2학년</option>
      <option value="3">3학년</option>
    </select>

    <!-- 반 선택-->
    <select v-model="credential.survey.class_field">
      <option value="0">전체</option>
      <option value="1">1반</option>
      <option value="2">2반</option>
      <option value="4">4반</option>
      <option value="5">5반</option>
      <option value="6">6반</option>
      <option value="7">7반</option>
      <option value="8">8반</option>
      <option value="9">9반</option>
      <option value="10">10반</option>
    </select>
    
    <!-- 문항 선택 -->
    <button class="surveymargin" @click="addSurvey">문항 추가</button>
    <form class="surveymargin">
      <div class="surveymargin" v-for="survey in surveyList" :key="survey">
          <survey-item :survey="survey"/>
            <button @click="deleteSurvey">설문문항 삭제</button>
          <hr>
          
      </div>
    </form>
    <button @click="testSurvey(credential)">설문등록</button>

    <!-- <button></button> -->
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import axios from 'axios'
import SurveyItem from '../components/SurveyItem.vue'
import drf from '@/api/drf'

export default {
  components: { SurveyItem },
  name: 'SurveyCreateView',
  computed: {
    ...mapGetters(['surveyData']),
  },
  data() {
    return {
      credential : {
        survey: {
          title: '',
          grade: '',
          class_field: '',
        },
        question: {},
      },
      surveyList : 2
    }
  },
  methods: {
    addSurvey() {
      this.surveyList++
      
    },
    deleteSurvey(event) {
      event.preventDefault()
      this.surveyList = this.surveyList - 1
    },
    parents() {
      console.log('부모가 받았어!!')
    },
    testSurvey() {
      this.credential.question = this.surveyData
      axios({
        url: drf.survey.surveyCreate(),
        method: 'post',
        headers : this.authHeader,
        data : this.credential
      })
        .then(res => {
          console.log('갑니까?')
          console.log(res)
        })
    }
  }
}
</script>

<style scoped>
  .inputWidth {
    width: 50%;
  }
  .surveymargin {
    margin: 40px;
  }
</style>