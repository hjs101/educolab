<template>
<<<<<<< HEAD
  <main class="q-mx">
=======
  <div class="q-mx">
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
    <h3 v-if="type.type">FIND {{type.title}}</h3>
    <!-- form 부분 -->
<<<<<<< HEAD
    <q-form
      class="q-gutter row">
<<<<<<< HEAD
      <section class="input col-8 offset-2 col-md-3 offset-md-4">
=======
    <q-form class="column justify-center">
      <section>
>>>>>>> db26c2a (Style & Fix : 스타일 및 오류 수정)
      <!-- 여기에 이름, 이메일 입력 창 -->
        <find-id />
        <send-pw-email v-if="!type.isTypeId" />
      </section>
    </q-form>
<<<<<<< HEAD
    <!-- 여기에 회원가입 로그인 비밀번호 찾기 -->
    <button-group v-if="type.type" :currentUrl="type.currentUrl"/>
  </main>
=======
      <div class="input col-8 offset-2 col-md-3 offset-md-4">
      <!-- 여기에 이름, 이메일 입력 창 -->
        <div v-if="type.type">
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
          <q-select
            v-model="userInfo.address"
            :options="emailOptions"
            class="col-4"
            label="이메일 주소 선택"
            required
          />
          <q-btn
            color="amber"
            label="FIND ID"
            v-if="type.isTypeId"
            class="col-8 offset-2 col-md-1 offset-md-1"
            @click="findId"
          />
        </div>
        <send-pw-email
          v-if="!type.isTypeId"
          :name="userInfo.computedName"
          :email="userInfo.fullEmail"
        />
      </div>
    </q-form>
    <q-dialog v-model="confirm.prompt" persistent>
      <q-card style="min-width: 350px">
        <q-card-section>
          <div class="text-h6 center">{{confirm.message}}</div>
        </q-card-section >
        <q-card-actions text-align="center">
          <button-group v-if="confirm.isSuccess" :currentUrl="type.currentUrl" @click="initInfo"/>
          <q-btn v-else color="primary" label="확인" v-close-popup/>
        </q-card-actions>
      </q-card>
    </q-dialog>
=======
>>>>>>> db26c2a (Style & Fix : 스타일 및 오류 수정)
    <!-- 여기에 회원가입 로그인 비밀번호 찾기 -->
    <button-group v-if="type.type" :currentUrl="type.currentUrl" @click="initInfo"/>
  </div>
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)

</template>

<style scoped>
  .input {
    width: 500px;
  }
</style>

<script>
import { reactive } from '@vue/reactivity'
import {computed, onBeforeMount} from 'vue'
<<<<<<< HEAD
<<<<<<< HEAD
import {useRoute} from 'vue-router'
import ButtonGroup from '@/components/ButtonGroup.vue'
import SendPwEmail from '@/components/SendPwEmail.vue'
import FindId from '@/components/FindId.vue'
import ChangeUserInfo from '@/components/ChangeUserInfo.vue'
=======
import {useRoute, useRouter} from 'vue-router'
import axios from 'axios'
import drf from '@/api/drf.js'
import ButtonGroup from '@/components/ButtonGroup.vue'
import SendPwEmail from '@/components/SendPwEmail.vue'
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
=======
import {useRoute, useRouter} from 'vue-router'
import { useStore } from 'vuex'
import ButtonGroup from '@/components/ButtonGroup.vue'
import SendPwEmail from '@/components/SendPwEmail.vue'
import FindId from '@/components/FindId.vue'
>>>>>>> 086e088 (Feat : 회원정보 수정, 비밀번호 변경 페이지 구현 완료)

export default {
  name: 'FindView',
  components: {
    ButtonGroup,
    SendPwEmail,
<<<<<<< HEAD
    FindId,
  },
  setup () {
    const store = useStore()
    const route = useRoute()
<<<<<<< HEAD
    // const router = useRouter()
=======
  },
  setup () {

    const route = useRoute()
    const router = useRouter()
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
=======
    const router = useRouter()
>>>>>>> 086e088 (Feat : 회원정보 수정, 비밀번호 변경 페이지 구현 완료)
    const type = reactive({
      type : computed(() => route.params.info),
      isTypeId: computed(() => type.type === 'id'),
      title : computed(() => type.isTypeId? 'ID':'PW'),
      currentUrl: computed(() => type.isTypeId? 'findId':'findPw'),
      })
<<<<<<< HEAD
    onBeforeMount (() => {
      if (!type.isTypeId && type.type !== 'password') {
        router.push('/404')
      } else if (store.getters.isLoggedIn) {
        router.push('/educolab')
      }
    })
    return {
      type,
=======
    const emailOptions = [
      '@gmail.com', '@naver.com', '@hanmail.com', '@nate.com', '직접 입력'
    ]
    const userInfo = reactive({
      name : null,
      email: '',
      address: null,
      fullEmail: computed(() => userInfo.email + userInfo.address),
      computedName: computed(() => userInfo.name),
    })
    const confirm = reactive({
      username: null,
      success: false,
      prompt: false,
      computedPrompt: computed(() => confirm.prompt),
      message: computed(() => type.isTypeId && confirm.success? `아이디는 ${confirm.username}입니다`: '입력하신 회원정보가 존재하지 않습니다'),
      isSuccess: computed(() => confirm.success)
    })
    const findId = () => {
      axios.post(drf.accounts.findUsername(), {name: userInfo.name, email: userInfo.fullEmail})
        .then((res) => {
          confirm.success = res.data.success
          confirm.prompt = true
          if (confirm.success) {
            confirm.username = res.data.username
            console.log(confirm.username)
            console.log(confirm.prompt)
          }
        })
    }
    const initInfo = () => {
      userInfo.name = null
      userInfo.email = ''
      userInfo.address = null
      confirm.username = null
      confirm.success = false
      confirm.prompt= false
    }
    onBeforeMount (() => {
      if (!type.isTypeId && type.type !== 'password' && !type.changeType) {
        router.push('/404')
      }
    })
    return {
      type,
      emailOptions,
      userInfo,
      confirm,
      findId,
      initInfo
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
    }
  },
}
</script>