import { createStore } from 'vuex'
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e6b54fb (asdu)
import {accounts} from './modules/accounts.js'
=======
import { accounts } from './modules/accounts.js'
import { notice } from './modules/notice.js'
<<<<<<< HEAD
>>>>>>> afe56c9 (공지사항 메인페이지)
=======
import { task } from './modules/task.js'
>>>>>>> 194924a (Feat: 생성 기능 구현 중)

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
<<<<<<< HEAD
    accounts,
<<<<<<< HEAD
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
=======
>>>>>>> e6b54fb (asdu)
=======
    accounts, notice
>>>>>>> afe56c9 (공지사항 메인페이지)
=======
    accounts,
    notice,
    task,
>>>>>>> 194924a (Feat: 생성 기능 구현 중)
  }
})
