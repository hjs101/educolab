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
          <td>{{ survey.pk}}</td>
          <td>{{ survey.title }}</td>
          <td>{{ survey.grade}}</td>
          <td>{{ survey.class_field }}</td>
          <td>{{ survey.updated_at }}</td>          
        </tr> 
      </tbody>
    </table>
  <router-view />
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name : 'SurveyView',
  computed: {
    ...mapGetters(['survey'])
  },
  methods : {
    ...mapActions(['surveyList']),
  },
  created() {
    this.surveyList()
  }
}

</script>

<style>

</style>