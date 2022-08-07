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
    <change-password v-else :data="data" />
  </div>

</template>


<script>
import {computed} from 'vue'
import {useStore} from 'vuex'
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
    }
  }
}
</script>