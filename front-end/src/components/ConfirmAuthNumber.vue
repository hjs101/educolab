<template>
  <div>
    <!-- 인증 버튼 -->
    <q-btn v-if="params.userType" color="teal" label="이메일 인증" class="col-2" @click="isValidEmail"/>
    <q-btn v-else color="white" text-color="black" label="FIND PW" class="col-8 offset-2 col-md-1 offset-md-1" @click="isValidEmail"/>
    <!-- 비밀번호 찾기 (인증 실패 팝업) -->
    <q-dialog v-model="email.isFail">
        <q-card>
          <q-card-section>
            <div class="text-h6">인증 실패</div>
          </q-card-section>

          <q-card-section class="q-pt-none">
            <span>
              {{email.message}}
            </span>
          </q-card-section>

          <q-card-actions align="center">
            <q-btn flat label="확인" color="primary" v-close-popup/>
          </q-card-actions>
        </q-card>
      </q-dialog>
    <!-- 인증 번호 입력 창 -->
    <div v-if="number.showAuth" class="row justify-between">
      <q-input
        color="teal"
        v-model="number.inputNum"
        class="col-9"
        lazy-rules
        :rules="[ val => val && val.length > 0 || '인증번호를 입력해주세요']"
      />
      <!-- 인증 번호 확인 버튼 -->
      <q-btn color="teal" label="확인" class="col-2" @click="alert = true" />
      <!-- 인증 제한 시간 -->
      <p>
        제한 시간 {{time.minute}}:{{time.second}}
      </p>
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
            <span v-else-if="!number.isAuthNum">
              인증번호 입력 시간이 지났습니다. 이메일 인증을 다시 받아주세요
            </span>
            <span v-else>
              인증번호가 일치하지 않습니다
            </span>
          </q-card-section>

          <q-card-actions align="right">
            <q-btn flat label="확인" color="primary" v-close-popup @click="sendData"/>
          </q-card-actions>
        </q-card>
      </q-dialog>
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
export default {
  name: 'ConfirmAuthNumber',
  props: {
    data: Object,
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
      isFail: computed(() => !!email.message)
    })
    const isValidEmail = () => {
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
        }
      } else {
        if (props.data.email) {
          axios.post(drf.accounts.sendEmail(), props.data)
            .then(res => {
              console.log
              email.authNum = res.data['auth_num']
              email.valid = true
              start()
            })
        }
      }
    }
    const number = reactive({
      inputNum: null,
      showAuth: computed(() => email.valid),
      isValidNumber: computed(() => email.authNum === number.inputNum),
      isAuthNum: computed(() => !!email.authNum),
    }) 
    let alert = ref(false)
    let limit = ref(180)
    const start = () => {
      console.log(1)
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
          store.dispatch('setPermission', true)
          router.push('/change/password')
          } else {
          store.dispatch('changeData', {email:props.email})
        }
      }
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
      sendData,
    }
  }
}
</script>