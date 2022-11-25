<template>
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 89ccfeb ( Feat: 회원 가입 기능 완료 (백 통신해서 디버깅 해야 함))
  <q-input
    color="teal"
    label="생년월일"
    type="date"
    v-model="birthday"
    @change="sendData"
    lazy-rules
    :rules="[ val => val && val.length > 0 || '생년월일을 입력해주세요']"
  />
<<<<<<< HEAD
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
=======
>>>>>>> 89ccfeb ( Feat: 회원 가입 기능 완료 (백 통신해서 디버깅 해야 함))
</template>

<script>
import {ref} from '@vue/reactivity'
<<<<<<< HEAD
<<<<<<< HEAD
import {useStore} from 'vuex'
=======
>>>>>>> 03de9fd (Feat: 회원가입 학교 검색, 이름, 전화번호, 생년월일, 학년/반/번호)
=======
import {useStore} from 'vuex'
>>>>>>> 89ccfeb ( Feat: 회원 가입 기능 완료 (백 통신해서 디버깅 해야 함))
export default {
  name: 'UserBirthday',
  props: {
    userType: String,
  },
  setup(props) {
    let birthday = ref(props.userType === 'student'?'2008-01-01':'1972-01-01')
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 89ccfeb ( Feat: 회원 가입 기능 완료 (백 통신해서 디버깅 해야 함))
    const store = useStore()
    const sendData = () => {
      store.dispatch('changeData', {birthday:birthday.value})
    }
<<<<<<< HEAD
    return {
      birthday,
      sendData
=======
    return {
      birthday
>>>>>>> 03de9fd (Feat: 회원가입 학교 검색, 이름, 전화번호, 생년월일, 학년/반/번호)
=======
    return {
      birthday,
      sendData
>>>>>>> 89ccfeb ( Feat: 회원 가입 기능 완료 (백 통신해서 디버깅 해야 함))
    }
  }
}
</script>