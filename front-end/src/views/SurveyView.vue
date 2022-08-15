<template>
  <div class="baseStyle">
    <h4 class="text-center">설문조사</h4>
    <hr>
    <div class="row justify-end q-mt-lg">
      <q-btn @click="surveyCreate" class="text-size q-mx-lg q-py-sm"
      color="blue-6" label="설문 등록" />
    </div>

    <!-- 설문조사 전체 조회 -->
    <div class="q-pa-md">
      <q-markup-table class="survey-full">
        <thead>
          <tr>
            <th class="text-center text-size">번호</th>
            <th class="text-center text-size">제목</th>
            <th class="text-center text-size">학년</th>
            <th class="text-center text-size">반</th>
            <th class="text-center text-size">등록(수정)일</th>
            <th class="text-center text-size">설문 통계</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(survey, index) in survey.slice((page-1)*10, page*10)" :key="index">
            <td class="text-center text-size">{{ index+1+((page-1)*10) }}</td>
            <td @click="surveyDetail(survey.pk)" class="text-size cursor-pointer">{{ survey.title }}</td>
            <td class="text-center text-size">{{ survey.grade }}</td>
            <td class="text-center text-size">{{ survey.class_field }}</td>
            <td class="text-center text-size">{{ timeInfo(survey.updated_at) }}</td>
            <td @click="onSurveyStat(survey.pk)" class="cursor-pointer text-center text-size">통계보기</td>
          </tr>
        </tbody>
      </q-markup-table>

      <q-markup-table class="survey-small">
        <thead>
          <tr>
            <th class="text-center text-size">제목</th>
            <th class="text-center text-size">학년</th>
            <th class="text-center text-size">반</th>
            <th class="text-center text-size">설문 통계</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(survey,index) in survey.slice((page-1)*10, page*10)" :key="index">
            <td @click="surveyDetail(survey.pk)" class="text-size cursor-pointer">{{ survey.title }}</td>
            <td class="text-center text-size">{{ survey.grade }}</td>
            <td class="text-center text-size">{{ survey.class_field }}</td>
            <td @click="onSurveyStat(survey.pk)" class="cursor-pointer text-center text-size">통계보기</td>
          </tr>
        </tbody>
      </q-markup-table>
    </div>

    <div>
      <the-pagi-nation v-if="surveyLength" :limit="surveyLength" @change-page="changePage">
      </the-pagi-nation>
    </div>   

  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import { ref } from 'vue'
import ThePagiNation from '@/components/ThePagination.vue'

export default {
  name : 'SurveyView',
  components: {ThePagiNation},
  setup() {
    let page = ref(1)
    const changePage = (value) => {
      page.value = value
    }
    return {
      page,
      changePage,
      alert : ref(false)
    }
  },
  computed: {
    ...mapGetters(['survey', 'surveyLength', ]),
  },
  methods : {
    ...mapActions(['surveyList', 'getSurveyDetail',]),
    timeInfo(time) {
      const d = new Date(time)
      return d.getFullYear() + ". " + (d.getMonth()+1) + ". " + d.getDate()
    },
    surveyCreate() {
      this.$router.push({name:'SurveyCreate'})
    },
    surveyDetail(surveyPk) {
      this.$router.push({name:'SurveyDetail', params:{ surveyPk:surveyPk }})
    },
    onSurveyStat(surveyPk) {
      this.$router.push({name:'SurveyStat', params:{ surveyPk: surveyPk}},)
    },

  },
  created() {
    this.surveyList()
  }
}

</script>

<style scoped>
  .text-size {font-size:1rem;}
  .surveyMargin {margin-right : 10px;}
  .test {position: relative;}
  .test2 {text-decoration: none;}
  .button-size {
    font-size: 1rem;
  }
  .survey-small {
    display: none;
  }
  @media screen and (max-width: 815px) {
    .survey-full {
      display: none;
    }
    .survey-small {
      display: block;
    }
  }
</style>