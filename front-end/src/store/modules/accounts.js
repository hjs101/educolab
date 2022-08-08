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
        birthday: "2008-01-01",
        email: null,
        userflag: false,
      },
      teacherInfo: {
        username: null,
        password1: null,
        password2: null,
        name: null,
        school: null, // code
        subject: null,
        phone_number: null,
        birthday: "1972-01-01",
        email: null,
        userflag: true,
      },
      userType: null,
      access: localStorage.getItem("access") || "",
      currentUser: {
        userflag : true
      },
      authError: null,
    };
  },
  getters: {
    isLoggedIn: state => !!state.access, 
    currentUser: state => state.currentUser,
    authError: state => state.authError,
    authHeader: state => ({ Authorization: `Bearer ${state.access}` }),
    getUserType: state => state.userType,
    getSubject: state => state.teacherInfo.subject,
  },
  mutations: {
    SET_TOKEN: (state, access) => (state.access = access),
    SET_CURRENT_USER: (state, user) => (state.currentUser = user),
    SET_AUTH_ERROR: (state, error) => (state.authError = error),
    CHANGE_DATA(state, data) {
      if (state.userType === "student") {
        for (let key in data) {
          state.studentInfo[key] = data[key]
        }
      } else {
        for (let key in data) {
          state.teacherInfo[key] = data[key]
        }
      }
    },
    SET_USER_TYPE: (state, userType) => (state.userType = userType),
  },
  actions: {
    saveToken({ commit }, access) {
      commit("SET_TOKEN", access);
      localStorage.setItem("access", access)
    },
    removeToken({ commit }) {
      commit("SET_TOKEN", "");
      localStorage.setItem("access", "")
    },
    initInfo({state, getters, dispatch}) {
      if (getters.getUserType == "student") {
        for (let key in state.studentInfo) {
          if (key === 'userflag') {
            dispatch('changeData', {'userflag':false})
          } else if (key === 'birthday') {
            dispatch('changeData', {'birthday':"2008-01-01"})
          } else {
            dispatch('changeData', {[key]:null})
          }
        }
      } else {
        for (let key in state.teacherInfo) {
          if (key === 'userflag') {
            dispatch('changeData', {'userflag':false})
          } else if (key === 'birthday') {
            dispatch('changeData', {'birthday':"1967-01-01"})
          } else {
            dispatch('changeData', {[key]:null})
          }
        }
      }
    },
    login({ commit, dispatch }, credentials) {
      // 로그인 함수 구현
      axios({
        url: drf.accounts.login(),
        method: "post",
        data: credentials,
      })
        .then((res) => {
          const access = res.data.access
          dispatch("saveToken", access)
          // commit("SET_CURRENT_USER", res.data)
          router.push({ name: "educolab" })
        })
        .catch((err) => {
          commit("SET_AUTH_ERROR", err.response.data)
        });
    },
    signup({state, getters}) {
      let data = null
      if (getters.getUserType == "student") {
        data = state.studentInfo
      } else {
        data = state.teacherInfo
      }
      axios.post(drf.accounts.signup(), data)
        .then(() => {
          window.alert("회원가입이 완료되었습니다")
          router.push({ name: "login" })
          this.initInfo()
        })
        .catch(({response}) => {
          if (response.data?.email) {
            window.alert(response.data.email[0])
          } else {
            window.alert('필수 항목이 빠져 있거나, 올바르지 않습니다')
          }
        })
    },
    logout({ dispatch }) {
      dispatch("removeToken");
      router.push({ name: "login" }).catch((err) => {
        console.log(err.respone);
      });
    },
    setUserType({ commit }, userType) {
      // 로그인할 때
      // 회원가입 페이지
      commit("SET_USER_TYPE", userType)
    },
    changeData({ commit }, data) {
      commit("CHANGE_DATA", data)
    },
  },
};
