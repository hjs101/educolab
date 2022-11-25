<template>
  <q-input
    color="teal"
    label="전화번호"
    v-model="phoneNumber"
    mask="###-####-####"
    maxlength="13"
    @change="sendData"
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
    props: {
      number: String,
      type: String,
    },
    setup(props) {
      const store = useStore()
      let phoneNumber = ref( `${props.number?.slice(0,3)}-${props.number?.slice(3,7)}-${props.number?.slice(7,11)}` || '')
      const sendData = () => {
        const value = phoneNumber.value.split('-')
        const convertNumber = {phone_number: value[0] + value[1] + value[2]}
        if (props.type !== 'change') {
          store.dispatch('changeData', convertNumber)
        } else {
          store.dispatch('changeInfo', convertNumber)
        }
      }
      return {
        sendData,
        phoneNumber
      }
    },
  }
</script>
