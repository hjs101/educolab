<template>
  <div>
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
  </div>

</template>


<script>
import {computed} from 'vue'
<<<<<<< HEAD
import {useStore} from 'vuex'
import {useRoute} from 'vue-router'
import { reactive} from '@vue/reactivity'
=======
import {useRoute} from 'vue-router'
import { reactive, ref } from '@vue/reactivity'
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
import ConfirmAuthNumber from '@/components/ConfirmAuthNumber.vue'
import ChangePassword from '@/components/ChangePassword.vue'
export default {
  name: 'SendPwEmail',
  components: {
    ConfirmAuthNumber,
    ChangePassword
    },
<<<<<<< HEAD
  setup(){
    const route = useRoute()
    const store = useStore()
    let info = computed(() => route.params.info)
    const data = reactive({
      name: computed(() => store.getters.getInfo.name),
      email: computed(() => store.getters.getInfo.email),
      username: null
    })
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