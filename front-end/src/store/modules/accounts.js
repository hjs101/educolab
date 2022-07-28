// import router from '@/router'
// import axios from 'axios'

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
        number: null,
        phoneNumber: null,
        birthday: null,
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
        birthday: null,
        email: null,
      },
      userType: null,
    }
  },
  getters: {
    // isLoggedIn: state => !!state.token,
    getUserType: state => state.userType,
    getStudentInfo: state => state.studentInfo,
    getTeacherInfo: state => state.teacherInfo,
  },
  mutations: {
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
    // saveToken({commit}, token) {
    //   commit('SET_TOKEN', token)
    //   localStorage.setItem('token', token)
    // },
    login() {

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