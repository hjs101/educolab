import drf from "@/api/drf.js"
import axios from "axios"

export const notice = {
  state() {
    return {
      notice1 : {},
    }
  },
  
  getters: {
    notice2 : state => state.notice1
  },

  mutations: {
    NOTICE_LIST: (state, notice1) => state.notice1 = notice1 
  },

  actions: {
    noticeList({ commit, getters }) {
      axios({
        url: drf.notice.noticeList(),
        method : 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          console.log(res.data)
          commit('NOTICE_LIST', res.data)
        })
        .catch(err => {
          console.log(err.data)
        })
    }
  }
}