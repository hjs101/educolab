<template>
  <div class="baseStyle">
    <h4>{{ getTitle }}</h4>

    <div class="row q-mr-xl justify-end">
      <q-btn class="text-size" @click="addSurvey" color="orange-6"  label="문항 추가" />
    </div>

    <div class="row q-gutter-md">
      <q-select class="text-size" style="width:100px;" outlined v-model="credentials.survey.grade" :options="selGrade" label="학년" emit-value map-options/>
      <q-select class="text-size" style="width:100px;" outlined v-model="credentials.survey.class_field" :options="selClassField" label="반" emit-value map-options/>
    </div>

    <div class="row q-mt-xl">
      <span class="q-py-md q-mx-lg text-center text-size">제목</span>
      <q-input class="text-size" outlined v-model="credentials.survey.title" 
      style="width: 700px;" placeholder="설문 제목을 입력해주세요." />
    </div>
    <hr>
    
    <q-form>
      <div v-if="surveyPk">
        <div v-for="survey in surveyList" :key="survey">
          <div class="row justify-end q-mt-xl q-mr-xl">
            <q-btn @click="deleteSurvey(quiz, $event)" class="text-size" color="orange-6">문제 삭제</q-btn>
          </div>
          <survey-item
          :survey="survey"
          :surveyPk="surveyPk"
          />
        </div>
      </div>

      <div v-else>
        <div v-for="survey in surveyList" :key="survey">
          <div class="row justify-end q-mt-md q-mr-xl">
            <q-btn @click="deleteSurvey(survey, $event)" class="text-size" color="orange-6">문항 삭제</q-btn>
          </div>
            <survey-item 
            :survey="survey"
            :surveyPk="surveyPk"/>
        </div>
      </div>
    </q-form>

    <div class="row justify-center q-my-xl">
      <q-btn @click="goSurvey" class="text-size q-px-xl q-py-md" color="grey-8">취소</q-btn>
      <q-btn @click="surveyPk ? updateSurvey(credentials) : submitSurvey(credentials)"
      class="text-size q-px-xl q-py-md q-mx-lg q-py-sm" color="blue-6">
      {{ surveyPk ? '수정' : '등록'}}
      </q-btn>
    </div>
    
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import { useRoute } from 'vue-router'
import { reactive } from 'vue'
import SurveyItem from '../components/SurveyItem.vue'

export default {
  components: { SurveyItem },
  name: 'SurveyCreateView',
  computed: {
    ...mapGetters(['surveyData', 'survey', 'surveyItem' ,'isLoggedIn', 'currentUser', 'surveyItemLength']),
    getTitle() {
      if (this.surveyPk) return "설문조사 수정"
      return "설문조사 등록"
    }
  },
  data() {
    return {
      surveyList : 1
    }
  },
  setup() {
    const route = useRoute()
    const {surveyPk} = route.params
    const credentials = reactive({
      survey_num : surveyPk,
      survey : {
        title : '',
        grade : '',
        class_field: '',
      },
      question: {}
    })
    let surveyDetail = null
    return {
      credentials,
      surveyDetail,
      surveyPk,
      selGrade: [
        {
          label: '전체',
          value: 0
        },
        {
          label: '1학년',
          value: 1
        },
        {
          label: '2학년',
          value: 2
        },
        {
          label: '3학년',
          value: 3
        }
      ],
      selClassField: [
        {
          label: '전체',
          value: 0
        },
        {
          label: '1반',
          value: 1
        },        {
          label: '2반',
          value: 2
        },        {
          label: '3반',
          value: 3
        },        {
          label: '4반',
          value: 4
        },
        {
          label: '5반',
          value: 5
        },        {
          label: '6반',
          value: 6
        },
        {
          label: '7반',
          value: 7
        },        {
          label: '8반',
          value: 8
        },        {
          label: '9반',
          value: 9
        },
        {
          label: '10반',
          value: 10
        },
      ]
    }
  },
  methods: {
    ...mapActions(['submitSurvey', 'getSurveyDetail', 'updateSurvey', 'surveyTotalData']),
    addSurvey() {
      this.surveyList++,
      this.surveyData.push({})
    },
    deleteSurvey(survey, event) {
      if (survey === 1 && this.surveyList === 1) {
        alert('설문은 한 문제 이상 작성되어야 합니다')
      } else if (confirm('문항을 정말 삭제하시겠습니까?')) {
        event.preventDefault()
        this.surveyList = this.surveyList - 1
        this.surveyData.splice(survey-1, 1)
      }
    },
    goSurvey() {
      if (confirm('페이지에서 나가시겠습니까? 글은 저장되지 않습니다.'))
      this.$router.push({name:'Survey'})
    }
  },
  created() {
    if (this.surveyPk) {
      this.getSurveyDetail(this.surveyPk)
      this.credentials.survey.title = this.surveyItem[0]?.survey_name
      this.credentials.survey.grade = this.surveyItem[0]?.survey_grade
      this.credentials.survey.class_field = this.surveyItem[0]?.survey_class
      this.surveyTotalData(this.surveyItem.slice(1,this.surveyItemLength))
      this.surveyList = this.surveyItemLength-1
    }
  }
}
</script>

<style scoped>
  .inputWidth {
    width: 50%;
  }
  .button-color {
    border: 2px solid orange;
  }
  .text-size {
    font-size: 1rem;
  }
  .button-size {
    font-size: 1.1rem;
  }
  .delete-size {
    font-size: 1rem;
  }
</style>

