<template>
  <div class="q-mx">
    <h3>FIND {{}}</h3>
    <!-- form 부분 -->
    <q-form
      class="q-gutter row"
    >
    <!-- 여기에 이름, 이메일 입력 창 -->
      <div class="input col-8 offset-2 col-md-3 offset-md-4">
        <q-input
          color="teal"
          v-model="userInfo.name"
          label="이름"
          lazy-rules
          :rules="[ val => val && val.length > 0 || '이름을 입력해주세요']"
        />
        <q-input
        color="teal"
        v-model="userInfo.email"
        label="이메일"
        lazy-rules
        :rules="[
          val => val !== null && val !== '' || '이메일을 입력해주세요',
        ]"
        />
        <q-select v-model="userInfo.address" :options="emailOptions" class="col-4" label="이메일 주소 선택" required />
      </div>
    </q-form>
      <!-- 여기에 아이디 찾기 버튼 -->
      <q-btn color="amber" label="FIND" class="col-8 offset-2 col-md-1 offset-md-1" @click="findId"/>

      <q-dialog v-model="confirm.prompt" persistent>
        <q-card style="min-width: 350px">
          <q-card-section>
            <div class="text-h6 center">{{confirm.message}}</div>
          </q-card-section >
          <q-card-actions align="center">
            <button-group v-if="confirm.isSuccess" :currentUrl="currentUrl"/>
            <q-btn v-else color="primary" label="확인" v-close-popup/>
          </q-card-actions>
        </q-card>
      </q-dialog>
    <!-- 여기에 회원가입 로그인 비밀번호 찾기 -->
    <button-group :currentUrl="currentUrl"/>
  </div>

</template>

<style scoped>
  .input {
    width: 500px;
  }
  .buttonGroup {
    margin-top: 100px;
  }
</style>

<script>
import { reactive } from '@vue/reactivity'
import {computed} from 'vue'
import {useRoute} from 'vue-router'
import axios from 'axios'
import drf from '@/api/drf.js'
import ButtonGroup from '@/components/ButtonGroup.vue'

export default {
  components: { ButtonGroup },
  name: 'FindView',
  setup () {
    const store = useRoute()
    const type = store.params.info
    const currentUrl = type === 'id'? 'findId':'findPw'
    const emailOptions = [
      '@gmail.com', '@naver.com', '@hanmail.com', '@nate.com', '직접 입력'
    ]
    const userInfo = reactive({
      name : null,
      email: null,
      address: null,
      username: null,
      fullEmail: computed(() => userInfo.email + userInfo.address)
    })
    const confirm = reactive({
      username: null,
      success: false,
      prompt: false,
      message: computed(() => type === 'id' && confirm.success? `아이디는 ${confirm.username}입니다`: '입력하신 회원정보가 존재하지 않습니다'),
      isSuccess: computed(() => confirm.success)
    })
    const findId = () => {
      axios.post(drf.accounts.findUsername(), {name: userInfo.name, email: userInfo.fullEmail})
        .then((res) => {
          confirm.success = res.data.success
          confirm.prompt = true
          if (confirm.success) {
            confirm.username = res.data.username
          }
        })
    }
    const findPw = () => {
      axios.post(drf.accounts.sendPwEmail(), {name: userInfo.name, email: userInfo.fullEmail, username: userInfo.username})
        .then((res) => {
          confirm.success = res.data.success
          confirm.prompt = true
          if (confirm.success) {
            console.log('1')
          }
        })
    }
    return {
      currentUrl,
      emailOptions,
      userInfo,
      confirm,
      findId,
      findPw
    }
  },
}
</script>