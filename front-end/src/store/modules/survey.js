import drf from "@/api/drf.js"
import router from "@/router"
import axios from "axios"

export const survey = {
  state() {
    return {
      survey : {},
      surveyData: [{}, {}],
      // surveyItem : {}
    }
  },
  
  getters: {
    survey : state => state.survey,
    surveyData : state => state.surveyData,
    surveyItem: state => state.surveyItem,
  },

  mutations: {
    SURVEY_LIST : (state, survey) => state.survey = survey,
    SURVEY_DATA: (state, data) => state.surveyData[data.question_number-1] = data,
    SURVEY_ITEM: (state, surveyItem) => state.surveyItem = surveyItem,
  },

  actions: {
    surveyList({ getters, commit }) {
      axios({
        url: drf.survey.surveyList(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          console.log(res)
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
      credentials.question = getters.surveyData
      console.log(credentials.question)
      axios({
        url: drf.survey.surveyCreate(),
        method: 'post',
        headers : getters.authHeader,
        data : credentials
      })
        .then(res => {
          console.log(res)
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
          console.log(res.data)
          commit('SURVEY_ITEM', res.data)
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
} 