<template>
  <div>
    <q-input
      color="teal"
      label="이름"
      v-model="info.name"
      maxlength="20"
      clearable
      :dense="false"
      lazy-rules
      :rules="[ val => val && val.length > 0 || '이름을 입력해주세요']"
    />
    <q-input
      color="teal"
      label="전화번호"
      v-model="info.phoneNumber"
      mask="###-####-####"
      clearable
      lazy-rules
      :rules="[ val => val && val.length > 0 || '전화번호를 입력해주세요']"
    />
  </div>
</template>

<script>
import {reactive} from '@vue/reactivity'
export default {
  name: 'UserPhoneNumber',
  setup() {
    const info = reactive({
      phoneNubmer: null,
      name: null
    })
    return {
      info
    }
  },
}
</script>