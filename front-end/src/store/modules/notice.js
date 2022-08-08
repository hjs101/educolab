import drf from "@/api/drf.js"
import router from "@/router"
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
    NOTICE_DETAIL : (state, noticeDetail) => state.noticeDetail = noticeDetail,
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
          console.log(res.data)
          commit('NOTICE_DETAIL', res.data)
        })
        .catch(err => {
          console.log(err)
        })
    },

    submitNotice({ getters }, info) {
      console.log('ㅋㅋㅋㅋㅋㅋㅋㅋ')
      axios({
        url: drf.notice.noticeCreate(),
        method: 'post',
        headers: {
          ...getters.authHeader,
          'Content-Type': 'multipart/form-data'
        },
        data : info,
      })
      .then(res => {
          console.log(res.data)
          router.push({ name: 'Notice' })
        })
        .catch(err => {
          console.log(err)
        })
    },

    deleteNotice({ getters }, noticeId) {
      axios({
        url: drf.notice.noticeDetail(),
        method: 'delete',
        headers: getters.authHeader,
        params : {
          notice_num : noticeId
        }
      })
        .then(res => {
          console.log(res)
          alert('해당 글이 삭제되었습니다.')
          router.push({ name : 'Notice'})
        })
    },
    updateNotice({ getters }, credentials, noticePk) {
      console.log(credentials)
      axios({
        url: drf.notice.noticeUpdate(),
        method: 'put',
        headers: getters.authHeader,
        data : credentials,
        params: {
          notice_num : noticePk
        }
      })
        .then(res => {
          console.log(res)
          alert('해당 글이 수정되었습니다.')
          router.push({ name : 'Notice'})
        })
    },
  }
}

// updateArticle({ commit, getters }, { pk, title, content}) {
//   axios({
//     url: drf.articles.article(pk),
//     method: 'put',
//     data: { title, content },
//     headers: getters.authHeader,
//   })
//     .then(res => {
//       commit('SET_ARTICLE', res.data)
//       router.push({
//         name: 'article',
//         params: { articlePk: getters.article.pk }
//       })
//     })
// },
