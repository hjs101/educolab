<template>
<<<<<<< HEAD
  <div>
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    <q-input
      color="teal"
      label="아이디"
      v-model="userData.username"
      lazy-rules
      :rules="[ val => val && val.length > 0 || '아이디를 입력해주세요']"
    />
    <q-btn label="중복 확인" color="primary" @click="confirmUsername" />
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 80ba160 ( Feat : 백과의 통신 (학교 검색과 회원가입은 미완료))
=======
>>>>>>> e6b54fb (asdu)
=======
=======
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
    <div class="row justify-between">
=======
    <div class="row justify-between" v-if="!changeMode">
>>>>>>> 086e088 (Feat : 회원정보 수정, 비밀번호 변경 페이지 구현 완료)
=======
  <section>
    <article class="row justify-between" v-if="!changeMode">
>>>>>>> f86710a (Feat : 비밀번호 변경 구현 완료)
      <q-input
        color="teal"
        label="아이디"
        v-model="userData.username"
        lazy-rules
        class="col-8 alp"
        maxlength="20"
        :rules="[ val => val && val.length > 0 || '아이디를 입력해주세요',
        val => val && val.length > 4 ||'아이디는 최소 5자리 이상이어야 합니다'
        ]"
      />
      <q-btn label="중복 확인" color="teal" @click="confirmUsername" class="text-size" />
      <message-pop-up
        v-if="computedData.confirm"
        :message="computedData.message"
        @reverse="userData.confirm = false"
      />
<<<<<<< HEAD
    </div>
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> bf45305 ( Fix : 버그 수정)
=======
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)

    <q-dialog v-model="userData.confirm" class="dialog">
      <q-card>
        <q-card-section>
          <b>
            {{computedData.message}}
          </b>
          <br>
          <q-btn
          v-close-popup
          label="확인"
          color="primary"
          class="submitButton"
          @click="userData.confirm = false"
          />
        </q-card-section>
      </q-card>
    </q-dialog>
<<<<<<< HEAD
<<<<<<< HEAD
    
    <p v-if="userData.password2 && computedData.validUsername !== 2">
      <span v-if="computedData.validUsername">
        {{computedData.message}}
      </span>
<<<<<<< HEAD
=======
    <p v-if="userData.password2 && computedData.validUsername !== 2">
<<<<<<< HEAD
      <span v-show="computedData.validUsername">사용가능한 아이디입니다</span>
<<<<<<< HEAD
      <span v-show="!computedData.validUsername">이미 존재하는 아이디입니다/다른 아이디 값을 입력해주세요</span>
>>>>>>> 147871f (Feat : 회원가입 틀 제작 후 이름까지 완료 (그 이후 부분은 미완성))
=======
      <span v-show="!computedData.validUsername">이미 존재하는 아이디입니다. 다른 아이디 값을 입력해주세요</span>
>>>>>>> acd4b8a ( Feat : 아이디 중복 확인, 학교 검색, 이메일 인증 백과 통신 기능 추가)
=======
      <span v-if="computedData.validUsername">
        {{computedData.message}}
      </span>
>>>>>>> bb316aa ( Feat : 회원가입 시 입력받은 정보를 취합하는 중)
=======
>>>>>>> e6b54fb (asdu)
    </p>
=======
>>>>>>> bf45305 ( Fix : 버그 수정)
=======
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
=======
>>>>>>> 086e088 (Feat : 회원정보 수정, 비밀번호 변경 페이지 구현 완료)
=======
    </article>
>>>>>>> f86710a (Feat : 비밀번호 변경 구현 완료)
    <q-input
      color="teal"
      label="비밀번호"
      type="password"
      class="col-8 han"
      v-model="userData.password1"
      maxlength="20"
      lazy-rules
      :rules="[
        val => val !== null && val !== '' || '비밀번호를 입력해주세요',
        val => val.length > 5 ||'비밀번호는 최소 6자리 이상이어야 합니다'
      ]"
    />
    <q-input
      color="teal"
      label="비밀번호 확인"
      type="password"
      style="ime-mode:disabled"
      v-model="userData.password2"
      @keyup="isCorrect"
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
      @change="$emit(toSignup)"
>>>>>>> 147871f (Feat : 회원가입 틀 제작 후 이름까지 완료 (그 이후 부분은 미완성))
=======
>>>>>>> 2091835 (Feat: merge 전 수정 사항 반영)
=======
>>>>>>> e6b54fb (asdu)
=======
=======
      class="col-8"
>>>>>>> db26c2a (Style & Fix : 스타일 및 오류 수정)
=======
      class="col-8 han"
>>>>>>> ed2b7a7 (Fix : 교사 과제 검색 기능 오류 해결)
      minlength="5"
      maxlength="20"
>>>>>>> bf45305 ( Fix : 버그 수정)
=======
      minlength="5"
      maxlength="20"
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
      lazy-rules
      :rules="[
        val => val !== null && val !== '' || '비밀번호를 다시 입력해주세요',
      ]"
    />
    <!-- 비밀번호 일치 여부 확인 -->
    <p v-if="userData.password2">
      <span v-show="computedData.samePassword">비밀번호가 일치합니다</span>
      <span v-show="!computedData.samePassword" class="red">비밀번호가 일치하지 않습니다</span>
    </p>
    <article v-if="changeMode">
      <q-btn label="비밀번호 변경" color="amber" @click="changePw" class="col-8 text-size"/>
      <message-pop-up
        v-if="password.popUpFlag"
        :message="password.message"
        @reverse="toLogin"
      />
      <message-pop-up
        v-if="password.ErrorpopUp"
        :message="password.message"
        @reverse="password.error = false"
      />
    </article>
  </section>
</template>

<style scoped>
  .alp {
    -webkit-ime-mode:disabled;
    -moz-ime-mode:disabled;
    -ms-ime-mode:disabled;
    ime-mode:disabled;
  }
  .han {
    -webkit-ime-mode:active;
    -moz-ime-mode:active;
    -ms-ime-mode:active;
    ime-mode:active;
  }
</style>

<script>
import {reactive} from '@vue/reactivity'
import {computed} from 'vue'
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
import axios from 'axios'
import drf from '@/api/drf.js'
import {useStore} from 'vuex'
<<<<<<< HEAD
=======
import {accounts} from '@/api/drf.js'
// import axios from 'axios';
>>>>>>> acd4b8a ( Feat : 아이디 중복 확인, 학교 검색, 이메일 인증 백과 통신 기능 추가)
=======
import axios from 'axios'
import drf from '@/api/drf.js'
<<<<<<< HEAD
import {useStore} from 'store'
>>>>>>> bb316aa ( Feat : 회원가입 시 입력받은 정보를 취합하는 중)
=======
import {useStore} from 'vuex'
>>>>>>> 89ccfeb ( Feat: 회원 가입 기능 완료 (백 통신해서 디버깅 해야 함))
=======
import axios from 'axios'
import drf from '@/api/drf.js'
import {useStore} from 'vuex'
>>>>>>> e6b54fb (asdu)
=======
import axios from 'axios'
import drf from '@/api/drf.js'
import {useStore} from 'vuex'
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
=======
import MessagePopUp from './MessagePopUp.vue'
>>>>>>> 086e088 (Feat : 회원정보 수정, 비밀번호 변경 페이지 구현 완료)
export default {
  name: 'LoginInfo',
  props: {
    changeMode: Boolean,
  },
  components: {
    MessagePopUp
  },
  setup (props) {
    const store = useStore()
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
// import axios from 'axios';
export default {
  name: 'LoginInfo',
<<<<<<< HEAD
  setup (props, {emit}) {
>>>>>>> 147871f (Feat : 회원가입 틀 제작 후 이름까지 완료 (그 이후 부분은 미완성))
=======
  setup () {
>>>>>>> 2091835 (Feat: merge 전 수정 사항 반영)
=======
>>>>>>> bb316aa ( Feat : 회원가입 시 입력받은 정보를 취합하는 중)
=======
>>>>>>> e6b54fb (asdu)
=======
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
    const userData = reactive({
      username: null,
      password1: null,
      password2: null,
      correct: null,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e6b54fb (asdu)
=======
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
      confirm: null,
      valid: null,
    })
    const computedData = reactive({
      samePassword: computed(() => userData.correct),
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 80ba160 ( Feat : 백과의 통신 (학교 검색과 회원가입은 미완료))
=======
>>>>>>> e6b54fb (asdu)
      validUsername: computed(() => userData.confirm),
=======
      validUsername: computed(() => userData.valid),
<<<<<<< HEAD
>>>>>>> bf45305 ( Fix : 버그 수정)
=======
      validUsername: computed(() => userData.valid),
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
=======
      confirm: computed(() => userData.confirm),
>>>>>>> 086e088 (Feat : 회원정보 수정, 비밀번호 변경 페이지 구현 완료)
      message: computed(() => computedData.validUsername? '사용 가능한 아이디입니다':'중복된 아이디입니다. 다른 아이디를 입력해주세요')
    })
    const password = reactive({
      message: null,
      success: false,
      prompt: false,
      error: false,
      popUpFlag:computed(() => password?.prompt),
      ErrorpopUp:computed(() => password?.error),
      samePassword: computed(() => password.one === password.two)
    })
    const confirmUsername = () => {
      // 아이디 중복 여부 확인
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
      axios.get(drf.accounts.checkUsername(), {username: userData.username})
        .then((res) => {
          userData.confirm = res.data.dup === 'success'
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e6b54fb (asdu)
          if (computedData.validUsername) {
            store.dispatch('changeData', {username: userData.username})
          }
        })
<<<<<<< HEAD
=======
      confirm: 2,
=======
      confirm: null,
>>>>>>> acd4b8a ( Feat : 아이디 중복 확인, 학교 검색, 이메일 인증 백과 통신 기능 추가)
    })
    const computedData = reactive({
      samePassword: computed(() => userData.correct),
      validUsername: computed(() => userData.confirm == 'success')
    })
    const confirmUsername = () => {
      // 아이디 일치 여부 확인
<<<<<<< HEAD
      // const data = {username: userData.username}
    
    //   axios.get('', data)
    //     .then((res) => {
    //       // 변수명 알아내야 함
    //       confirm = res.data
      console.log(userData.username)
>>>>>>> 147871f (Feat : 회원가입 틀 제작 후 이름까지 완료 (그 이후 부분은 미완성))
=======
      axios.get(accounts.checkUsername(), {username: userData.username})
=======
      validUsername: computed(() => userData.confirm === 'success'),
      message: computed(() => computedData.validUsername? '사용 가능한 아이디입니다':'중복된 아이디입니다. 다른 아이디를 입력해주세요')
    })
    const confirmUsername = () => {
      // 아이디 중복 여부 확인
      axios.get(drf.accounts.checkUsername(), {username: userData.username})
>>>>>>> bb316aa ( Feat : 회원가입 시 입력받은 정보를 취합하는 중)
        .then((res) => {
          userData.confirm = res.data.dup
=======
>>>>>>> 80ba160 ( Feat : 백과의 통신 (학교 검색과 회원가입은 미완료))
          if (computedData.validUsername) {
            store.dispatch('changeData', {username: userData.username})
          }
        })
>>>>>>> acd4b8a ( Feat : 아이디 중복 확인, 학교 검색, 이메일 인증 백과 통신 기능 추가)
=======
>>>>>>> e6b54fb (asdu)
=======
      if (userData.username.length > 5) {
        axios.get(drf.accounts.checkUsername(), {username: userData.username})
=======
      if (userData.username.length > 4) {
=======
      if (userData.username && userData.username.length > 4) {
>>>>>>> dab616b ( Style : 회원가입 스타일 수정)
        axios.get(drf.accounts.checkUsername(), {params : {username: userData.username}})
>>>>>>> 0929323 ( Feat : 회원가입 기능 구현)
=======
      if (userData.username && userData.username.length > 4) {
<<<<<<< HEAD
        axios.get(drf.accounts.checkUsername(), {params : {username: userData.username}})
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
=======
        axios({
          url: drf.accounts.checkUsername(),
          method: 'get',
          params : {username: userData.username}
        })
>>>>>>> f86710a (Feat : 비밀번호 변경 구현 완료)
          .then((res) => {
            userData.confirm = true
            userData.valid = res.data.dup === 'success'
            if (computedData.validUsername) {
              store.dispatch('changeData', {username: userData.username})
            }
          })
      }
<<<<<<< HEAD
>>>>>>> bf45305 ( Fix : 버그 수정)
=======
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
    }
    const isCorrect = () => {
      if (userData.password1 === userData.password2) {
        userData.correct = true
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        store.dispatch('changeData', {password1: userData.password1, password2: userData.password2})
=======
>>>>>>> 147871f (Feat : 회원가입 틀 제작 후 이름까지 완료 (그 이후 부분은 미완성))
=======
        store.dispatch('changeData', {password1: userData.password1, password2: userData.password2})
>>>>>>> 89ccfeb ( Feat: 회원 가입 기능 완료 (백 통신해서 디버깅 해야 함))
=======
        store.dispatch('changeData', {password1: userData.password1, password2: userData.password2})
>>>>>>> e6b54fb (asdu)
=======
        if (userData.password1 > 5) {
=======
        if (userData.password1.length > 5) {
>>>>>>> 0929323 ( Feat : 회원가입 기능 구현)
          store.dispatch('changeData', {password1: userData.password1, password2: userData.password2})
        }
>>>>>>> bf45305 ( Fix : 버그 수정)
=======
        if (userData.password1.length > 5) {
          if (!props?.changeMode) {
            store.dispatch('changeData', {password1: userData.password1, password2: userData.password2})
          }
        }
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
      } else {
        userData.correct = false
      }
    }
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
    const toSignup = () => {
      emit('to-signup', userData)
    }
>>>>>>> 147871f (Feat : 회원가입 틀 제작 후 이름까지 완료 (그 이후 부분은 미완성))
=======
>>>>>>> 2091835 (Feat: merge 전 수정 사항 반영)
=======
    const 
>>>>>>> bb316aa ( Feat : 회원가입 시 입력받은 정보를 취합하는 중)
=======
>>>>>>> 89ccfeb ( Feat: 회원 가입 기능 완료 (백 통신해서 디버깅 해야 함))
=======
>>>>>>> e6b54fb (asdu)
=======
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
=======
=======
    const toLogin = () => {
      password.prompt = false
      store.dispatch('logout')
    }
>>>>>>> 110d2da (Fix : 비밀번호 변경 시 팝업 경로 수정 및 경우에 따른 팝업 메시지 수정)
    const changePw = () => {
      if (userData.password1 !== null && userData.password1 !== '') {
        if (userData.password1.includes(' ')) {
          password.message = '비밀번호에 공백을 포함할 수 없습니다'
          password.error = true
        } else if (!password.samePassword) {
          password.message = '비밀번호가 일치하지 않습니다'
          password.error = true
        } else if (userData.password1.length < 6) {
          password.message = '비밀번호를 6자리 이상 입력해주세요'
          password.error = true
        } else {
          axios({
            url: drf.accounts.changePw(),
            method: 'post',
            data: {
              ...store.getters.getInfo,
              password1: userData.password1,
              password2: userData.password2
              }
          })
          .then(({data}) => {
            console.log(data)
            password.message = data.message
            if (data.success) {
              password.prompt = true
            } else {
              password.error = true
            }
          })
          .catch(({response}) => {
            password.message = response.data.message
            password.error = true
          })
        }
      } else {
        password.message = '비밀번호를 입력해주세요'
        password.error = true
      }
    }
>>>>>>> f86710a (Feat : 비밀번호 변경 구현 완료)
    return {
      userData,
      computedData,
      confirmUsername,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
      isCorrect
=======
      isCorrect,
      password,
      changePw,
<<<<<<< HEAD
>>>>>>> f86710a (Feat : 비밀번호 변경 구현 완료)
=======
      toLogin
>>>>>>> 110d2da (Fix : 비밀번호 변경 시 팝업 경로 수정 및 경우에 따른 팝업 메시지 수정)
    }
  }
<<<<<<< HEAD
=======
      isCorrect,
      toSignup
=======
      isCorrect
>>>>>>> 2091835 (Feat: merge 전 수정 사항 반영)
    }
  },
>>>>>>> 147871f (Feat : 회원가입 틀 제작 후 이름까지 완료 (그 이후 부분은 미완성))
=======
>>>>>>> acd4b8a ( Feat : 아이디 중복 확인, 학교 검색, 이메일 인증 백과 통신 기능 추가)
=======
      isCorrect
    }
  }
>>>>>>> e6b54fb (asdu)
=======
      isCorrect
    }
  }
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
}
</script>

<style scoped>
  .text-size {
    font-size: 1rem;
  }
</style>