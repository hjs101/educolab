import drf from "@/api/drf.js"
import router from "@/router"
import axios from "axios"
import { isEmpty } from "lodash"

export const survey = {
  state() {
    return {
      survey : {},
      surveyData: [{}],
      surveyBogi : [],
      surveyStat: {},
      surveyQuestion: {},
      surveyItem : []
    }
  },
  
  getters: {
    survey : state => state.survey,
    surveyData : state => state.surveyData,
    surveyItem : state => state.surveyItem,
    surveyItemLength : state => state.surveyItem.length,
    surveyBogi : state => state.surveyBogi,
    surveyStat : state => state.surveyStat,
    surveyQuestion: state => state.surveyQuestion,
    surveyLength: state => Math.ceil(state.survey.length/10),
  },

  mutations: {
    SURVEY_LIST : (state, survey) => state.survey = survey,
    SURVEY_DATA: (state, data) => state.surveyData[data.question_number-1] = data,
    SURVEY_TOTAL_DATA: (state, data) => state.surveyData = data,
    SURVEY_ITEM: (state, surveyItem) => state.surveyItem = surveyItem,
    SURVEY_BOGI: (state, surveyBogi) => state.surveyBogi = surveyBogi,
    SURVEY_STAT: (state, surveyStat) => state.surveyStat = surveyStat,
    SURVEY_QUESTION: (state, surveyQuestion) => state.surveyQuestion = surveyQuestion,
  },

  actions: {
    surveyList({ getters, commit }) {
      axios({
        url: drf.survey.surveyList(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SURVEY_LIST', res.data)
        })
        .catch(err => {
          console.log(err)
        })
    },
    onSurvey({ commit }, data) {
      console.log(data)
      commit('SURVEY_DATA', data)
    },
    submitSurvey({ getters }, credentials) {
      console.log(credentials)
      const {survey} = credentials
      if (survey.title && survey.grade !== null && survey.class_field !== null) {
        credentials.question = getters.surveyData
        console.log(getters.surveyData)
        console.log(credentials)
        if (isEmpty(...credentials.question)) {
          alert('설문은 한 문항 이상 작성되어야 합니다')
        } else {
          axios({
            url: drf.survey.surveyCreate(),
            method: 'post',
            headers : getters.authHeader,
            data : credentials
          })
            .then(res => {
              console.log(res.data)
              router.push({ name: 'Survey' })
            })
        }
      } else {
        alert('빈 항목을 채워주세요')
      }
    },
    surveyTotalData({commit}, data) {
      console.log(data)
      commit('SURVEY_TOTAL_DATA', data)
    }
    ,
    getSurveyDetail({ getters, commit }, surveyPk) {
      axios({
        url: drf.survey.surveyDetail(),
        method: 'get',
        headers: getters.authHeader,
        params: {
          survey_num : surveyPk
        }
      })
        .then(res => {
          console.log(res.data)
          for(var i = 1; i < res.data.length; i++) {
            if (res.data[i].multiple_bogi) {
              const surveyBogi = res.data[i].multiple_bogi.split('/')
              getters.surveyBogi[i] = surveyBogi
            }
          }
          commit('SURVEY_ITEM', res.data)
        })
        .catch(err => {
          console.log(err)
        })
    },
    deleteSurvey({ getters }, surveyPk) {
      axios({
        url: drf.survey.surveyDetail(),
        method: 'delete',
        headers: getters.authHeader,
        params: {
          survey_num : surveyPk
        } 
      })
        .then(alert('해당 글이 삭제되었습니다.'), 
        router.push({ name : 'Survey' }))
        .catch(err => {
          console.log(err)
        })
    },
    updateSurvey({ getters }, credentials) {
      const {survey} = credentials
      console.log(credentials)
      if (credentials.survey_num && survey.title && survey.grade !== null  && survey.class_field  !== null ) {
        credentials.question = getters.surveyData
        if (isEmpty(...credentials.question)) {
          alert('설문은 한 문항 이상 작성되어야 합니다')
        } else {
          axios({
            url: drf.survey.surveyUpdate(),
            method: 'put',
            headers: getters.authHeader,
            data : credentials,
          })
            .then(res => {
              console.log(res)
              router.push({ name : 'Survey' })
            })
        } 
      } else {
        alert('빈 항목을 채워주세요')
      }
    },

    getSurveyStat({ getters, commit }, surveyPk) {
      axios({
        url: drf.survey.surveyStat(),
        method: 'get',
        headers: getters.authHeader,
        params: {
          survey_num : surveyPk
        }
      })
        .then(res => {
          const totalQuestion = res.data.questions
          for (var i=0; i < totalQuestion.length; i++) {
            if (totalQuestion[i].multiple_bogi) {
              const bogi = totalQuestion[i].multiple_bogi.split('/')
              totalQuestion[i].multiple_bogi = bogi
            }
          }
          for (var j=0; j < totalQuestion.length; j++) {
            const totalNum = totalQuestion[j].num1 + totalQuestion[j].num2 + totalQuestion[j].num3 + totalQuestion[j].num4 + totalQuestion[j].num5
            const purcentNum = [(totalQuestion[j].num1 / totalNum)*100, (totalQuestion[j].num2 / totalNum)*100, 
            (totalQuestion[j].num3 / totalNum)*100, (totalQuestion[j].num4 / totalNum)*100, (totalQuestion[j].num5 / totalNum)*100]
            totalQuestion[j].purcentNum = purcentNum
          }
          console.log(res.data)
          commit('SURVEY_STAT', res.data)
        })
        .catch(err => {
          console.log(err)
        })
    },

    onQuestion({ getters, commit }, questionPk) {
      console.log(questionPk)
      axios({
        url: drf.survey.surveyQuestion(),
        method: 'get',
        headers: getters.authHeader,
        params: {
          question_num : questionPk
        }
      })
        .then(res => {
          console.log(res.data)
          commit('SURVEY_QUESTION', res.data)
        })
        .catch(err => {
          console.log(err)
        })
    },
  },
} 