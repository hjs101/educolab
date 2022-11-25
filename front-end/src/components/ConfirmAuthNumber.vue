<template>
  <div class="row justify-center">
    <!-- 인증 버튼 -->
    <q-btn
      v-if="params.userType || params.userData === 'info'"
      class="col-12"
      color="teal"
      :label="params.userType? '이메일 인증':'이메일 변경'"
      @click="isValidEmail"/>
    <q-btn
      v-else
      class="col-4"
      color="white"
      text-color="black"
      label="FIND PW"
      @click="isValidEmail"/>
    <!-- 인증 번호 보냈음을 알림 & 인증 실패 팝업 (일치하는 회원정보가 없음) -->
    <message-pop-up 
      v-if="email.confirm"
      :message="email.message"
      @reverse="email.prompt = false"
    />
    <span class="col-12"></span>
    <!-- 인증 번호 입력 창 -->
    <div v-if="!email.isFail" class="col-4 row justify-between q-mt-lg">
      <q-input
        color="teal"
        class="col-9"
        v-model="number.inputNum"
        lazy-rules
        :rules="[ val => val && val.length > 0 || '인증번호를 입력해주세요']"
      />
      <!-- 인증 번호 확인 버튼 -->
      <q-btn color="teal" class="col-2" label="확인" @click="sendData" />
      <!-- 인증 제한 시간 -->
      <p>
        제한 시간 {{time.minute}}:{{time.second}}
      </p>
      <!-- 인증 번호 일치 여부 팝업-->
      <message-pop-up
        v-if="alert.computedState"
        title="인증 번호 확인"
        message="인증되었습니다"
        :path="params.info?'/change/password':''"
        @reverse="alert.state = false"
      />
    </div>
  </div>
    
</template>

<script>
import {reactive, ref} from '@vue/reactivity'
import {useRoute} from 'vue-router'
import {computed} from 'vue'
import {useStore} from 'vuex'
import axios from 'axios'
import drf from '@/api/drf.js'
import MessagePopUp from '@/components/MessagePopUp.vue'
export default {
  name: 'ConfirmAuthNumber',
  props: {
    data: Object,
  },
  emits: [
    'reverse',
  ],
  components: {
    MessagePopUp,
  },
  setup (props) {
    const route = useRoute()
    const store = useStore()
    const params = reactive({
      userData: route.params.userData || null,
      info: route.params.info || null,
      userType: route.params.userType || null,
    })
    const email = reactive({
      authNum: null,
      valid: false,
      message: null,
      prompt: false,
      isFail: computed(() => !email.valid),
      confirm: computed(() => email.prompt),
    })
    const isValidEmail = () => {
      // if는 find pw, else는 signup, change info
      let url = null
      // find
      if (params.info) {
        if (props.data.email && props.data.name && props.data.username) {
          url = drf.accounts.sendPwEmail()
        } 
      } else if (props.data.email) {
        url = drf.accounts.sendEmail()
      } else {
        email.message = '비어있는 항목을 채워주세요'
        email.prompt =  true
      }
      if (url) {
        axios({
          url,
          method: 'post',
          data: props.data
        })
          .then(res => {
            if ( (params.info && res.data.success) || props.data.email) {
              start()
              email.authNum = res.data['auth_num']
              email.message = "인증번호가 전송되었습니다"
              email.valid = true
            } else {
              email.message = res.data.message
            }
            email.prompt =  true
          })
          .catch(err => console.dir(err))
      }
    }
    const number = reactive({
      inputNum: null,
      showAuth: computed(() => email.valid),
      message: null,
      isValidNumber: computed(() => email.authNum === number.inputNum),
      isAuthNum: computed(() => !!email.authNum),
    }) 
    const alert = reactive({
      state: false,
      computedState: computed(() => alert.state)
      })
    let limit = ref(180)
    const start = () => {
      limit.value = 180
      const timer = setInterval(() => {
        if (limit.value > 0) {
          limit.value -= 1
        } else {
          clearInterval(timer)
          email.authNum = null
        }
      },1000)
    }
    const time = reactive({
      minute: computed(() => Math.floor(limit.value/60)),
      second: computed(() => limit.value%60 >= 10? limit.value%60:'0'+limit.value%60),
    })
    const sendData = () => {
      if (number.isValidNumber) {
        // 비밀번호 찾기
        if (params.info === 'password') {
          alert.state = true
          } else if (params.userData === 'info') {
            store.dispatch('changeInfo', props.data)
          } else {
          store.dispatch('changeData', props.data)
        }
        store.dispatch('changeValid', true)
      }
      alert.state = true
    }
    return {
      params,
      email,
      number,
      alert,
      time,
      isValidEmail,
      sendData
    }
  }
}
</script>