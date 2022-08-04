import drf from "@/api/drf.js"
// import router from "@/router"
import axios from "axios"

export const survey = {
  state() {
    return {
      survey : {},
    }
  },
  
  getters: {
    survey : state => state.survey
  },

  mutations: {
    SURVEY_LIST : (state, survey) => state.survey = survey
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
    }
  }
} 