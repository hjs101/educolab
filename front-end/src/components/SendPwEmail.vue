<template>
  <div>
    <q-input
      color="teal"
      v-model="username"
      label="아이디"
      lazy-rules
      :rules="[ val => val && val.length > 0 || '아이디를 입력해주세요']"
    />
    <q-btn color="white" text-color="black" label="FIND PW" class="col-8 offset-2 col-md-1 offset-md-1" @click="findPw"/>
    <!-- 인증 버튼 (아래 복붙) -->
    <q-btn color="teal" label="인증" class="col-2" @click="isValidEmail"/>
    <!-- 인증 번호 입력 창 -->
    <div v-if="email.showAuth" class="row justify-between">
      <q-input
        color="teal"
        v-model="number.inputNum"
        class="col-9"
        lazy-rules
        :rules="[ val => val && val.length > 0 || '인증번호를 입력해주세요']"
      />
      <!-- 인증 번호 확인 버튼 -->
      <q-btn color="teal" label="인증" class="buttonGroup col-2" @click="alert = true" />
      <!-- 인증 제한 시간 -->
      <p>
        제한 시간 {{time.minute}}:{{time.second}}
      </p>
      <!-- 인증 번호 일치 여부 팝업-->
      <q-dialog v-model="alert">
        <q-card>
          <q-card-section>
            <div class="text-h6">인증 번호 확인</div>
          </q-card-section>

          <q-card-section class="q-pt-none">
            <span v-if="number.isAuthNum && number.isValidNumber">
              인증되었습니다
            </span>
            <span v-else>
              인증번호가 일치하지 않습니다
            </span>
          </q-card-section>

          <q-card-actions align="right">
            <q-btn flat label="확인" color="primary" v-close-popup @click="sendData({email:email.fullEmail})"/>
          </q-card-actions>
        </q-card>
      </q-dialog>
    </div>

  </div>

</template>



<script>
import { reactive, ref } from '@vue/reactivity'
// import {computed} from 'vue'
import axios from 'axios'
import drf from '@/api/drf.js'
export default {
  name: 'SendPwEmail',
  props: {
    name: String,
    email: String,
  },
  setup() {
    let username = ref('')
    const confirm = reactive({
      prompt: false,
    })
    const findPw = (props) => {
      axios.post(drf.accounts.sendPwEmail(), {name:props.name, email:props.email, username,})
        .then((res) => {
          // confirm.success = res.data.success
          // confirm.prompt = true
          // if (confirm.success) {
          //   console.log('1')
          // }
        })
    }
    return {
      username,
      confirm,
      findPw
    }
  }
}
</script>