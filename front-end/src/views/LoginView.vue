<template>
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e6b54fb (asdu)
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
<<<<<<< HEAD
=======
  <div class="q-pa-md">
    <!-- 반응형 아직 X -->
=======
  <div class="q-mx">
    <!-- 반응형하는 중 -->
>>>>>>> 860f864 (Refactor : 로그인, 회원가입 동의 페이지 코드 수정 & 404 페이지 만듦)
    <h3>LOGIN</h3>
    <!-- form 부분 -->
    <q-form
      @submit="login"
      class="q-gutter row"
    >
    <!-- 여기에 아이디, 비밀번호 입력 창 -->
      <div class="input col-8 offset-2 col-md-3 offset-md-4">
        <q-input
          color="teal"
<<<<<<< HEAD
<<<<<<< HEAD
          v-model="idValue"
>>>>>>> 23e74e9 (Feat : 로그인 화면 제작 완료 & 기능 구현 미완료 & 약관 동의 화면 구현)
=======
          v-model="state.username"
>>>>>>> 860f864 (Refactor : 로그인, 회원가입 동의 페이지 코드 수정 & 404 페이지 만듦)
=======
          v-model="credentials.username"
>>>>>>> c942112 (로그인 프론트와 백 연결)
=======
>>>>>>> e6b54fb (asdu)
          label="ID"
          lazy-rules
          :rules="[ val => val && val.length > 0 || '아이디를 입력해주세요']"
        />

        <q-input
          color="teal"
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
          v-model="credentials.password"
=======
          v-model="pwValue"
>>>>>>> 23e74e9 (Feat : 로그인 화면 제작 완료 & 기능 구현 미완료 & 약관 동의 화면 구현)
=======
          v-model="state.password"
>>>>>>> 860f864 (Refactor : 로그인, 회원가입 동의 페이지 코드 수정 & 404 페이지 만듦)
=======
          v-model="credentials.password"
>>>>>>> c942112 (로그인 프론트와 백 연결)
=======
          v-model="credentials.password"
>>>>>>> e6b54fb (asdu)
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
      <q-btn color="secondary" label="LOGIN" class="col-8 offset-2 col-md-1 offset-md-1" @click="login(credentials)"/>
=======
      <q-btn color="secondary" label="LOG IN" class="col-1" @click="login"/>
>>>>>>> 23e74e9 (Feat : 로그인 화면 제작 완료 & 기능 구현 미완료 & 약관 동의 화면 구현)
=======
      <q-btn color="secondary" label="LOG IN" class="col-8 offset-2 col-md-1 offset-md-1" @click="login"/>
>>>>>>> 860f864 (Refactor : 로그인, 회원가입 동의 페이지 코드 수정 & 404 페이지 만듦)
=======
      <q-btn color="secondary" label="LOGIN" class="col-8 offset-2 col-md-1 offset-md-1" @click="login(credentials)"/>
>>>>>>> c942112 (로그인 프론트와 백 연결)
=======
      <q-btn color="secondary" label="LOGIN" class="col-8 offset-2 col-md-1 offset-md-1" @click="login(credentials)"/>
>>>>>>> e6b54fb (asdu)

    </q-form>

    <!-- 여기에 회원가입 / ID 찾기 / 비밀번호 찾기 -->
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    <div class="buttonGroup">
=======
    <div class="userGroup">
>>>>>>> 23e74e9 (Feat : 로그인 화면 제작 완료 & 기능 구현 미완료 & 약관 동의 화면 구현)
=======
    <div class="buttonGroup">
>>>>>>> 860f864 (Refactor : 로그인, 회원가입 동의 페이지 코드 수정 & 404 페이지 만듦)
=======
    <div class="buttonGroup">
>>>>>>> e6b54fb (asdu)
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
=======
    <button-group :currentUrl="currentUrl"/>
    <router-view></router-view>
>>>>>>> c780a28 (Feat : 아이디 찾기 기능 완료 & 비밀번호 찾기 진행 중)
  </div>

</template>

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> c942112 (로그인 프론트와 백 연결)
=======
>>>>>>> e6b54fb (asdu)
<style scoped>
  .input {
    width: 500px;
  }
  .buttonGroup {
    margin-top: 100px;
<<<<<<< HEAD
<<<<<<< HEAD
=======
<style>
  .login {
    margin-left: auto;
    margin-right: auto;
  }
  h3 {
    text-align: center;
  }
=======
<style scoped>
>>>>>>> 860f864 (Refactor : 로그인, 회원가입 동의 페이지 코드 수정 & 404 페이지 만듦)
  .input {
    width: 500px;
  }
  .buttonGroup {
    margin-top: 100px;
<<<<<<< HEAD
    text-align: center;
    gap: 10px;
  }
  .button {
    text-decoration: none;
>>>>>>> 23e74e9 (Feat : 로그인 화면 제작 완료 & 기능 구현 미완료 & 약관 동의 화면 구현)
=======
>>>>>>> 860f864 (Refactor : 로그인, 회원가입 동의 페이지 코드 수정 & 404 페이지 만듦)
=======
>>>>>>> c942112 (로그인 프론트와 백 연결)
=======
>>>>>>> e6b54fb (asdu)
  }
</style>

<script>
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e6b54fb (asdu)
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
<<<<<<< HEAD
=======
// import { reactive } from '@vue/reactivity'
import { mapGetters, mapActions } from 'vuex'
import AccountErrorList from '@/components/AccountErrorList.vue'

export default {
  name: 'LoginView',
<<<<<<< HEAD
>>>>>>> c942112 (로그인 프론트와 백 연결)
=======
  components: {
    AccountErrorList
  },
>>>>>>> 77a4159 (로그아웃 구현)
=======
>>>>>>> e6b54fb (asdu)
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
<<<<<<< HEAD
<<<<<<< HEAD
</script>
=======
import {mapActions} from 'vuex'
=======
import { reactive } from '@vue/reactivity'
>>>>>>> 860f864 (Refactor : 로그인, 회원가입 동의 페이지 코드 수정 & 404 페이지 만듦)

export default {
  name: 'LoginView',
  setup () {
    // 기존의 data
    const state = reactive({
      username: '',
      password: ''
    })
    // method 부분
    const login = () => {
      // login method
      // state 호출할 때 this 바인딩이 필요하지 않음
    }
    return {
      login,
      state
    }
  }
}
</script>
>>>>>>> 23e74e9 (Feat : 로그인 화면 제작 완료 & 기능 구현 미완료 & 약관 동의 화면 구현)
=======
  <h1>로그인 페이지</h1>
</template>

<script>
export default {
  name: 'LoginView',
}
</script>
>>>>>>> 3d37e1b (공지사항 검색기능 구현)
=======
</script>
>>>>>>> c942112 (로그인 프론트와 백 연결)
=======
</script>
>>>>>>> e6b54fb (asdu)
