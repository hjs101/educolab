<template>
  <div>
    <!-- 인증 버튼 -->
    <q-btn
      v-if="params.userType"
      color="teal"
      label="이메일 인증"
      class="col-2"
      @click="isValidEmail"/>
    <q-btn
      v-else
      color="white"
      text-color="black"
      label="FIND PW"
      class="col-8 offset-2 col-md-1 offset-md-1"
      @click="isValidEmail"/>
    <!-- 인증 번호를 보냈음을 알림 또는 빈 항목이 있음을 알림 (프론트) -->
    <message-pop-up
      v-if="email.prompt && !email.isFail"
      title=""
      message="인증번호가 전송되었습니다"
      path=""
      success=""
    />
    <!-- 인증 실패 팝업 (일치하는 회원정보가 없음) -->
    <message-pop-up 
      v-if="email.prompt && email.isFail"
      title="인증 실패"
      :message="email.message"
      path=""
      success=""
    />
    <!-- 인증 번호 입력 창 -->
    <div v-if="email.prompt && !email.isFail" class="row justify-between">
      <q-input
        color="teal"
        v-model="number.inputNum"
        class="col-9"
        lazy-rules
        :rules="[ val => val && val.length > 0 || '인증번호를 입력해주세요']"
      />
      <!-- 인증 번호 확인 버튼 -->
      <q-btn color="teal" label="확인" class="col-2" @click="sendData" />
      <!-- 인증 제한 시간 -->
      <p>
        제한 시간 {{time.minute}}:{{time.second}}
      </p>
      <!-- 인증 번호 일치 여부 팝업-->
      <message-pop-up
        v-if="alert"
        title="인증 번호 확인"
        message="인증되었습니다"
        path=""
        :success="email.valid"
      />
    </div>
  </div>
    
</template>

<script>
import {reactive, ref} from '@vue/reactivity'
import {useRoute, useRouter} from 'vue-router'
import {computed, onBeforeMount} from 'vue'
import {useStore} from 'vuex'
import axios from 'axios'
import drf from '@/api/drf.js'
import MessagePopUp from '@/components/MessagePopUp.vue'
export default {
  name: 'ConfirmAuthNumber',
  props: {
    data: Object,
  },
  components: {
    MessagePopUp,
  },
  setup (props) {
    const route = useRoute()
    const router = useRouter()
    const store = useStore()
    const params = reactive({
      info: route.params.info? route.params.info : null,
      userType: route.params.userType? route.params.userType : null,
    })
    const email = reactive({
      authNum: null,
      valid: false,
      message: null,
      prompt: false,
      isFail: computed(() => !!email.message)
    })
    const isValidEmail = () => {
      // if는 find, else는 signup
      if (params.info) {
        if (props.data.email && props.data.name && props.data.username) {
          axios.post(drf.accounts.sendPwEmail(), props.data)
            .then(res => {
              if (res.data.success) {
                email.authNum = res.data['auth_num']
                email.valid = true
                start()
              } else {
                email.message = res.data.message
              }
            })
        } else {
          email.message = '비어있는 항목을 채워주세요'
          // 빈 항목이 있을 때
        }
        email.prompt = true
      } else {
          if (props.data.email) {
            start()
            axios.post(drf.accounts.sendEmail(), props.data)
              .then(res => {
                email.authNum = res.data['auth_num']
                email.valid = true
              })
          } else {
            email.message = '비어있는 항목을 채워주세요'
          }
          email.prompt = true
      }
    }
    const number = reactive({
      inputNum: null,
      showAuth: computed(() => email.valid),
      message: null,
      isValidNumber: computed(() => email.authNum === number.inputNum),
      isAuthNum: computed(() => !!email.authNum),
    }) 
    let alert = ref(false)
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
        if (route.params.info === 'password') {
          alert = true
          email.valid = false
          router.push('/change/password')
          } else {
            store.dispatch('changeData', props.data)
        }
      }
      alert = true
    }
    onBeforeMount (() => {
      if (!params.userType && params.info !== 'password') {
        router.push('/404')
      }
    })
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