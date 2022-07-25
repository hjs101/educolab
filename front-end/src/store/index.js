import { createStore } from 'vuex'
import accounts from './accounts.js'

export default createStore({
  state: {
    // 서버 기본 주소
    URL: ''
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    accounts,
  }
})
