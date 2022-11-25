import drf from "@/api/drf.js";
import router from "@/router";
import axios from "axios";

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
      access: localStorage.getItem("access") || "",
      userType: null,
      validEmail: false,
      currentUser: {},
      authError: '',
      subjectOptions: [
        "과학",
        "국어",
        "기술가정",
        "사회",
        "수학",
        "보건",
        "한국사",
        "기타",
      ],
      emailOptions: [
        "@gmail.com",
        "@naver.com",
        "@hanmail.com",
        "@nate.com",
        "직접 입력",
      ],
      userInfo: {},
      profil: null,
      findPw: {
        name: null,
        email: null,
        username: null,
      },
    };
  },
  getters: {
    isLoggedIn: (state) => !!state.access,
    currentUser: (state) => state.currentUser,
    authError: (state) => state.authError,
    authHeader: (state) => ({ Authorization: `Bearer ${state.access}` }),
    getUserType: (state) => state.userType,
    getSubject: (state) => state.subjectOptions,
    getEmail: (state) => state.emailOptions,
    isValidEmail: (state) => state.validEmail,
    getUserInfo: (state) => state.userInfo,
    getProfil: (state) => state.profil,
    getInfo: (state) => state.findPw,
    getUsername: (state) => state.currentUser.username,
  },
  mutations: {
    SET_TOKEN: (state, access) => (state.access = access),
    SET_AUTH_ERROR: (state, error) => (state.authError = error),
    CHANGE_DATA(state, data) {
      if (state.userType === "student") {
        for (let key in data) {
          state.studentInfo[key] = data[key];
        }
      } else {
        for (let key in data) {
          state.teacherInfo[key] = data[key];
        }
      }
    },
    SET_USER_TYPE: (state, userType) => (state.userType = userType),
    CHANGE_INFO: (state, data) => {
      for (let key in data) {
        if (key !== "profil") {
          state.userInfo[key] = data[key];
        } else {
          state.profil = data[key];
        }
      }
    },
    CHANGE_PW_INFO: (state, data) => {
      for (let key in data) {
        state.findPw[key] = data[key];
      }
    },
    CHANGE_VALID: (state, data) => {
      state.validEmail = data;
    },
    CURRENTING_USER: (state, currentUser) => {
      for (let key in currentUser) {
        if (key === "access") {
          state.access = currentUser.access;
        } else if (key === "refresh") {
          localStorage.setItem("refresh", currentUser.refresh);
        } else {
          state.currentUser[key] = currentUser[key];
        }
      }
    },
  },
  actions: {
    saveToken({ commit }, access) {
      commit("SET_TOKEN", access);
      localStorage.setItem("access", access);
    },
    removeToken({ commit }) {
      commit("SET_TOKEN", "");
      localStorage.setItem("access", "")
      localStorage.setItem("refresh", "")
    },

    currentingUser({ commit }) {
      if (localStorage.getItem("refresh")) {
        axios({
          url: drf.accounts.currenting(),
          method: "post",
          data: {
            refresh: localStorage.getItem("refresh"),
          },
        }).then((res) => {
          commit("CURRENTING_USER", res.data);
        });
      }
    },

    login({ commit, dispatch }, credentials) {
      axios({
        url: drf.accounts.login(),
        method: "post",
        data: credentials,
      })
        .then((res) => {
          const access = res.data.access;
          dispatch("saveToken", access);
          commit("CURRENTING_USER", res.data);
          router.push({ name: "educolab" });
        })
        .catch((err) => {
          console.log(err.response.data)
          if (err.response.data.message == 'username or password is incorrect!') {
            alert('아이디 또는 비밀번호를 확인해주세요.')
          }
        });
    },
    changeValid({ commit }, data) {
      commit("CHANGE_VALID", data);
    },
    signup({ state, getters, dispatch }) {
      let data = null;
      if (getters.getUserType == "student") {
        data = state.studentInfo;
      } else {
        data = state.teacherInfo;
      }
      axios
        .post(drf.accounts.signup(), data)
        .then(() => {
          window.alert("회원가입이 완료되었습니다");
          // 새로고침 -> vuex에 있는 정보 날려버리기 -> 이동
          router.push({ name: "login" });
        })
        .catch(({ response }) => {
          if (response.data?.email) {
            window.alert(response.data.email[0]);
            dispatch("changeValid", false);
          } else {
            window.alert("필수 항목이 빠져 있거나, 올바르지 않습니다");
          }
        });
    },
    logout({ dispatch }) {
      dispatch("removeToken");
      router.push({ name: "login" });
      router.go(1)
    },
    setUserType({ commit }, userType) {
      // 로그인할 때
      // 회원가입 페이지
      commit("SET_USER_TYPE", userType);
    },
    changeData({ commit }, data) {
      commit("CHANGE_DATA", data);
    },
    changeInfo({ commit }, data) {
      commit("CHANGE_INFO", data);
    },
    changePwInfo({ commit }, data) {
      commit("CHANGE_PW_INFO", data);
    },
  },
};
