<template>
  <div>
    <div v-if="info">
      <q-input
        color="teal"
        v-model="data.username"
        label="아이디"
        lazy-rules
        :rules="[ val => val && val.length > 0 || '아이디를 입력해주세요']"
      />
      <confirm-auth-number :data="data"/>
    </div>
    <change-password
      v-else
      :data="data"
    />
  </div>

</template>



<script>
import {onMounted} from 'vue'
import {useRoute} from 'vue-router'
import { reactive} from '@vue/reactivity'
import ConfirmAuthNumber from '@/components/ConfirmAuthNumber.vue'
import ChangePassword from '@/components/ChangePassword.vue'
export default {
  name: 'SendPwEmail',
  components: {
    ConfirmAuthNumber,
    ChangePassword
    },
  props: {
    name: String,
    email: String,
  },
  setup(props){
    const route = useRoute()
    let info = route.params.info
    const data = reactive({
      name: props.name,
      email: props.email,
      username: '',
    })
    onMounted(() => {
      console.log(route)
    })
    return {
      data,
      info
    }
  }
}
</script>