<template>
  <div>
    <q-input v-model="email.username" :suffix="email.address !== '직접 입력'? email.address: ''" input-class="text-right" label-slot clearable stack-label>
      <template v-slot:label>
        <div class="row items-center all-pointer-events">
          Email
          <q-tooltip class="bg-grey-8" anchor="top left" self="bottom left" :offset="[0, 8]">Email address</q-tooltip>
        </div>
      </template>
    </q-input>
    <!-- 이메일 주소 선택 -->
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
      <!-- 인증 번호 일치 여부 팝업-->
      <q-dialog v-model="alert">
        <q-card>
          <q-card-section>
            <div class="text-h6">인증 번호 확인</div>
          </q-card-section>

          <q-card-section class="q-pt-none">
            <span v-if="number.isValidNumber">
              인증번호가 일치합니다
            </span>
            <span v-else>
              인증번호가 일치하지 않습니다
            </span>
          </q-card-section>

          <q-card-actions align="right">
            <q-btn flat label="OK" color="primary" v-close-popup />
          </q-card-actions>
        </q-card>
      </q-dialog>
    </div>
  </div>
</template>

<script>
import {reactive, ref} from '@vue/reactivity'
import {computed} from 'vue'
// import axios from 'axios'
export default {
  name: 'EmailConfirm',
  setup () {
    const emailOptions = [
      '@gmail.com', '@naver.com', '@hanmail.com', '@nate.com', '직접 입력'
    ]
    const number = reactive({
      authNum: null,
      inputNum: null,
      isValidNumber: computed(() => number.authNum === number.inputNum)
    }) 
    const email = reactive({
      address: '',
      username: '',
      valid: false,
      showAuth: computed(() => email.valid),
    })
    let fullEmail = email.address !== '직접 입력'? email.username+email.address: email.username
    let alert = ref(false)
    const isValidEmail = () => {
      // axios.post('', fullEmail)
      //   .then(res => realNumber = res.data.)
      //   .catch(err => confirm('이메일이 유효하지 않습니다'))
      email.valid = true
    }
    return {
      emailOptions,
      number,
      email,
      fullEmail,
      alert,
      isValidEmail,
    }
  }
}
</script>