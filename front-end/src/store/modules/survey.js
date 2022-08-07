import drf from "@/api/drf.js"
import router from "@/router"
import axios from "axios"

export const survey = {
  state() {
    return {
      survey : {},
      surveyData: [{}, {}],
      surveyBogi : [],
      surveyStat: {},
      surveyQuestion: {}
    }
  },
  
  getters: {
    survey : state => state.survey,
    surveyData : state => state.surveyData,
    surveyItem : state => state.surveyItem,
    surveyBogi : state => state.surveyBogi,
    surveyStat : state => state.surveyStat,
    surveyQuestion: state => state.surveyQuestion
  },

  mutations: {
    SURVEY_LIST : (state, survey) => state.survey = survey,
    SURVEY_DATA: (state, data) => state.surveyData[data.question_number-1] = data,
    SURVEY_ITEM: (state, surveyItem) => state.surveyItem = surveyItem,
    SURVEY_BOGI: (state, surveyBogi) => state.surveyBogi = surveyBogi,
    SURVEY_STAT: (state, surveyStat) => state.surveyStat = surveyStat,
    SURVEY_QUESTION: (state, surveyQuestion) => state.surveyQuestion = surveyQuestion
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
      commit('SURVEY_DATA', data)
    },
    submitSurvey({ getters }, credentials) {
      credentials.question = getters.surveyData
      console.log(credentials)
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
    },
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
    updateSurvey({ getters }, {credentials, surveyPk}) {
      credentials.question = getters.surveyData
      credentials.survey_num = surveyPk
      axios({
        url: drf.survey.surveyUpdate(),
        method: 'put',
        headers: getters.authHeader,
        data : credentials,
        params : {
          survey_num : surveyPk
        }
      })
        .then(res => {
          console.log(res)
          router.push({ name : 'Survey' })
        })
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
          commit('SURVEY_STAT', res.data)
        })
        .catch(err => {
          console.log(err)
        })
    },
    onQuestion({ getters, commit }, questionPk) {
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
    }
  },
} 