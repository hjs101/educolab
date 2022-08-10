import { createStore } from 'vuex'
<<<<<<< HEAD
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
<<<<<<< HEAD
>>>>>>> afe56c9 (공지사항 메인페이지)
=======
import { task } from './modules/task.js'
>>>>>>> 194924a (Feat: 생성 기능 구현 중)
=======
import { survey } from './modules/survey.js'
<<<<<<< HEAD
>>>>>>> 452a9d1 (설문조사  등록)
=======
import { quiz } from './modules/quiz.js'
<<<<<<< HEAD
>>>>>>> c9ecd87 (퀴즈 임베디드 연동)
=======
import { accounts } from './modules/accounts.js'
import { notice } from './modules/notice.js'
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
=======
import { mainpage } from './modules/mainpage.js'
>>>>>>> e824b6b (메인페이지 화면 구성)

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
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
    accounts, notice, survey
>>>>>>> 452a9d1 (설문조사  등록)
=======
    accounts, notice, survey, quiz
>>>>>>> c9ecd87 (퀴즈 임베디드 연동)
=======
    accounts, notice
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
=======
    accounts, notice, survey, quiz, mainpage
>>>>>>> e824b6b (메인페이지 화면 구성)
  }
})
