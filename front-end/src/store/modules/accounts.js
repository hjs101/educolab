// import router from '@/router'
// import axios from 'axios'

import drf from '@/api/drf.js'
import axios from "axios"

export const accounts = {
  state() {
    return {
      // token: localStorage.getItem('token') || '',
      studentInfo: {
        username: null,
        password1: null,
        password2: null,
        name: null,
        school: null, // code
        grade: null,
        classField: null,
        phoneNumber: null,
        birthday: '2008-01-01',
        email: null,
      },
      teacherInfo: {
        username: null,
        password1: null,
        password2: null,
        name: null,
        school: null, // code
        subject: null,
        phoneNumber: null,
        birthday: '1972-01-01',
        email: null,
      },
      userType: null,
    }
  },
  getters: {
    // isLoggedIn: state => !!state.token,
    getUserType: state => state.userType,
    // getStudentInfo: state => state.studentInfo,
    // getTeacherInfo: state => state.teacherInfo,
    getSubject: state => state.teacherInfo.subject,
  },
  mutations: {
    CHANGE_DATA(state, data) {
      console.log(state.userType)
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
    // saveToken({commit}, token) {
    //   commit('SET_TOKEN', token)
    //   localStorage.setItem('token', token)
    // },
    login() {

    },
    signup(state) {
      if (state.userType == 'student') {
        axios.post(drf.accounts.signup(), state.studentInfo)
          .then(() => {
            confirm('회원가입이 완료되었습니다')
            // 자동으로 이동
          })
          .catch(() => {
            confirm('필수 항목이 빠져 있거나, 올바르지 않습니다')
          })
          
        } else if (state.userType == 'teacher') {
        axios.post(drf.accounts.signup(), state.teacherInfo)
          .then(() => {
            confirm('회원가입이 완료되었습니다')
            // 자동으로 이동
          })
          .catch(() => {
            confirm('필수 항목이 빠져 있거나, 올바르지 않습니다')
          })
      }
    },
    logout() {

    },
    setUserType({commit}, userType) {
      // 로그인할 때
      // 회원가입 페이지
      commit('SET_USER_TYPE', userType)
    },
    changeData({commit}, data) {
      console.log(data)
      commit('CHANGE_DATA', data)
    },
  },
}