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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e6b54fb (asdu)
=======
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
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
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
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
>>>>>>> 89ccfeb ( Feat: 회원 가입 기능 완료 (백 통신해서 디버깅 해야 함))
=======
>>>>>>> e6b54fb (asdu)
=======
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
