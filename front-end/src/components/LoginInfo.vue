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
<<<<<<< HEAD

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
=======
    <p v-if="userData.password2 && computedData.validUsername !== 2">
      <span v-show="computedData.validUsername">사용가능한 아이디입니다</span>
      <span v-show="!computedData.validUsername">이미 존재하는 아이디입니다/다른 아이디 값을 입력해주세요</span>
>>>>>>> 147871f (Feat : 회원가입 틀 제작 후 이름까지 완료 (그 이후 부분은 미완성))
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
<<<<<<< HEAD
=======
      @change="$emit(toSignup)"
>>>>>>> 147871f (Feat : 회원가입 틀 제작 후 이름까지 완료 (그 이후 부분은 미완성))
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
<<<<<<< HEAD
import axios from 'axios'
import drf from '@/api/drf.js'
import {useStore} from 'vuex'
export default {
  name: 'LoginInfo',
  setup () {
    const store = useStore()
=======
// import axios from 'axios';
export default {
  name: 'LoginInfo',
  setup (props, {emit}) {
>>>>>>> 147871f (Feat : 회원가입 틀 제작 후 이름까지 완료 (그 이후 부분은 미완성))
    const userData = reactive({
      username: null,
      password1: null,
      password2: null,
      correct: null,
<<<<<<< HEAD
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
=======
      confirm: 2,
    })
    const computedData = reactive({
      samePassword: computed(() => userData.correct),
      validUsername: computed(() => userData.confirm)
    })
    const confirmUsername = () => {
      // 아이디 일치 여부 확인
      // const data = {username: userData.username}
    
    //   axios.get('', data)
    //     .then((res) => {
    //       // 변수명 알아내야 함
    //       confirm = res.data
      console.log(userData.username)
>>>>>>> 147871f (Feat : 회원가입 틀 제작 후 이름까지 완료 (그 이후 부분은 미완성))
    }
    const isCorrect = () => {
      if (userData.password1 === userData.password2) {
        userData.correct = true
<<<<<<< HEAD
        store.dispatch('changeData', {password1: userData.password1, password2: userData.password2})
=======
>>>>>>> 147871f (Feat : 회원가입 틀 제작 후 이름까지 완료 (그 이후 부분은 미완성))
      } else {
        userData.correct = false
      }
    }
<<<<<<< HEAD
=======
    const toSignup = () => {
      emit('to-signup', userData)
    }
>>>>>>> 147871f (Feat : 회원가입 틀 제작 후 이름까지 완료 (그 이후 부분은 미완성))
    return {
      userData,
      computedData,
      confirmUsername,
<<<<<<< HEAD
      isCorrect
    }
  }
=======
      isCorrect,
      toSignup
    }
  },
>>>>>>> 147871f (Feat : 회원가입 틀 제작 후 이름까지 완료 (그 이후 부분은 미완성))
}
</script>