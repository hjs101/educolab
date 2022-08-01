<template>
  <q-input
    color="teal"
    label="휴대전화번호"
    v-model="phoneNumber"
    maxlength="13"
    :value="phoneNumber.value"
    @change="sendData"
    mask="###-####-####"
    clearable
    :dense="false"
    lazy-rules
    :rules="[ val => val && val.length > 0 || '휴대전화번호를 입력해주세요']"
  />
</template>

<script>
  import {ref} from '@vue/reactivity'
  import {useStore} from 'vuex'

  export default {
    name:'userPhoneNumber',
    setup() {
      const store = useStore()
      let phoneNumber = ref('')
      const sendData = () => {
        const value = phoneNumber.value.split('-')
        const convertNumber = value[0] + value[1] + value[2]
        store.dispatch('changeData', {phone_number: convertNumber})
      }
      return {
        sendData,
        phoneNumber
      }
    },
  }
</script>
