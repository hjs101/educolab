<template>
  <div>
    <div class="row justify-between">
      <q-input
      color="teal"
      v-model="email.username"
      input-class="text-right"
      class="col-5"
      label-slot
      clearable
      stack-label
      lazy-rules
      :rules="[ val => val && val.length > 0 || '이메일을 입력해주세요']"
      required
      >
        <template v-slot:label>
          <div class="row items-center all-pointer-events">
            Email
            <q-tooltip class="bg-grey-8" anchor="top left" self="bottom left" :offset="[0, 8]">Email address</q-tooltip>
          </div>
        </template>
      </q-input>
      <!-- 이메일 주소 선택 -->
      <q-select v-model="email.address" :options="emailOptions" class="col-4" label="이메일 주소 선택" required />
    </div>
    <confirm-auth-number :data="{email:email.fullEmail}"/>
  </div>
</template>

<script>
import {reactive} from '@vue/reactivity'
import {computed} from 'vue'
import ConfirmAuthNumber from '@/components/ConfirmAuthNumber.vue'
export default {
  name: 'EmailConfirm',
  components: {
    ConfirmAuthNumber,
  },
  setup () {
    const emailOptions = [
      '@gmail.com', '@naver.com', '@hanmail.com', '@nate.com', '직접 입력'
    ]
    const email = reactive({
      address: null,
      username: '',
      fullEmail: computed(() => {
        if (email.address) {
          if (email.address === '직접 입력') {
            return email.username
          } else {
            return email.username+email.address
          }
        } else {
          return null
        }
      }),
    })
    
    return {
      emailOptions,
      email,
    }
  }
}
</script>