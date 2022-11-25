<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
import drf from "@/api/drf"
=======
import drf from "@/api/drf.js"
>>>>>>> f57c6b5 ( Fix : get 방식으로 요청)
import router from "@/router"
import axios from "axios"
=======
// import router from '@/router'
// import axios from 'axios'
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 03de9fd (Feat: 회원가입 학교 검색, 이름, 전화번호, 생년월일, 학년/반/번호)
=======
// import drf from '@/api/drf/js'
>>>>>>> 2091835 (Feat: merge 전 수정 사항 반영)

=======
>>>>>>> c64b335 (유저정보  테스트)
import drf from "@/api/drf"
import router from "@/router"
=======

import drf from '@/api/drf.js'
>>>>>>> 89ccfeb ( Feat: 회원 가입 기능 완료 (백 통신해서 디버깅 해야 함))
import axios from "axios"

export const accounts = {
<<<<<<< HEAD
  state() {
    return {
<<<<<<< HEAD
<<<<<<< HEAD
=======
      // token: localStorage.getItem('token') || '',
>>>>>>> 03de9fd (Feat: 회원가입 학교 검색, 이름, 전화번호, 생년월일, 학년/반/번호)
=======
>>>>>>> 80ba160 ( Feat : 백과의 통신 (학교 검색과 회원가입은 미완료))
=======
import drf from "@/api/drf.js"
import router from "@/router"
import axios from "axios"

export const accounts = {
  state() {
    return {
>>>>>>> e6b54fb (asdu)
      studentInfo: {
        username: null,
        password1: null,
        password2: null,
        name: null,
        school: null, // code
        grade: null,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e6b54fb (asdu)
        class_field: null,
        phone_number: null,
        birthday: '2008-01-01',
        email: null,
        user_flag : false,
<<<<<<< HEAD
=======
        classField: null,
        phoneNumber: null,
        birthday: '2008-01-01',
        email: null,
>>>>>>> 03de9fd (Feat: 회원가입 학교 검색, 이름, 전화번호, 생년월일, 학년/반/번호)
=======
        class_field: null,
        phone_number: null,
        birthday: '2008-01-01',
        email: null,
        user_flag : false,
>>>>>>> 6e582c6 (develop 브랜치 푸시)
=======
>>>>>>> e6b54fb (asdu)
      },
      teacherInfo: {
        username: null,
        password1: null,
        password2: null,
        name: null,
        school: null, // code
        subject: null,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 6e582c6 (develop 브랜치 푸시)
=======
>>>>>>> e6b54fb (asdu)
        phone_number: null,
        birthday: '1972-01-01',
        email: null,
        user_flag : true,
      },
      userType: null,
      access: localStorage.getItem('access') || '',
      currentUser: {},
      authError: null,
    }
  },
  getters: {
    isLoggedIn: state => !!state.access, 
    currentUser: state => state.currentUser,
    authError: state => state.authError,
    authHeader: state => ({ Authorization: `Token ${state.access}` }),
    getUserType: state => state.userType,
    // getStudentInfo: state => state.studentInfo,
    // getTeacherInfo: state => state.teacherInfo,
    getSubject: state => state.teacherInfo.subject,
  },
  mutations: {
    SET_TOKEN: (state, access) => state.access = access,
    SET_CURRENT_USER: (state, user) => state.currentUser = user,
    SET_AUTH_ERROR: (state, error) => state.authError = error,
    CHANGE_DATA(state,data) {
<<<<<<< HEAD
=======
        phoneNumber: null,
        birthday: '1972-01-01',
        email: null,
      },
      userType: null,
    }
=======
  state: {
<<<<<<< HEAD
      token: localStorage.getItem('token') || '',
      userInfo: {},
      isLogin: false,
>>>>>>> c942112 (로그인 프론트와 백 연결)
=======
      access: localStorage.getItem('access') || '',
      currentUser: {},
      authError: null,
>>>>>>> 77a4159 (로그아웃 구현)
  },
  getters: {
    isLoggedIn: state => !!state.access,
    currentUser: state => state.currentUser,
    authError: state => state.authError,
    authHeader: state => ({ Authorization: `Token ${state.access}` }),
    getUserType: state => state.userType,
    // getStudentInfo: state => state.studentInfo,
    // getTeacherInfo: state => state.teacherInfo,
    getSubject: state => state.teacherInfo.subject,
  },
  mutations: {
<<<<<<< HEAD
    SET_TOKEN: (state, access) => state.access = access,
    SET_CURRENT_USER: (state, user) => state.currentUser = user,
    SET_AUTH_ERROR: (state, error) => state.authError = error,
    CHANGE_STUDENT_DATA(state,data) {
>>>>>>> 03de9fd (Feat: 회원가입 학교 검색, 이름, 전화번호, 생년월일, 학년/반/번호)
=======
    CHANGE_DATA(state, data) {
<<<<<<< HEAD
>>>>>>> bb316aa ( Feat : 회원가입 시 입력받은 정보를 취합하는 중)
=======
      console.log(state.userType)
>>>>>>> 89ccfeb ( Feat: 회원 가입 기능 완료 (백 통신해서 디버깅 해야 함))
=======
>>>>>>> e6b54fb (asdu)
      if (state.userType === 'student') {
        for (let key in data) {
          state.studentInfo[key] = data[key]
        }
      } else {
          for (let key in data) {
            state.teacherInfo[key] = data[key]
          }
        }
      },
    SET_USER_TYPE: (state, userType) => state.userType = userType,
    },
  actions: {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e6b54fb (asdu)
    saveToken({commit}, access) {
      commit('SET_TOKEN', access)
      localStorage.setItem('access', access)
    },
    removeToken({commit}) {
      commit('SET_TOKEN', '')
      localStorage.setItem('access', '')
    },
    login({ commit, dispatch }, credentials) {
      // 로그인 함수 구현
      axios({
<<<<<<< HEAD
<<<<<<< HEAD
=======
    saveToken({commit}, token) {
      commit('SET_TOKEN', token)
      localStorage.setItem('token', token)
=======
    saveToken({commit}, access) {
      commit('SET_TOKEN', access)
      localStorage.setItem('access', access)
>>>>>>> 77a4159 (로그아웃 구현)
    },
    removeToken({commit}) {
      commit('SET_TOKEN', '')
      localStorage.setItem('access', '')
    },
    login({ commit, dispatch }, credentials) {
      // 로그인 함수 구현
      Axios({
>>>>>>> c942112 (로그인 프론트와 백 연결)
=======
>>>>>>> c64b335 (유저정보  테스트)
=======
>>>>>>> e6b54fb (asdu)
        url: drf.accounts.login(),
        method: 'post',
        data: credentials
      })
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e6b54fb (asdu)
        .then(res => {
          console.log(res)
          const access = res.data.access
          dispatch('saveToken', access)
          commit('SET_CURRENT_USER', res.data) 
          router.push({ name: 'educolab'})
        })         
        .catch(err => {
          console.error(err.response.data)
          commit('SET_AUTH_ERROR', err.response.data)
        })
    },
    signup(state) {
      if (state.getters.getUserType == 'student') {
        axios.post(drf.accounts.signup(), state.state.studentInfo)
          .then(() => {
            console.log(state.teacherInfo)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            confirm('회원가입이 완료되었습니다')
=======
            window.alert('회원가입이 완료되었습니다')
>>>>>>> f57c6b5 ( Fix : get 방식으로 요청)
=======
            window.alert('회원가입이 완료되었습니다')
>>>>>>> e6b54fb (asdu)
            // 자동으로 이동
          })
          .catch(() => {
            window.alert('필수 항목이 빠져 있거나, 올바르지 않습니다')
          })
          
        } else if (state.getters.getUserType == 'teacher') {
        axios.post(drf.accounts.signup(), state.state.teacherInfo)
          .then(() => {
            console.log(state.studentInfo)
            window.alert('회원가입이 완료되었습니다')
            // 자동으로 이동
          })
          .catch(() => {
            window.alert('필수 항목이 빠져 있거나, 올바르지 않습니다')
          })
      }
    },
    logout({dispatch}) {
        dispatch('removeToken')
        router.push({ name : 'login' })
      .catch(err => {
        console.log(err.respone)
      })
<<<<<<< HEAD
=======
    // saveToken({commit}, token) {
    //   commit('SET_TOKEN', token)
    //   localStorage.setItem('token', token)
    // },
    login() {

=======
      console.log(credentials)
=======
>>>>>>> 77a4159 (로그아웃 구현)
        .then(res => {
          console.log(res)
          const access = res.data.access
          dispatch('saveToken', access)
          commit('SET_CURRENT_USER', res.data) 
          router.push({ name: 'nav'})
        })         
        .catch(err => {
          console.error(err.response.data)
          commit('SET_AUTH_ERROR', err.response.data)
        })
<<<<<<< HEAD
        // .catch(err => {
        //   console.err(err.response.data)
        //   commit('')
        // })
>>>>>>> c942112 (로그인 프론트와 백 연결)
=======
>>>>>>> 77a4159 (로그아웃 구현)
    },
    signup(state) {
      if (state.userType == 'student') {
        axios.post(drf.accounts.signup(), state.studentInfo)
          .then(() => {
=======
>>>>>>> 80ba160 ( Feat : 백과의 통신 (학교 검색과 회원가입은 미완료))
            confirm('회원가입이 완료되었습니다')
            // 자동으로 이동
          })
          .catch(() => {
            confirm('필수 항목이 빠져 있거나, 올바르지 않습니다')
          })
          
        } else if (state.userType == 'teacher') {
        axios.post(drf.accounts.signup(), state.teacherInfo)
          .then(() => {
            console.log(state.studentInfo)
            confirm('회원가입이 완료되었습니다')
            // 자동으로 이동
          })
          .catch(() => {
            confirm('필수 항목이 빠져 있거나, 올바르지 않습니다')
          })
      }
    },
<<<<<<< HEAD
    logout() {

>>>>>>> 03de9fd (Feat: 회원가입 학교 검색, 이름, 전화번호, 생년월일, 학년/반/번호)
=======
    logout({dispatch}) {
        dispatch('removeToken')
        router.push({ name : 'login' })
      .catch(err => {
        console.log(err.respone)
      })
>>>>>>> 77a4159 (로그아웃 구현)
=======
>>>>>>> e6b54fb (asdu)
    },
    setUserType({commit}, userType) {
      // 로그인할 때
      // 회원가입 페이지
      commit('SET_USER_TYPE', userType)
    },
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    changeData({commit}, data) {
      console.log(data)
      commit('CHANGE_DATA', data)
=======
    changeStudentData({commit}, data) {
      commit('CHANGE_STUDENT_DATA', data)
    },
    changeTeacherData({commit}, data) {
      commit('CHANGE_TEACHER_DATA', data)
>>>>>>> 03de9fd (Feat: 회원가입 학교 검색, 이름, 전화번호, 생년월일, 학년/반/번호)
=======
    changeData({commit}, data) {
      console.log(data)
      commit('CHANGE_DATA', data)
>>>>>>> bb316aa ( Feat : 회원가입 시 입력받은 정보를 취합하는 중)
=======
    changeData({commit}, data) {
      console.log(data)
      commit('CHANGE_DATA', data)
>>>>>>> e6b54fb (asdu)
    },
  },
}