// import router from '@/router'
// import axios from 'axios'
// import drf from '@/api/drf/js'

import drf from "@/api/drf"
import router from "@/router"
import Axios from "axios"

export const accounts = {
  state: {
      token: localStorage.getItem('token') || '',
      userInfo: {},
      isLogin: false,
  },
  getters: {
    isLoggedIn: state => !!state.token,
    currentUser: state => state.currentUser,
    getUserType: state => state.userType,
    getStudentInfo: state => state.studentInfo,
    getTeacherInfo: state => state.teacherInfo,
  },
  mutations: {
    loginSuccess(state) {
      state.isLogin = true
    },
    CHANGE_STUDENT_DATA(state,data) {
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
    saveToken({commit}, token) {
      commit('SET_TOKEN', token)
      localStorage.setItem('token', token)
    },
    login({ dispatch }, credentials) {
      // 로그인 함수 구현
      Axios({
        url: drf.accounts.login(),
        method: 'post',
        data: credentials
      })
      console.log(credentials)
        .then(res => {
          const token = res.data.key
          dispatch('saveToken', token)
          router.push({ name: 'Notice'})
        })
        // .catch(err => {
        //   console.err(err.response.data)
        //   commit('')
        // })
    },
    signup() {

    },
    logout() {

    },
    setUserType({commit}, userType) {
      // 로그인할 때
      // 회원가입 페이지
      commit('SET_USER_TYPE', userType)
    },
    changeStudentData({commit}, data) {
      commit('CHANGE_STUDENT_DATA', data)
    },
    changeTeacherData({commit}, data) {
      commit('CHANGE_TEACHER_DATA', data)
    },
  },
}