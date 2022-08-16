
<template>
  <div v-if="type.type" class="q-my-lg">
    <div class="row justify-center">
      <q-input
        class="col-4"
        color="teal"
        v-model="userInfo.name"
        label="이름"
        @change="changeData({name:userInfo.name})"
        lazy-rules
        :rules="[ val => val && val.length > 0 || '이름을 입력해주세요']"
      />
      <span class="col-12"></span>
      <q-input
        class="col-2 q-mr-md"
        color="teal"
        v-model="userInfo.email"
        label="이메일"
        @change="changeData({email:userInfo.fullEmail})"
        lazy-rules
        :rules="[
          val => val !== null && val !== '' || '이메일을 입력해주세요',
        ]"
      />
      <q-select
        v-model="address"
        :options="emailOptions"
        color="teal"
        class="col-2"
        label="이메일 주소 선택"
        required
      />
      <span class="col-12"></span>
      <q-btn
        class="col-4 q-my-lg text-size"
        color="amber"
        v-if="type.isTypeId"
        @click="findId">FIND ID</q-btn>
    </div>
    <message-pop-up
      v-if="confirm.computedPrompt"
      :message="confirm.message"
      :button="confirm.idSuccess"
      @reverse="confirm.prompt = false"
    />
  </div>
</template>

<script>
import { ref, reactive, computed, watch } from 'vue'
import { useStore } from 'vuex'
import { useRoute } from 'vue-router'
import axios from 'axios'
import drf from '@/api/drf.js'
import MessagePopUp from './MessagePopUp.vue'
export default {
  name: 'FindId',
  components: {
    MessagePopUp,
  },
  setup() {
    const route = useRoute()
    const store = useStore()
    const emailOptions = store.getters.getEmail
    const type = reactive({
      type : computed(() => route.params.info),
      isTypeId: computed(() => type.type === 'id'),
      })
    let address = ref('')
    const userInfo = reactive({
      name : null,
      email: '',
      fullEmail: computed(() => {
        if (userInfo.email && address.value) {
          if (address.value.startsWith('@')) {
            return userInfo.email + address.value
          } else {
            return userInfo.email
          }
        } else {
          return null
        }
      }),
      computedName: computed(() => userInfo.name),
    })
    const confirm = reactive({
      username: null,
      success: false,
      prompt: false,
      computedPrompt: computed(() => confirm.prompt),
      idSuccess:computed(() => type.isTypeId && confirm.success),
      message: computed(() => confirm.isSuccess? `아이디는 ${confirm.username}입니다`: '입력하신 회원정보가 존재하지 않습니다'),
      isSuccess: computed(() => confirm.success)
    })
    const changeData = (data) => {
      if (type.type && !type.isTypeId) {
        store.dispatch('changePwInfo', data)
      }
    }
    watch(address, () => {
      if (type.type && !type.isTypeId) {
        changeData({email:userInfo.fullEmail})
      }
    })
    const findId = () => {
      axios.post(drf.accounts.findUsername(), {name: userInfo.name, email: userInfo.fullEmail})
        .then((res) => {
          confirm.success = res.data.success
          if (confirm.success) {
            confirm.username = res.data.username
          }
        })
        .finally(() => {
          confirm.prompt = true
        })
    }
    return {
      emailOptions,
      type,
      userInfo,
      findId,
      confirm,
      changeData,
      address
    }
  },
}
</script>

<style scoped>
  .text-size {
    font-size: 1rem;
  }
</style>