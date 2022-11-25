<template>
<<<<<<< HEAD
  <div class="q-mx">
    <!-- 반응형하는 중 -->
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
=======
  <div class="q-pa-md">
    <!-- 반응형 아직 X -->
    <h3>LOGIN</h3>
    <q-form
      @submit="onSubmit"
      class="q-gutter-md row"
    >
    <!-- 여기에 아이디, 비밀번호 입력 창 -->
      <div class="input col-3 offset-4">
        <q-input
          color="teal"
          v-model="idValue"
>>>>>>> 23e74e9 (Feat : 로그인 화면 제작 완료 & 기능 구현 미완료 & 약관 동의 화면 구현)
          label="ID"
          lazy-rules
          :rules="[ val => val && val.length > 0 || '아이디를 입력해주세요']"
        />

        <q-input
          color="teal"
<<<<<<< HEAD
          v-model="credentials.password"
=======
          v-model="pwValue"
>>>>>>> 23e74e9 (Feat : 로그인 화면 제작 완료 & 기능 구현 미완료 & 약관 동의 화면 구현)
          label="Password"
          type="password"
          lazy-rules
          :rules="[
            val => val !== null && val !== '' || '비밀번호를 입력해주세요',
          ]"
        />
      </div>
      <!-- 여기에 로그인버튼 -->
<<<<<<< HEAD
      <q-btn color="secondary" label="LOGIN" class="col-8 offset-2 col-md-1 offset-md-1" @click="login(credentials)"/>
=======
      <q-btn color="secondary" label="LOG IN" class="col-1" @click="login"/>
>>>>>>> 23e74e9 (Feat : 로그인 화면 제작 완료 & 기능 구현 미완료 & 약관 동의 화면 구현)

    </q-form>

    <!-- 여기에 회원가입 / ID 찾기 / 비밀번호 찾기 -->
<<<<<<< HEAD
    <div class="buttonGroup">
=======
    <div class="userGroup">
>>>>>>> 23e74e9 (Feat : 로그인 화면 제작 완료 & 기능 구현 미완료 & 약관 동의 화면 구현)
      <router-link to="/signup" class="button">
        <q-btn color="primary" label="SIGN UP"/>
      </router-link>
      <router-link to="#" class="button">
        <q-btn color="amber" label="FIND ID" />
      </router-link>
      <router-link to="#" class="button">
        <q-btn color="light" text-color="black" label="FIND PW" />
      </router-link>
      <router-view></router-view>
    </div>
  </div>

</template>

<<<<<<< HEAD
<style scoped>
  .input {
    width: 500px;
  }
  .buttonGroup {
    margin-top: 100px;
=======
<style>
  .login {
    margin-left: auto;
    margin-right: auto;
  }
  h3 {
    text-align: center;
  }
  .input {
    width: 500px;
    margin-right: 50px;
  }
  .userGroup {
    display: flex;
    justify-content: center;
    margin-top: 100px;
    text-align: center;
    gap: 10px;
  }
  .button {
    text-decoration: none;
>>>>>>> 23e74e9 (Feat : 로그인 화면 제작 완료 & 기능 구현 미완료 & 약관 동의 화면 구현)
  }
</style>

<script>
<<<<<<< HEAD
// import { reactive } from '@vue/reactivity'
import { mapGetters, mapActions } from 'vuex'
import AccountErrorList from '@/components/AccountErrorList.vue'

export default {
  name: 'LoginView',
  components: {
    AccountErrorList
  },
  data () {
    return {
      credentials: {
        username : '',
        password: '',
      }
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
=======
import {mapActions} from 'vuex'

export default {
  name: 'LoginView',
  data: function () {
    return {
      idValue: null,
      pwValue: null,
    }
  },
  methods: {
    ...mapActions(['login'])
  }
}
</script>
>>>>>>> 23e74e9 (Feat : 로그인 화면 제작 완료 & 기능 구현 미완료 & 약관 동의 화면 구현)
