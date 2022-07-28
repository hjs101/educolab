import { createStore } from 'vuex'
import {accounts} from './modules/accounts.js'

export default createStore({
  state () {
    return {
      // 서버 기본 주소
      URL: ''
    }
  },
  getters() {

  },
  mutations() {
  },
  actions() {
  },
  modules: {
    accounts,
  }
})
