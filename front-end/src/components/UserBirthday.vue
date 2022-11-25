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
import {ref, onBeforeMount} from 'vue'
import {useStore} from 'vuex'
export default {
  name: 'UserBirthday',
  props: {
    date: String,
    userType: String,
    type: String,
  },
  setup(props) {
    const store = useStore()
    let birthday = ref(props.userType === 'student'?'2008-01-01':'1972-01-01')
    onBeforeMount(() => {
      if (props.date) {
        birthday.value = props.date
      }
    })
    const sendData = () => {
      const data = {birthday:birthday.value}
      if (props.type === 'change') {
        store.dispatch('changeInfo', data)
      } else {
        store.dispatch('changeData', data)
      }
    }
    return {
      birthday,
      sendData
    }
  }
}
</script>