import drf from "@/api/drf.js"
// import router from "@/router"
import axios from "axios"

export const survey = {
  state() {
    return {
      survey : {},
      surveyData: [{}, {}],
    }
  },
  
  getters: {
    survey : state => state.survey,
    surveyData : state => state.surveyData
  },

  mutations: {
    SURVEY_LIST : (state, survey) => state.survey = survey,
    SURVEY_DATA: (state, data) => state.surveyData[data.question_number-1] = data
    
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
    goSurvey({commit}, data) {
      console.log(data)
      commit('SURVEY_DATA', data)
    }
  }
} 