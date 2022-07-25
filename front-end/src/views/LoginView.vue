<template>
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
          label="ID"
          lazy-rules
          :rules="[ val => val && val.length > 0 || '아이디를 입력해주세요']"
        />

        <q-input
          color="teal"
          v-model="pwValue"
          label="Password"
          type="password"
          lazy-rules
          :rules="[
            val => val !== null && val !== '' || '비밀번호를 입력해주세요',
          ]"
        />
      </div>
      <!-- 여기에 로그인버튼 -->
      <q-btn color="secondary" label="LOG IN" class="col-1" @click="login"/>

    </q-form>

    <!-- 여기에 회원가입 / ID 찾기 / 비밀번호 찾기 -->
    <div class="userGroup">
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
  }
</style>

<script>
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
