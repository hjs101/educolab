import drf from "@/api/drf.js"
import axios from "axios"

export const notice = {
  state() {
    return {
      notice1 : {},
      noticeDetail: {},
    }
  },
  
  getters: {
    notice2 : state => state.notice1,
    noticeItem : state => state.noticeDetail
  },

  mutations: {
    NOTICE_LIST: (state, notice1) => state.notice1 = notice1,
    NOTICE_DETAIL : (state, noticeDetail) => state.noticeDetail = noticeDetail
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
    },

    noticeDetail({ getters, commit }, noticeId) {
      axios({
        url: drf.notice.noticeDetail(),
        method: 'get',
        headers: getters.authHeader,
        params: {
          notice_num : noticeId
        }
      })
        .then(res => {
          console.log('여기는 오니?')
          console.log(res.data)
          commit('NOTICE_DETAIL', res.data)
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}