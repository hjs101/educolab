<template>
  <div>
    <q-input v-model="email" :suffix="emailAddress" input-class="text-right" label-slot clearable stack-label>
      <template v-slot:label>
        <div class="row items-center all-pointer-events">
          Email
          <q-tooltip class="bg-grey-8" anchor="top left" self="bottom left" :offset="[0, 8]">Email address</q-tooltip>
        </div>
      </template>
    </q-input>
    <!-- 이메일 주소 선택 -->
    <q-select v-model="emailAddress" :options="emailOptions" label="이메일 주소 선택" />
    <!-- 인증 버튼 -->
    <q-btn color="primary" label="이메일 인증" class="buttonGroup" @click="isValidEmail"/>
    <!-- 인증 번호 입력 창 -->
    <q-input
      color="teal"
      v-model="authNumber"
      lazy-rules
      :rules="[ val => val && val.length > 0 || '인증번호를 입력해주세요']"
    />
    <!-- 인증 번호 확인 버튼 -->
    <q-btn color="primary" label="인증" class="buttonGroup" @click="isValidNumber"/>
    <!-- 인증 번호 일치 여부 -->

  </div>
</template>

<script>
import {ref} from '@vue/reactivity'
export default {
  name: 'EmailConfirm',
  setup () {
    const emailOptions = [
      '@gmail.com', '@naver.com', '@hanmail.com', '@nate.com'
    ]
    let realNumber = ref(0)
    let inputNumber = ref(0)
    let emailAddress = ref('')
    const isValidEmail = () => {
      // 백에 신호 보내 인증 번호 받기 -> realNumber 바꿔주기
    }
    const isValidNumber = () => {
      // 인증 번호 확인
      if (realNumber === inputNumber) {
        return true
      } else {
        return false
      }
    }
    return {
      emailOptions,
      emailAddress,
      isValidEmail,
      isValidNumber,
      realNumber,
      inputNumber
    }
  }
}
</script>