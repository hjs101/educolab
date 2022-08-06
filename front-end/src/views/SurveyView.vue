<template>
  <div>
    <h1>설문조사</h1>
    <router-link to="/survey/create"><button>설문조사 등록</button></router-link>

    <table>
      <thead>
        <tr>
          <th>번호</th>
          <th>제목</th>
          <th>학년</th>
          <th>반</th>
          <th>생성일</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="survey in survey" :key="survey.pk">
          <td>{{ survey.pk }}</td>
          <td>{{ survey.title }}</td>
          <td>{{ survey.grade }}</td>
          <td>{{ survey.class_field }}</td>
          <td>{{ survey.updated_at }}</td>    
          <button @click="getSurveyDetail(survey.pk)">상세보기</button>
        </tr> 
      </tbody>
    </table>
    <hr>

    <div v-for="surveyItem in surveyItem" :key="surveyItem">
      <p>{{ surveyItem.question_number }}. {{ surveyItem.survey_question }}</p>
      <p>{{ surveyItem.multiple_bogi }}</p>
    </div>

    <p>{{ bogi }}</p>
  <router-view />
  </div>
</template>

<script>
// import { survey } from '@/store/modules/survey'
import { mapActions, mapGetters } from 'vuex'
// import SurveyDetailView from '@/views/SurveyDetailView.vue'

export default {
  name : 'SurveyView',
  data() {
    // let bogi = this.surveyItem.multiple_bogi
    return {
      // bogi
    }
  },
  computed: {
    ...mapGetters(['survey', 'surveyItem'])
  },
  methods : {
    ...mapActions(['surveyList', 'getSurveyDetail']),
    // surveyDetail(surveyPk) {this.$router.push(
    //   { name: 'surveyDetail', params: {surveyPk : surveyPk }})
    // }
  },
  created() {
    this.surveyList()
  }
}

</script>

<style>

</style>