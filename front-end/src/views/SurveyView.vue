<template>
  <div class="baseStyle">
    <img src="@/assets/설문조사.png" alt="survey" style="height:200px;">
    <div class="row justify-end">
      <q-btn @click="surveyCreate" class="text-size q-mx-lg q-py-sm"
      color="green-13" label="설문 등록" />
    </div>

    <!-- 설문조사 전체 조회 -->
    <div class="q-pa-md">
      <q-markup-table>
        <thead>
          <tr>
            <th class="text-left text-size">번호</th>
            <th class="text-center text-size">제목</th>
            <th class="text-center text-size">학년</th>
            <th class="text-center text-size">반</th>
            <th class="text-center text-size">생성일</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="survey in survey" :key="survey.pk">
            <td class="text-left text-size">{{ survey.pk }}</td>
            <td @click="surveyDetail(survey.pk)" class="text-size cursor-pointer">{{ survey.title }}</td>
            <td class="text-center text-size">{{ survey.grade }}</td>
            <td class="text-center text-size">{{ survey.class_field }}</td>
            <td class="text-center text-size">{{ timeInfo(survey.updated_at) }}</td>
          </tr>
        </tbody>
      </q-markup-table>
    </div>
    <!-- <table>
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
            <td class="test2">{{ survey.title }}</td>
          </router-link>
          <td>{{ survey.grade }}</td>
          <td>{{ survey.class_field }}</td>
          <td>{{ timeInfo(survey.updated_at) }}</td> 
          <router-link :to="{name:'SurveyStat', params: {surveyPk:`${survey.pk}`}}">
            <button @click="surveyStat(survey.pk)">통계보기</button>
          </router-link>
        </tr> 
      </tbody>
    </table> -->
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

    surveyCreate() {
      this.$router.push({name:'SurveyCreate'})
    },
    surveyDetail(surveyPk) {
      this.$router.push({name:'surveyDetail', params:{ surveyPk:surveyPk }})
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
  .text-size {font-size:1.2rem;}
  .surveyMargin {margin-right : 10px;}
  .test {position: relative;}
  .test2 {text-decoration: none;}
</style>