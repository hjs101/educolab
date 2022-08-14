<template>
  <div>
    <h3>CHANGE PW</h3>
    <q-form
      class="q-gutter row">
      <div class="input col-8 offset-2 col-md-3 offset-md-4">
        <q-input
          color="teal"
          type="password"
          v-model="password.one"
          label="새 비밀번호"
          lazy-rules
          :rules="[ val => val && val.length > 0 || '비밀번호를 입력해주세요']"
        />
        <q-input
          color="teal"
          type="password"
          v-model="password.two"
          label="비밀번호 확인"
          lazy-rules
          :rules="[val => val !== null && val !== '' || '비밀번호를 입력해주세요']"
        />
        <p v-if="password.two">
        <span v-show="password.samePassword">비밀번호가 일치합니다</span>
        <span v-show="!password.samePassword">비밀번호가 일치하지 않습니다</span>
      </p>
      </div>
      <q-btn
        color="amber"
        label="CHANGE PW"
        class="col-8 offset-2 col-md-1 offset-md-1"
        @click="changePw"
      />
      <message-pop-up
        v-if="password.popUpFlag"
        :message="password.message"
        :path="'/'"
        />
    </q-form>
  </div>
</template>

<script>
import {computed, reactive} from 'vue'
import {useStore} from 'vuex'
import {useRouter} from 'vue-router'
import axios from 'axios'
import drf from '@/api/drf.js'
import MessagePopUp from '@/components/MessagePopUp.vue'
export default {
  name: 'ChangeView',
  components: {
    MessagePopUp,
  },
  props: {
    data: Object,
  },
  setup(props) {
    const store = useStore()
    const router = useRouter()
    const password = reactive({
      one: null,
      two: null,
      message: null,
      success: false,
      prompt: false,
      popUpFlag:computed(() => password.prompt),
      samePassword: computed(() => password.one === password.two)
    })
    const changePw = () => {
      axios({
        url: drf.accounts.changePw(),
        metthod: 'post',
        data: {
          ...props.data,
          password1:password.one,
          password2:password.two
        })
      .then(({data}) => {
        console.log(data)
        password.message = data.message
        password.success = data.success
      })
      .catch(({response}) => {
        password.message = response.data.message
        password.success = false
      })
      .finally(() => {
        password.prompt = true
      })
    }
    return {
      store,
      router,
      password,
      changePw
    }
  }
}
</script>