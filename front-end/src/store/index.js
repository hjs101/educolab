import { createStore } from 'vuex'
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
=======
import accounts from './accounts.js'
>>>>>>> 23e74e9 (Feat : 로그인 화면 제작 완료 & 기능 구현 미완료 & 약관 동의 화면 구현)
=======
import {accounts} from './modules/accounts.js'
>>>>>>> 03de9fd (Feat: 회원가입 학교 검색, 이름, 전화번호, 생년월일, 학년/반/번호)

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
<<<<<<< HEAD
>>>>>>> 1f63946 (vue 환경셋팅)
=======
    accounts,
>>>>>>> 23e74e9 (Feat : 로그인 화면 제작 완료 & 기능 구현 미완료 & 약관 동의 화면 구현)
  }
})
