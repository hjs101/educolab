<template>
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 89ccfeb ( Feat: 회원 가입 기능 완료 (백 통신해서 디버깅 해야 함))
=======
>>>>>>> e6b54fb (asdu)
=======
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
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
<<<<<<< HEAD
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
=======
>>>>>>> e6b54fb (asdu)
=======
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
</template>

<script>
<<<<<<< HEAD
import {ref} from '@vue/reactivity'
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
import {ref, onBeforeMount} from 'vue'
>>>>>>> 086e088 (Feat : 회원정보 수정, 비밀번호 변경 페이지 구현 완료)
import {useStore} from 'vuex'
=======
>>>>>>> 03de9fd (Feat: 회원가입 학교 검색, 이름, 전화번호, 생년월일, 학년/반/번호)
=======
import {useStore} from 'vuex'
>>>>>>> 89ccfeb ( Feat: 회원 가입 기능 완료 (백 통신해서 디버깅 해야 함))
=======
import {useStore} from 'vuex'
>>>>>>> e6b54fb (asdu)
=======
import {useStore} from 'vuex'
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
export default {
  name: 'UserBirthday',
  props: {
    date: String,
    userType: String,
    type: String,
  },
  setup(props) {
<<<<<<< HEAD
    let birthday = ref(props.userType === 'student'?'2008-01-01':'1972-01-01')
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 89ccfeb ( Feat: 회원 가입 기능 완료 (백 통신해서 디버깅 해야 함))
=======
>>>>>>> e6b54fb (asdu)
=======
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
=======
>>>>>>> 086e088 (Feat : 회원정보 수정, 비밀번호 변경 페이지 구현 완료)
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
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
    return {
      birthday,
      sendData
>>>>>>> e6b54fb (asdu)
=======
    return {
      birthday,
      sendData
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
    }
  }
}
</script>