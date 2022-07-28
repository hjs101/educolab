<template>
  <div>
    <q-input
      color="teal"
      label="생년월일"
      type="date"
      v-model="birthday"
      lazy-rules
      :rules="[ val => val && val.length > 0 || '생년월일을 입력해주세요']"
    />
  </div>
</template>

<script>
import {ref} from '@vue/reactivity'
export default {
  name: 'UserBirthday',
  props: {
    userType: String,
  },
  setup(props) {
    let birthday = ref(props.userType === 'student'?'2008-01-01':'1972-01-01')
    return {
      birthday
    }
  }
}
</script>