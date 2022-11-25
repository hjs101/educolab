<template>
<<<<<<< HEAD
  <q-input
    color="teal"
    label="생년월일"
    type="date"
    v-model="birthday"
    @change="sendData"
    lazy-rules
    :rules="[ val => val && val.length > 0 || '생년월일을 입력해주세요']"
  />
=======
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
>>>>>>> 03de9fd (Feat: 회원가입 학교 검색, 이름, 전화번호, 생년월일, 학년/반/번호)
</template>

<script>
import {ref} from '@vue/reactivity'
<<<<<<< HEAD
import {useStore} from 'vuex'
=======
>>>>>>> 03de9fd (Feat: 회원가입 학교 검색, 이름, 전화번호, 생년월일, 학년/반/번호)
export default {
  name: 'UserBirthday',
  props: {
    userType: String,
  },
  setup(props) {
    let birthday = ref(props.userType === 'student'?'2008-01-01':'1972-01-01')
<<<<<<< HEAD
    const store = useStore()
    const sendData = () => {
      store.dispatch('changeData', {birthday:birthday.value})
    }
    return {
      birthday,
      sendData
=======
    return {
      birthday
>>>>>>> 03de9fd (Feat: 회원가입 학교 검색, 이름, 전화번호, 생년월일, 학년/반/번호)
    }
  }
}
</script>