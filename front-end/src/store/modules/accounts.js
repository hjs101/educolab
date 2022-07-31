import drf from "@/api/drf.js"
import router from "@/router"
import axios from "axios"

export const accounts = {
  state() {
    return {
      studentInfo: {
        username: null,
        password1: null,
        password2: null,
        name: null,
        school: null, // code
        grade: null,
        class_field: null,
        phone_number: null,
        birthday: '2008-01-01',
        email: null,
        user_flag : false,
      },
      teacherInfo: {
        username: null,
        password1: null,
        password2: null,
        name: null,
        school: null, // code
        subject: null,
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
      if (state.getters.getUserType == 'student') {
        axios.post(drf.accounts.signup(), state.state.studentInfo)
          .then(() => {
            console.log(state.teacherInfo)
            window.alert('회원가입이 완료되었습니다')
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