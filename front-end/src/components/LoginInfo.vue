<template>
  <div>
    <q-input
      color="teal"
      label="아이디"
      v-model="userData.username"
      lazy-rules
      :rules="[ val => val && val.length > 0 || '아이디를 입력해주세요']"
    />
    <q-btn label="중복 확인" color="primary" @click="confirmUsername" />

    <q-dialog v-model="userData.confirm">
      <q-card>
        <q-card-section>
          <p>
            {{computedData.message}}
          </p>
          <br>
          <q-btn v-close-popup label="확인" color="primary" class="buttonGroup"/>
        </q-card-section>
      </q-card>
    </q-dialog>
    
    <p v-if="userData.password2 && computedData.validUsername !== 2">
      <span v-if="computedData.validUsername">
        {{computedData.message}}
      </span>
    </p>
    <q-input
      color="teal"
      label="비밀번호"
      type="password"
      v-model="userData.password1"
      lazy-rules
      :rules="[
        val => val !== null && val !== '' || '비밀번호를 입력해주세요',
      ]"
    />
    <q-input
      color="teal"
      label="비밀번호 확인"
      type="password"
      v-model="userData.password2"
      @keyup="isCorrect"
      lazy-rules
      :rules="[
        val => val !== null && val !== '' || '비밀번호를 다시 입력해주세요',
      ]"
    />
    <!-- 비밀번호 일치 여부 확인 -->
    <p v-if="userData.password2">
      <span v-show="computedData.samePassword">비밀번호가 일치합니다</span>
      <span v-show="!computedData.samePassword">비밀번호가 일치하지 않습니다</span>
    </p>
  </div>
</template>

<style>
</style>

<script>
import {reactive} from '@vue/reactivity'
import {computed} from 'vue'
import axios from 'axios'
import drf from '@/api/drf.js'
import {useStore} from 'vuex'
export default {
  name: 'LoginInfo',
  setup () {
    const store = useStore()
    const userData = reactive({
      username: null,
      password1: null,
      password2: null,
      correct: null,
      confirm: null,
    })
    const computedData = reactive({
      samePassword: computed(() => userData.correct),
      validUsername: computed(() => userData.confirm),
      message: computed(() => computedData.validUsername? '사용 가능한 아이디입니다':'중복된 아이디입니다. 다른 아이디를 입력해주세요')
    })
    const confirmUsername = () => {
      // 아이디 중복 여부 확인
      axios.get(drf.accounts.checkUsername(), {username: userData.username})
        .then((res) => {
          userData.confirm = res.data.dup === 'success'
          if (computedData.validUsername) {
            store.dispatch('changeData', {username: userData.username})
          }
        })
    }
    const isCorrect = () => {
      if (userData.password1 === userData.password2) {
        userData.correct = true
        store.dispatch('changeData', {password1: userData.password1, password2: userData.password2})
      } else {
        userData.correct = false
      }
    }
    return {
      userData,
      computedData,
      confirmUsername,
      isCorrect
    }
  }
}
</script>