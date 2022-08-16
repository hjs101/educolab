import drf from "@/api/drf.js"
// import router from "@/router"
import axios from "axios"

export const mainpage = {
  state() {
    return {
      mainNotice: {},
      mainHomework: {},
      mainWeekRank: {},
      mainAccRank: {},
    }
  },

  getters: {
    mainNotice: state => state.mainNotice,
    mainHomework: state => state.mainHomework,
    mainWeekRank: state => state.mainWeekRank,
    mainAccRank: state => state.mainAccRank,
  },

  mutations: {
    MAIN_NOTICE: (state, mainNotice) => state.mainNotice = mainNotice,
    MAIN_HOMEWORK: (state, mainHomework) => state.mainHomework = mainHomework,
    MAIN_WEEK_RANK: (state, mainWeekRank) => state.mainWeekRank = mainWeekRank,
    MAIN_ACC_RANK: (state, mainAccRank) => state.mainAccRank = mainAccRank,
  },

  actions: {
    getMainPage({ getters, commit}) {
      axios({
        url: drf.mainpage.mainItem(),
        method: 'get',
        headers: getters.authHeader
      })
        .then(res => {
          commit('MAIN_NOTICE', res.data.notice)
          commit('MAIN_HOMEWORK', res.data.homework)
          commit('MAIN_ACC_RANK', res.data.acc_rank)
          commit('MAIN_WEEK_RANK', res.data.week_rank)
        })
    }
  }
}