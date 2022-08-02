<template>
  <div>
    <q-input
      color="teal"
      v-model="data.username"
      label="아이디"
      lazy-rules
      :rules="[ val => val && val.length > 0 || '아이디를 입력해주세요']"
    />
    <confirm-auth-number :data="data"/>
  </div>

</template>



<script>
import { reactive} from '@vue/reactivity'
import ConfirmAuthNumber from '@/components/ConfirmAuthNumber.vue'
export default {
  name: 'SendPwEmail',
  components: { ConfirmAuthNumber },
  props: {
    name: String,
    email: String,
  },
  setup(props){
    const data = reactive({
      name: props.name,
      email: props.email,
      username: '',
    })
    return {
      data,
    }
  }
}
</script>