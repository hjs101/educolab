<template>
  <div>
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    <q-input v-model="email.username" :suffix="email.address !== '직접 입력'? email.address: ''" input-class="text-right" label-slot clearable stack-label>
=======
    <q-input v-model="email" :suffix="emailAddress" input-class="text-right" label-slot clearable stack-label>
>>>>>>> 147871f (Feat : 회원가입 틀 제작 후 이름까지 완료 (그 이후 부분은 미완성))
=======
    <q-input v-model="email.username" :suffix="email.address !== '직접 입력'? email.address: ''" input-class="text-right" label-slot clearable stack-label>
>>>>>>> 03de9fd (Feat: 회원가입 학교 검색, 이름, 전화번호, 생년월일, 학년/반/번호)
=======
    <q-input v-model="email.username" :suffix="email.address !== '직접 입력'? email.address: ''" input-class="text-right" label-slot clearable stack-label>
>>>>>>> e6b54fb (asdu)
      <template v-slot:label>
        <div class="row items-center all-pointer-events">
          Email
          <q-tooltip class="bg-grey-8" anchor="top left" self="bottom left" :offset="[0, 8]">Email address</q-tooltip>
        </div>
      </template>
    </q-input>
    <!-- 이메일 주소 선택 -->
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e6b54fb (asdu)
    <q-select v-model="email.address" :options="emailOptions" label="이메일 주소 선택" />
    <!-- 인증 버튼 -->
    <q-btn color="primary" label="이메일 인증" class="buttonGroup" @click="isValidEmail"/>
    <!-- 인증 번호 입력 창 -->
    <div v-if="email.showAuth">
      <q-input
        color="teal"
        v-model="number.inputNum"
        lazy-rules
        :rules="[ val => val && val.length > 0 || '인증번호를 입력해주세요']"
      />
      <!-- 인증 번호 확인 버튼 -->
      <q-btn color="primary" label="인증" class="buttonGroup" @click="alert = true"/>
      <!-- 인증 제한 시간 -->
      <p>
        제한 시간 {{time.minute}}:{{time.second}}
      </p>
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e6b54fb (asdu)
      <!-- 인증 번호 일치 여부 팝업-->
      <q-dialog v-model="alert">
        <q-card>
          <q-card-section>
            <div class="text-h6">인증 번호 확인</div>
          </q-card-section>

          <q-card-section class="q-pt-none">
            <span v-if="number.isAuthNum && number.isValidNumber">
              인증되었습니다
            </span>
            <span v-else>
              인증번호가 일치하지 않습니다
            </span>
          </q-card-section>

          <q-card-actions align="right">
            <q-btn flat label="확인" color="primary" v-close-popup @click="sendData({email:email.fullEmail})"/>
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e6b54fb (asdu)
          </q-card-actions>
        </q-card>
      </q-dialog>
    </div>
<<<<<<< HEAD
=======
    <q-select v-model="emailAddress" :options="emailOptions" label="이메일 주소 선택" />
=======
    <q-select v-model="email.address" :options="emailOptions" label="이메일 주소 선택" />
>>>>>>> 03de9fd (Feat: 회원가입 학교 검색, 이름, 전화번호, 생년월일, 학년/반/번호)
    <!-- 인증 버튼 -->
    <q-btn color="primary" label="이메일 인증" class="buttonGroup" @click="isValidEmail"/>
    <!-- 인증 번호 입력 창 -->
    <div v-if="email.showAuth">
      <q-input
        color="teal"
        v-model="number.inputNum"
        lazy-rules
        :rules="[ val => val && val.length > 0 || '인증번호를 입력해주세요']"
      />
      <!-- 인증 번호 확인 버튼 -->
      <q-btn color="primary" label="인증" class="buttonGroup" @click="alert = true"/>
=======
>>>>>>> 8e42007 ( Feat : 이메일 인증 제한 시간 추가)
      <!-- 인증 번호 일치 여부 팝업-->
      <q-dialog v-model="alert">
        <q-card>
          <q-card-section>
            <div class="text-h6">인증 번호 확인</div>
          </q-card-section>

<<<<<<< HEAD
>>>>>>> 147871f (Feat : 회원가입 틀 제작 후 이름까지 완료 (그 이후 부분은 미완성))
=======
          <q-card-section class="q-pt-none">
            <span v-if="number.isAuthNum && number.isValidNumber">
              인증되었습니다
            </span>
            <span v-else>
              인증번호가 일치하지 않습니다
            </span>
          </q-card-section>

          <q-card-actions align="right">
            <q-btn flat label="OK" color="primary" v-close-popup />
=======
>>>>>>> 80ba160 ( Feat : 백과의 통신 (학교 검색과 회원가입은 미완료))
          </q-card-actions>
        </q-card>
      </q-dialog>
    </div>
>>>>>>> 03de9fd (Feat: 회원가입 학교 검색, 이름, 전화번호, 생년월일, 학년/반/번호)
=======
>>>>>>> e6b54fb (asdu)
  </div>
</template>

<script>
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e6b54fb (asdu)
import {reactive, ref} from '@vue/reactivity'
import {computed} from 'vue'
import {useStore} from 'vuex'
import axios from 'axios'
import drf from '@/api/drf.js'
export default {
  name: 'EmailConfirm',
  setup () {
    const store = useStore()
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e6b54fb (asdu)
    const emailOptions = [
      '@gmail.com', '@naver.com', '@hanmail.com', '@nate.com', '직접 입력'
    ]
    const number = reactive({
      authNum: null,
      inputNum: null,
      isValidNumber: computed(() => number.authNum === number.inputNum),
      isAuthNum: computed(() => !!number.authNum)
    }) 
    const email = reactive({
      address: '',
      username: '',
      valid: false,
      showAuth: computed(() => email.valid),
      fullEmail: computed(() => email.address !== '직접 입력'? email.username+email.address: email.username),
    })
    let alert = ref(false)
    let limit = ref(180)
    const start = () => {
      limit.value = 180
      const timer = setInterval(() => {
        if (limit.value > 0) {
          limit.value -= 1
        } else {
          number.authNum = null
          clearInterval(timer)
        }
      },1000)
    }
    const isValidEmail = () => {
      axios.post(drf.accounts.sendEmail(), {email:email.fullEmail})
        .then(res => {
          number.authNum = res.data['auth_num']
        })
<<<<<<< HEAD
<<<<<<< HEAD
      email.valid = true
      start()
    }
    const time = reactive({
      minute: computed(() => Math.floor(limit.value/60)),
      second: computed(() => limit.value%60 >= 10? limit.value%60:'0'+limit.value%60),
    })
    const sendData = (data) => {
      if (number.isValidNumber) {
        store.dispatch('changeData', data)
=======
import {ref} from '@vue/reactivity'
=======
import {reactive, ref} from '@vue/reactivity'
import {computed} from 'vue'
<<<<<<< HEAD
// import axios from 'axios'
>>>>>>> 03de9fd (Feat: 회원가입 학교 검색, 이름, 전화번호, 생년월일, 학년/반/번호)
=======
import axios from 'axios'
<<<<<<< HEAD
import {accounts} from '@/api/drf.js'
>>>>>>> acd4b8a ( Feat : 아이디 중복 확인, 학교 검색, 이메일 인증 백과 통신 기능 추가)
=======
import drf from '@/api/drf.js'
>>>>>>> bb316aa ( Feat : 회원가입 시 입력받은 정보를 취합하는 중)
export default {
  name: 'EmailConfirm',
  setup () {
=======
>>>>>>> 89ccfeb ( Feat: 회원 가입 기능 완료 (백 통신해서 디버깅 해야 함))
    const emailOptions = [
      '@gmail.com', '@naver.com', '@hanmail.com', '@nate.com', '직접 입력'
    ]
    const number = reactive({
      authNum: null,
      inputNum: null,
      isValidNumber: computed(() => number.authNum === number.inputNum),
      isAuthNum: computed(() => !!number.authNum)
    }) 
    const email = reactive({
      address: '',
      username: '',
      valid: false,
      showAuth: computed(() => email.valid),
      fullEmail: computed(() => email.address !== '직접 입력'? email.username+email.address: email.username),
    })
    let alert = ref(false)
    let limit = ref(180)
    const start = () => {
      limit.value = 180
      const timer = setInterval(() => {
        if (limit.value > 0) {
          limit.value -= 1
        } else {
          number.authNum = null
          clearInterval(timer)
        }
      },1000)
    }
    const isValidEmail = () => {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
      // 백에 신호 보내 인증 번호 받기 -> realNumber 바꿔주기
    }
    const isValidNumber = () => {
      // 인증 번호 확인
      if (realNumber === inputNumber) {
        return true
      } else {
        return false
>>>>>>> 147871f (Feat : 회원가입 틀 제작 후 이름까지 완료 (그 이후 부분은 미완성))
      }
    }
    return {
      emailOptions,
<<<<<<< HEAD
      number,
      email,
      alert,
      isValidEmail,
      time,
      start,
      sendData
=======
      emailAddress,
      isValidEmail,
      isValidNumber,
      realNumber,
      inputNumber
>>>>>>> 147871f (Feat : 회원가입 틀 제작 후 이름까지 완료 (그 이후 부분은 미완성))
=======
      // axios.post('', fullEmail)
      //   .then(res => realNumber = res.data.)
      //   .catch(err => confirm('이메일이 유효하지 않습니다'))
=======
      axios.post(accounts.sendEmail(), fullEmail)
        .then(res => realNumber = res.data[auth_num])
>>>>>>> acd4b8a ( Feat : 아이디 중복 확인, 학교 검색, 이메일 인증 백과 통신 기능 추가)
=======
      axios.post(drf.accounts.sendEmail(), email.fullEmail)
        .then(res => number.authNumber = res.data['auth_num'])
>>>>>>> bb316aa ( Feat : 회원가입 시 입력받은 정보를 취합하는 중)
=======
>>>>>>> 80ba160 ( Feat : 백과의 통신 (학교 검색과 회원가입은 미완료))
=======
>>>>>>> e6b54fb (asdu)
      email.valid = true
      start()
    }
    const time = reactive({
      minute: computed(() => Math.floor(limit.value/60)),
      second: computed(() => limit.value%60 >= 10? limit.value%60:'0'+limit.value%60),
    })
    const sendData = (data) => {
      if (number.isValidNumber) {
        store.dispatch('changeData', data)
      }
    }
    return {
      emailOptions,
      number,
      email,
      alert,
      isValidEmail,
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 03de9fd (Feat: 회원가입 학교 검색, 이름, 전화번호, 생년월일, 학년/반/번호)
=======
      time,
      start,
<<<<<<< HEAD
>>>>>>> 8e42007 ( Feat : 이메일 인증 제한 시간 추가)
=======
      sendData
>>>>>>> 89ccfeb ( Feat: 회원 가입 기능 완료 (백 통신해서 디버깅 해야 함))
=======
      time,
      start,
      sendData
>>>>>>> e6b54fb (asdu)
    }
  }
}
</script>