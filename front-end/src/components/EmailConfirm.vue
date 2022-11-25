<template>
  <div>
    <div class="row justify-between align-baseline">
      <q-input
        color="teal"
        v-model="email.username"
        input-class="text-right"
        class="col-5"
        clearable
        stack-label
        label="Email"
        lazy-rules
        :rules="[ val => val && val.length > 0 || '이메일을 입력해주세요']"
        required />
      <!-- 이메일 주소 선택 -->
      <q-select
        v-model="email.address"
        :options="emailOptions"
        color="teal"
        class="col-4"
        label="이메일 주소 선택"
        lazy-rules
        :rules="[ val => val && val.length > 0 || '이메일 주소를 선택해주세요']"
        required/>
      <confirm-auth-number :data="{email:email.fullEmail}"/>
    </div>
  </div>
</template>

<script>
import {computed, onMounted, reactive} from 'vue'
import { useStore } from 'vuex'
import ConfirmAuthNumber from '@/components/ConfirmAuthNumber.vue'
export default {
  name: 'EmailConfirm',
  props: {
    fullEmail: String,
    type: String,
  },
  components: {
    ConfirmAuthNumber,
  },
  setup (props) {
    const store = useStore()
    const emailOptions = store.getters.getEmail
    let mail = computed(() => props.fullEmail?.split('@'))
    const email = reactive({
      address: null,
      username: '',
      fullEmail: computed(() => {
        if (email.address && email.username) {
          if (email.address.startsWith('@')) {
            return email.username+email.address
          } else {
            return email.username
          }
        } else {
          return null
        }
      }),
    })
    onMounted(() => {
      if (props.type === 'change') {
        if (emailOptions.indexOf(`@${mail.value[1]}`) !== -1) {
          email.address = `@${mail.value[1]}`
          email.username = mail.value[0]
        } else {
          email.address = '직접 입력'
          email.username = props.fullEmail
        }
      }
    })
    
    return {
      emailOptions,
      email,
    }
  }
}
</script>