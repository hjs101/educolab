<template>
<<<<<<< HEAD
  <q-input
    color="teal"
    label="전화번호"
    v-model="phoneNumber"
    maxlength="13"
    :value="phoneNumber.value"
    @change="sendData"
    mask="###-####-####"
    clearable
    :dense="false"
    lazy-rules
    :rules="[ val => val && val.length > 0 || '이름을 입력해주세요']"
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
        store.dispatch('changeData', {phoneNumber: convertNumber})
      }
      return {
        sendData,
        phoneNumber
      }
    },
  }
</script>
=======
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
>>>>>>> 03de9fd (Feat: 회원가입 학교 검색, 이름, 전화번호, 생년월일, 학년/반/번호)
