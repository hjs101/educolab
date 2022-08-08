<template>
  <div class="q-mx-xl">
    <h1>설문조사</h1>
    <router-link to="/survey/create"><button>설문조사 등록</button></router-link>

    <!-- 설문조사 전체 조회 -->
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
          <router-link :to="{name:'SurveyDetail', params: {surveyPk:`${survey.pk}`}}">
            <td>{{ survey.title }}</td>
          </router-link>
          <td>{{ survey.grade }}</td>
          <td>{{ survey.class_field }}</td>
          <td>{{ timeInfo(survey.updated_at) }}</td> 
          <router-link :to="{name:'SurveyStat', params: {surveyPk:`${survey.pk}`}}">
            <button @click="surveyStat(survey.pk)">통계보기</button>
          </router-link>
        </tr> 
      </tbody>
    </table>
    <hr>

  <router-view />
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name : 'SurveyView',
  data() {
    return {
      onButton : false,
    }
  },
  computed: {
    ...mapGetters(['survey',]),
  },
  methods : {
    ...mapActions(['surveyList', 'getSurveyDetail', 'getSurveyStat']),
    timeInfo(time) {
      const d = new Date(time)
      return d.getFullYear() + ". " + (d.getMonth()+1) + ". " + d.getDate()
    },
    surveyStat(surveyPk) {
      this.getSurveyStat(surveyPk)
    }
  },
  created() {
    this.surveyList()
  }
}

</script>

<style scoped>
  .surveyMargin {
    margin-right : 10px;
  }
  .test {
    position: relative;
  }
</style>