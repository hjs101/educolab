<template>
  <div>
    <h1>{{ getTitle }}</h1>
    <div class="center">
      설문조사 제목 : <input class="inputWidth" type="text" placeholder="설문조사 제목을 입력해주세요." v-model="credentials.survey.title"><br>
    </div>

    <!-- 학년 선택-->
    <select v-model="credentials.survey.grade">
      <option value="0">전체</option>
      <option value="1">1학년</option>
      <option value="2">2학년</option>
      <option value="3">3학년</option>
    </select>

    <!-- 반 선택-->
    <select v-model="credentials.survey.class_field">
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
          <survey-item 
          :survey="survey"
          :surveyPk="surveyPk"/>
          <button @click="deleteSurvey(survey, $event)">설문문항 삭제</button>
          <hr>
      </div>
    </form>
    <button @click="surveyPk ? updateSurvey({credentials, surveyPk}) : submitSurvey(credentials)">
    {{ surveyPk ? '설문조사 수정' : '설문조사 등록'}}
    </button>

  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import SurveyItem from '../components/SurveyItem.vue'

export default {
  components: { SurveyItem },
  name: 'SurveyCreateView',
  computed: {
    ...mapGetters(['surveyData', 'survey']),
    getTitle() {
      if (this.surveyPk) return "설문조사 수정"
      return "설문조사 등록"
    }
  },
  data() {
    return {
      surveyPk : this.$route.params.surveyPk,
      credentials : {
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
    ...mapActions(['submitSurvey', 'getSurveyDetail', 'updateSurvey']),
    addSurvey() {
      this.surveyList++,
      this.surveyData.push({})
    },
    deleteSurvey(survey, event) {
      event.preventDefault()
      this.surveyList = this.surveyList - 1
      this.surveyData.splice(survey-1, 1)
    },
  },
  mounted() {
    if (this.surveyPk) {
      for (var i=0; i < this.survey.length; i++) {
        if (this.surveyPk == this.survey[i].pk) {
          this.credentials.survey.title = this.survey[i].title
          this.credentials.survey.grade = this.survey[i].grade
          this.credentials.survey.class_field = this.survey[i].class_field
          return
        }
      }
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

