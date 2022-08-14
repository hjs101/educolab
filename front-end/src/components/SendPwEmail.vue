<template>
  <div>
<<<<<<< HEAD
    <div v-if="info">
      <q-input
        color="teal"
<<<<<<< HEAD
        v-model="data.username"
=======
        v-model="username"
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
        label="아이디"
        lazy-rules
        :rules="[ val => val && val.length > 0 || '아이디를 입력해주세요']"
      />
      <confirm-auth-number :data="data"/>
    </div>
<<<<<<< HEAD
    <change-password v-else :data="data" />
=======
    <change-password
      v-else
      :data="data"
    />
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
=======
    <q-input
      color="teal"
      v-model="data.username"
      label="아이디"
      lazy-rules
      :rules="[ val => val && val.length > 0 || '아이디를 입력해주세요']"
    />
    <confirm-auth-number :data="data"/>
>>>>>>> 086e088 (Feat : 회원정보 수정, 비밀번호 변경 페이지 구현 완료)
  </div>

</template>


<script>
import {computed} from 'vue'
<<<<<<< HEAD
import {useStore} from 'vuex'
import {useRoute} from 'vue-router'
<<<<<<< HEAD
import { reactive} from '@vue/reactivity'
=======
import {useRoute} from 'vue-router'
import { reactive, ref } from '@vue/reactivity'
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
=======
>>>>>>> 086e088 (Feat : 회원정보 수정, 비밀번호 변경 페이지 구현 완료)
import ConfirmAuthNumber from '@/components/ConfirmAuthNumber.vue'
export default {
  name: 'SendPwEmail',
  components: {
    ConfirmAuthNumber,
    },
<<<<<<< HEAD
  setup(){
    const route = useRoute()
    const store = useStore()
    let info = computed(() => route.params.info)
    let data = computed(() => store.getters.getInfo)
    return {
      data,
      info
=======
  props: {
    name: String,
    email: String,
  },
  setup(props){
    const route = useRoute()
    let info = computed(() => route.params.info)
    let username = ref('')
    const data = reactive({
      name: computed(() => props.name),
      email: computed(() => props.email),
      username: computed(() => username.value)
    })
    return {
      data,
      info,
      username
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
    }
  }
}
</script>