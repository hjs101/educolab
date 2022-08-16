<<<<<<< HEAD
<<<<<<< HEAD
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
=======
import drf from "@/api/drf.js";
import router from "@/router";
import axios from "axios";
>>>>>>> 36a3f8f (Fix : 오타수정)
=======
import drf from "@/api/drf.js"
import router from "@/router"
import axios from "axios"
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)

export const accounts = {
  state() {
    return {
<<<<<<< HEAD
>>>>>>> e6b54fb (asdu)
=======
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
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
<<<<<<< HEAD
=======
>>>>>>> e6b54fb (asdu)
=======
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
        class_field: null,
        phone_number: null,
        birthday: "2008-01-01",
        email: null,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
        userflag : false,
>>>>>>> 0929323 ( Feat : 회원가입 기능 구현)
=======
        userflag: false,
>>>>>>> 36a3f8f (Fix : 오타수정)
=======
        userflag: false,
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
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
<<<<<<< HEAD
=======
>>>>>>> 6e582c6 (develop 브랜치 푸시)
=======
>>>>>>> e6b54fb (asdu)
=======
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
        phone_number: null,
        birthday: "1972-01-01",
        email: null,
        userflag: true,
      },
      userType: null,
      validEmail: false,
      access: localStorage.getItem("access") || "",
<<<<<<< HEAD
      currentUser: {
        userflag : true
      },
      authError: null,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
      subjectOptions : [
        '국어', '수학', '사회', '과학', '보건', '기술가정', '기타'
<<<<<<< HEAD
      ]
>>>>>>> 194924a (Feat: 생성 기능 구현 중)
    };
=======
      // 비밀번호 변경 페이지 들어가기 전 인증을 거쳤는지 여부
      hasPermission: false,
=======
>>>>>>> d7025b4 (Feat : 비밀번호 변경 페이지 제작 & 컴포넌트화 & 비밀번호 변경 기능 진행 중)
    }
>>>>>>> 9c886eb (Feat : 이메일 인증 부분 수정 & 아이디/비밀번호 찾기 기능 완료 & 비밀번호 변경 기능 진행 중)
=======
      ],
      emailOptions: [
        '@gmail.com', '@naver.com', '@hanmail.com', '@nate.com', '직접 입력',
      ],
      userInfo: {},
      profil: null,
      findPw: {
        name: null,
        email: null,
        username: null,
      }
    }
>>>>>>> fa227ef (Feat & Fix : 과제 생성/수정 기능 완료, 나머지 기능 진행 중, 회원 관리 부분 컴포넌트화 및 버그 수정 중)
  },
  getters: {
<<<<<<< HEAD
<<<<<<< HEAD
    isLoggedIn: (state) => !!state.access,
    currentUser: (state) => state.currentUser,
    authError: (state) => state.authError,
    authHeader: (state) => ({ Authorization: `Token ${state.access}` }),
    getUserType: (state) => state.userType,
    getSubject: (state) => state.teacherInfo.subject,
=======
=======
>>>>>>> 0004fc1 (notice merge)
=======
      currentUser: {},
      authError: null,
    };
  },
  getters: {
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
    isLoggedIn: state => !!state.access, 
    currentUser: state => state.currentUser,
    authError: state => state.authError,
    authHeader: state => ({ Authorization: `Bearer ${state.access}` }),
    getUserType: state => state.userType,
<<<<<<< HEAD
<<<<<<< HEAD
    getSubject: state => state.teacherInfo.subject,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> afe56c9 (공지사항 메인페이지)
=======
>>>>>>> 0004fc1 (notice merge)
=======
    getPermission: state => state.hasPermission
>>>>>>> 9c886eb (Feat : 이메일 인증 부분 수정 & 아이디/비밀번호 찾기 기능 완료 & 비밀번호 변경 기능 진행 중)
=======
>>>>>>> d7025b4 (Feat : 비밀번호 변경 페이지 제작 & 컴포넌트화 & 비밀번호 변경 기능 진행 중)
=======
    getSubject: state => state.subjectOptions,
<<<<<<< HEAD
>>>>>>> 194924a (Feat: 생성 기능 구현 중)
=======
    getEmail: state => state.emailOptions,
    isValidEmail: state => state.validEmail,
    getUserInfo: state => state.userInfo,
    getProfil: state => state.profil,
    getInfo: state => state.findPw,
>>>>>>> fa227ef (Feat & Fix : 과제 생성/수정 기능 완료, 나머지 기능 진행 중, 회원 관리 부분 컴포넌트화 및 버그 수정 중)
  },
  mutations: {
<<<<<<< HEAD
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
=======
=======
    getSubject: state => state.teacherInfo.subject,
  },
  mutations: {
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
    SET_TOKEN: (state, access) => (state.access = access),
    SET_CURRENT_USER: (state, user) => (state.currentUser = user),
    SET_AUTH_ERROR: (state, error) => (state.authError = error),
    CHANGE_DATA(state, data) {
      if (state.userType === "student") {
<<<<<<< HEAD
>>>>>>> 36a3f8f (Fix : 오타수정)
        for (let key in data) {
          state.studentInfo[key] = data[key];
        }
      } else {
        for (let key in data) {
          state.teacherInfo[key] = data[key];
        }
      }
    },
<<<<<<< HEAD
<<<<<<< HEAD
    SET_USER_TYPE: (state, userType) => (state.userType = userType),
    CHANGE_INFO: (state, data) => {
      for (let key in data) {
        if (key !== 'profil') {
          state.userInfo[key] = data[key]
        } else {
          state.profil = data[key]
        }
      }
    },
    CHANGE_PW_INFO: (state, data) => {
      for (let key in data) {
        state.findPw[key] = data[key]
      }
    },
    CHANGE_VALID: (state, data) => {
      state.validEmail = data
    }
  },
=======
    SET_PERMISSION: (state, permission) => state.hasPermission = permission,
>>>>>>> 9c886eb (Feat : 이메일 인증 부분 수정 & 아이디/비밀번호 찾기 기능 완료 & 비밀번호 변경 기능 진행 중)
=======
>>>>>>> d7025b4 (Feat : 비밀번호 변경 페이지 제작 & 컴포넌트화 & 비밀번호 변경 기능 진행 중)
  actions: {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e6b54fb (asdu)
    saveToken({commit}, access) {
      commit('SET_TOKEN', access)
      localStorage.setItem('access', access)
=======
    saveToken({ commit }, access) {
      commit("SET_TOKEN", access);
      localStorage.setItem("access", access);
>>>>>>> 36a3f8f (Fix : 오타수정)
    },
    removeToken({ commit }) {
      commit("SET_TOKEN", "");
<<<<<<< HEAD
      localStorage.setItem("access", "");
=======
      localStorage.setItem("access", "")
>>>>>>> d5aaae8 (Feat : 과제 생성/수정/상세 페이지 구현 완료 & 과제 수정/삭제/검색/페이지네이션 기능 구현 중)
=======
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
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
    },
    login({ commit, dispatch }, credentials) {
<<<<<<< HEAD
      axios({
<<<<<<< HEAD
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
=======
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
        url: drf.accounts.login(),
        method: "post",
        data: credentials,
      })
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e6b54fb (asdu)
        .then(res => {
          const access = res.data.access
<<<<<<< HEAD
          dispatch('saveToken', access)
          commit('SET_CURRENT_USER', res.data) 
          router.push({ name: 'educolab'})
        })         
        .catch(err => {
          commit('SET_AUTH_ERROR', err.response.data)
=======
        .then((res) => {
          const access = res.data.access;
          dispatch("saveToken", access);
          commit("SET_CURRENT_USER", res.data);
          router.push({ name: "educolab" });
>>>>>>> 36a3f8f (Fix : 오타수정)
=======
          dispatch("saveToken", access)
<<<<<<< HEAD
          console.log(res.data)
          commit("SET_CURRENT_USER",res.data)
          // 새로고침 -> 로그인 정보 날리기
=======
          // commit("SET_CURRENT_USER", res.data)
>>>>>>> 452a9d1 (설문조사  등록)
          router.push({ name: "educolab" })
>>>>>>> b5069a1 (Feat : 과제 목록 & 생성 & 상세 페이지 제작 진행 중)
        })
        .catch((err) => {
          commit("SET_AUTH_ERROR", err.response.data);
        });
    },
<<<<<<< HEAD
<<<<<<< HEAD
    signup(state) {
      if (state.getters.getUserType == "student") {
        axios
          .post(drf.accounts.signup(), state.state.studentInfo)
          .then(() => {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            console.log(state.teacherInfo)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            confirm('회원가입이 완료되었습니다')
=======
=======
            console.log(state.state.sudentInfo)
>>>>>>> d7d3605 (feat : 비밀번호 변경 기능 구현)
            window.alert('회원가입이 완료되었습니다')
>>>>>>> f57c6b5 ( Fix : get 방식으로 요청)
=======
            window.alert('회원가입이 완료되었습니다')
>>>>>>> e6b54fb (asdu)
            // 자동으로 이동
=======
            window.alert('회원가입이 완료되었습니다')
            router.push({ name: 'login'})
>>>>>>> 0929323 ( Feat : 회원가입 기능 구현)
          })
          .catch(() => {
            console.log(state.state.sudentInfo)
=======
=======
=======
      axios.post(
        drf.accounts.login(),
        credentials,
        { withCredentials: true }
      )
>>>>>>> 73fb905 (fix : 프론트쪽 login 주소 변경)
        .then((res) => {
          const access = res.data.access
          dispatch("saveToken", access)
          commit("SET_CURRENT_USER", res.data.userinfo)
          router.push({ name: "educolab" })
        })
        .catch((err) => {
          commit("SET_AUTH_ERROR", err.response.data)
        });
    },
<<<<<<< HEAD
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
    signup({state, getters}) {
=======
    changeValid({commit}, data) {
      commit("CHANGE_VALID", data)
    },
    signup({state, getters, dispatch}) {
>>>>>>> f86710a (Feat : 비밀번호 변경 구현 완료)
      let data = null
      if (getters.getUserType == "student") {
        data = state.studentInfo
      } else {
        data = state.teacherInfo
      }
      axios.post(drf.accounts.signup(), data)
        .then(() => {
          window.alert("회원가입이 완료되었습니다")
<<<<<<< HEAD
          // 새로고침 -> vuex에 있는 정보 날려버리기 -> 이동
          router.push({ name: "login" })
=======
          router.push({ name: "login" })
          this.initInfo()
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
        })
        .catch(({response}) => {
          if (response.data?.email) {
            window.alert(response.data.email[0])
            dispatch('changeValid', false)
          } else {
<<<<<<< HEAD
>>>>>>> fb19966 (Feat : 비밀번호 변경 기능 완료 & 팝업 컴포넌트화 (수정할 부분 있음))
            window.alert('필수 항목이 빠져 있거나, 올바르지 않습니다')
          })
          
        } else if (state.getters.getUserType == 'teacher') {
<<<<<<< HEAD
          axios.post(drf.accounts.signup(), state.state.teacherInfo)
          .then(() => {
=======
        axios.post(drf.accounts.signup(),state.state.teacherInfo)
          .then(() => {
            console.log(state.state.teacherInfo)
>>>>>>> d7d3605 (feat : 비밀번호 변경 기능 구현)
            window.alert('회원가입이 완료되었습니다')
            router.push({ name: 'login'})
          })
          .catch(() => {
            console.log(state.state.teacherInfo)
            window.alert('필수 항목이 빠져 있거나, 올바르지 않습니다')
          })
=======
    signup({state, getters, dispatch}) {
      let info = null
      if (getters.getUserType == 'student') {
        info = state.studentInfo
      } else {
        info = state.teacherInfo
>>>>>>> 9c886eb (Feat : 이메일 인증 부분 수정 & 아이디/비밀번호 찾기 기능 완료 & 비밀번호 변경 기능 진행 중)
      }
      axios.post(drf.accounts.signup(), info)
      .then(() => {
        window.alert('회원가입이 완료되었습니다')
        router.push({ name: 'login'})
        for (let key in state.studentInfo) {
          if (key === 'userflag') {
            dispatch('changeData', {'userflag':false})
          } else if (key === 'birthday') {
            dispatch('changeData', {'birthday':false})
          } else {
            dispatch('changeData', {key:null})
          }
        }
      })
      .catch(({response}) => {
        if (response.data.email) {
          window.alert(response.data.email[0])
        } else {
          window.alert('필수 항목이 빠져 있거나, 올바르지 않습니다')
        }
      })
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
=======
=======
>>>>>>> c19258a (DB 버그 수정)
=======
>>>>>>> 0004fc1 (notice merge)
=======
>>>>>>> 8dd0805 (깃 충돌  해결)
            window.alert("회원가입이 완료되었습니다");
            router.push({ name: "login" });
          })
          .catch(() => {
            window.alert("필수 항목이 빠져 있거나, 올바르지 않습니다");
          });
      } else if (state.getters.getUserType == "teacher") {
        axios
          .post(drf.accounts.signup(), state.state.teacherInfo)
          .then(() => {
            window.alert("회원가입이 완료되었습니다");
            router.push({ name: "login" });
          })
          .catch(() => {
            window.alert("필수 항목이 빠져 있거나, 올바르지 않습니다");
          });
      }
    },
    logout({ dispatch }) {
      dispatch("removeToken")
      // 새로고침까지 (vuex 데이터 모두 제거하고 싶음)
<<<<<<< HEAD
      router.push({ name: "login" }).catch((err) => {
<<<<<<< HEAD
        console.log(err.respone);
      });
>>>>>>> 36a3f8f (Fix : 오타수정)
=======
        console.log(err.respone)
      })
>>>>>>> 194924a (Feat: 생성 기능 구현 중)
=======
      router.push({ name: "login" })
<<<<<<< HEAD
      router.go(1)
>>>>>>> d6448ce (Feat: back branch merge 전 commit & 생성/수정/삭제 구현 완료 & 제출, 상세, 목록, 검색 기능 구현 중)
=======
>>>>>>> 8f533c8 (Feat : Pagination 기능 구현 완료)
=======
            window.alert('필수 항목이 빠져 있거나, 올바르지 않습니다')
          }
        })
    },
    logout({ dispatch }) {
      dispatch("removeToken");
      router.push({ name: "login" }).catch((err) => {
        console.log(err.respone);
      });
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
    },
    setUserType({ commit }, userType) {
      // 로그인할 때
      // 회원가입 페이지
<<<<<<< HEAD
      commit("SET_USER_TYPE", userType);
    },
<<<<<<< HEAD
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
=======
    changeData({ commit }, data) {
      commit("CHANGE_DATA", data);
>>>>>>> 36a3f8f (Fix : 오타수정)
    },
    changeInfo({commit}, data) {
      commit("CHANGE_INFO", data)
    },
    changePwInfo({commit}, data) {
      commit("CHANGE_PW_INFO", data)
    },
    // back에 현재 사용자 정보 요청 (토큰 보내면 )
=======
      commit("SET_USER_TYPE", userType)
    },
    changeData({ commit }, data) {
      commit("CHANGE_DATA", data)
    },
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
  },
};
