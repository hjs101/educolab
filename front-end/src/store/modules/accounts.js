<<<<<<< HEAD
import drf from "@/api/drf"
import router from "@/router"
import axios from "axios"
=======
// import router from '@/router'
// import axios from 'axios'
>>>>>>> 03de9fd (Feat: 회원가입 학교 검색, 이름, 전화번호, 생년월일, 학년/반/번호)

export const accounts = {
  state() {
    return {
<<<<<<< HEAD
=======
      // token: localStorage.getItem('token') || '',
>>>>>>> 03de9fd (Feat: 회원가입 학교 검색, 이름, 전화번호, 생년월일, 학년/반/번호)
      studentInfo: {
        username: null,
        password1: null,
        password2: null,
        name: null,
        school: null, // code
        grade: null,
<<<<<<< HEAD
        class_field: null,
        phone_number: null,
        birthday: '2008-01-01',
        email: null,
        user_flag : false,
=======
        classField: null,
        number: null,
        phoneNumber: null,
        birthday: null,
        email: null,
>>>>>>> 03de9fd (Feat: 회원가입 학교 검색, 이름, 전화번호, 생년월일, 학년/반/번호)
      },
      teacherInfo: {
        username: null,
        password1: null,
        password2: null,
        name: null,
        school: null, // code
        subject: null,
<<<<<<< HEAD
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
=======
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
>>>>>>> 03de9fd (Feat: 회원가입 학교 검색, 이름, 전화번호, 생년월일, 학년/반/번호)
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
        url: drf.accounts.login(),
        method: 'post',
        data: credentials
      })
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
      if (state.userType == 'student') {
        axios.post(drf.accounts.signup(), state.studentInfo)
          .then(() => {
            console.log(state.teacherInfo)
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
    logout({dispatch}) {
        dispatch('removeToken')
        router.push({ name : 'login' })
      .catch(err => {
        console.log(err.respone)
      })
=======
    // saveToken({commit}, token) {
    //   commit('SET_TOKEN', token)
    //   localStorage.setItem('token', token)
    // },
    login() {

    },
    signup() {

    },
    logout() {

>>>>>>> 03de9fd (Feat: 회원가입 학교 검색, 이름, 전화번호, 생년월일, 학년/반/번호)
    },
    setUserType({commit}, userType) {
      // 로그인할 때
      // 회원가입 페이지
      commit('SET_USER_TYPE', userType)
    },
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
    },
  },
}