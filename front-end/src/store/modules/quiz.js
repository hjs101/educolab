import drf from "@/api/drf.js"
import router from "@/router"
// import router from "@/router"
import axios from "axios"

export const quiz = {
  state() {
    return {
      quiz: {},
      quizDetail : {},
      quizData: [{}, {}],
    }
  },

  getters: {
    quiz : state => state.quiz,
    quizDetail : state => state.quizDetail,
    quizData : state => state.quizData,
    quizLength: state => Math.ceil(state.quiz.length/10),
  },

  mutations: {
    SURVEY_LIST : (state, quiz) => state.quiz = quiz,
    QUIZ_DETAIL : (state, quizDetail) => state.quizDetail = quizDetail,
    QUIZ_DATA : (state, data) => state.quizData[data.question_number-1] = data,
  },

  actions: {
    // 퀴즈 조회
    quizList( { getters, commit }) {
      axios({
        url: drf.quiz.quizList(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SURVEY_LIST', res.data)
        })
    },

    // 퀴즈 상세
    getQuizDetail({ getters, commit }, quizPk) {
      axios({
        url: drf.quiz.quizDetail(),
        method: 'get',
        headers: getters.authHeader,
        params: {
          quiz_num : quizPk
        }
      })
        .then(res => {
          console.log(res.data)
          for (var i=1; i < res.data.length; i++) {
            const bogi = res.data[i].multiple_bogi.split('/')
            res.data[i].multiple_bogi = bogi
          }
          commit('QUIZ_DETAIL', res.data)
        })
    },

    // 퀴즈 번호, 보기, 답 가져오기 
    onQuiz( { commit }, data) {
      console.log(data)
      commit('QUIZ_DATA', data)
    },

    createQuiz( { getters }, credentials) {
      credentials.question = getters.quizData
      console.log(credentials)
      axios({
        url: drf.quiz.quizCreate(),
        method: 'post',
        headers: getters.authHeader,
        data : credentials
      })
        .then(router.push({ name: 'Quiz'}))
    },

    deleteQuiz({ getters }, quizPk) {
      axios({
        url: drf.quiz.quizDetail(),
        method: 'delete',
        headers: getters.authHeader,
        params: {
          quiz_num : quizPk
        }
      })
        .then(alert('퀴즈가 삭제되었습니다.')),
        router.push({ name: 'Quiz'})
        .catch(err => {
          console.log(err)
        })
    },

    updateQuiz({ getters }, credentials) {
      credentials.question = getters.quizData
      console.log(credentials)
      axios({
        url: drf.quiz.quizDetail(),
        method: 'put',
        headers: getters.authHeader,
        data : credentials,
      })
        .then(res => {
          console.log(res)
          router.push({ name : 'Quiz' })
        })
    }
  }
}