<template>
  <q-input
    color="teal"
    label="생년월일"
    type="date"
    v-model="birthday"
    @change="sendData"
    lazy-rules
    :rules="[ val => val && val.length > 0 || '생년월일을 입력해주세요']"
  />
</template>

<script>
import {ref} from '@vue/reactivity'
import {useStore} from 'vuex'
export default {
  name: 'UserBirthday',
  props: {
    userType: String,
  },
  setup(props) {
    let birthday = ref(props.userType === 'student'?'2008-01-01':'1972-01-01')
    const store = useStore()
    const sendData = () => {
      store.dispatch('changeData', {birthday:birthday.value})
    }
    return {
      birthday,
      sendData
    }
  }
}
</script>