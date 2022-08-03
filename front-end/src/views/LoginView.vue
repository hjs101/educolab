<template>
  <div class="q-mx">
    <h3>LOGIN</h3>
    <account-error-list></account-error-list>
    <!-- form 부분 -->
    <q-form
      @submit="login"
      class="q-gutter row"
    >
    <!-- 여기에 아이디, 비밀번호 입력 창 -->
      <div class="input col-8 offset-2 col-md-3 offset-md-4">
        <q-input
          color="teal"
          v-model="credentials.username"
          label="ID"
          lazy-rules
          :rules="[ val => val && val.length > 0 || '아이디를 입력해주세요']"
        />

        <q-input
          color="teal"
          v-model="credentials.password"
          label="Password"
          type="password"
          lazy-rules
          :rules="[
            val => val !== null && val !== '' || '비밀번호를 입력해주세요',
          ]"
        />
      </div>
      <!-- 여기에 로그인버튼 -->
      <q-btn
        color="secondary"
        label="LOGIN"
        class="col-8 offset-2 col-md-1 offset-md-1"
        @click="login(credentials)"/>
    </q-form>

    <!-- 여기에 회원가입 / ID 찾기 / 비밀번호 찾기 -->
    <button-group :currentUrl="currentUrl"/>
    <router-view></router-view>
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
// import { reactive } from '@vue/reactivity'
import { mapGetters, mapActions } from 'vuex'
import AccountErrorList from '@/components/AccountErrorList.vue'
import ButtonGroup from '@/components/ButtonGroup.vue'

export default {
  name: 'LoginView',
  components: {
    AccountErrorList,
    ButtonGroup
  },
  data () {
    return {
      credentials: {
        username : '',
        password: '',
      },
      currentUrl: 'login',
    }
  },
  computed: {
    ...mapGetters(['authError'])
  },
  methods: {
    ...mapActions(['login'])
  },
}
</script>