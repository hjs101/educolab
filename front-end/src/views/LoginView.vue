<template>
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e6b54fb (asdu)
=======
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
  <div class="q-mx">
=======
  <div style="height:900px;" class="q-mx column justify-center">
>>>>>>> 7f2a492 (설문조사  sass)
=======
  <div style="height:800px;" class="q-mx column justify-center">
>>>>>>> eb5987b (로그인  버그 수정)
=======
  <div style="height:700px;" class="q-mx column justify-center">
<<<<<<< HEAD
>>>>>>> db26c2a (Style & Fix : 스타일 및 오류 수정)
=======

>>>>>>> 5264803 (프론트 버그 수정2)
    <h3>LOGIN</h3>
    <!-- form 부분 -->
    <q-form
      @submit="login(credentials)"
      class="row justify-center"
    >
    <!-- 여기에 아이디, 비밀번호 입력 창 -->
      <div class="row justify-end">
        <q-input
          class="col-10"
          color="teal"
          v-model="credentials.username"
<<<<<<< HEAD
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
=======
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
          label="ID"
          lazy-rules
          :rules="[ val => val && val.length > 0 || '아이디를 입력해주세요']"
        />

        <q-input
          class="col-10"
          color="teal"
<<<<<<< HEAD
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
<<<<<<< HEAD
          @keyup.enter="login"
=======
          v-model="credentials.password"
          label="Password"
          type="password"
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
=======
          @keyup.enter="login(credentials)"
>>>>>>> 885b034 (Feat : 칭호 적용)
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

=======
=======
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
      <q-btn
        color="secondary"
        class="q-ml-xl"
        label="LOGIN"
<<<<<<< HEAD
        class="col-8 offset-2 col-md-1 offset-md-1"
<<<<<<< HEAD
        @click="login(credentials)"/>
<<<<<<< HEAD
>>>>>>> d7025b4 (Feat : 비밀번호 변경 페이지 제작 & 컴포넌트화 & 비밀번호 변경 기능 진행 중)
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
=======
=======
=======
>>>>>>> db26c2a (Style & Fix : 스타일 및 오류 수정)
        type="submit"/>
>>>>>>> 885b034 (Feat : 칭호 적용)
    </q-form>

    <div class="text-center account-error-list">
      <p>{{ Error }}</p>
    </div>

    <!-- 여기에 회원가입 / ID 찾기 / 비밀번호 찾기 -->
    <button-group :currentUrl="currentUrl"/>
    <router-view></router-view>
<<<<<<< HEAD
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
  </div>
=======
>>>>>>> 7f2a492 (설문조사  sass)

    <footer class="bord-top bg-blue-grey-12 q-py-sm fixed-bottom" width="100%">
      <div class="row justify-start items-center">
        <img class="q-mx-xl" src="@/assets/footerlogo.png" alt="educolab" style="width:5rem; height:5rem;">
        <div class="ftr-size">
          <span class="text-bold">"교육과 서비스의 청량한 조화" edu colab!!</span><hr>
          <span>edu colab는 학습 역량 증진 / 교육 연계 보조 / 수업의 질 향상을 목표로 합니다.</span>
          <p>교사에게는 편리한, 학생에게는 학습욕구를 팽창시켜드립니다!!</p>
        </div>
      </div>
    </footer>
  </div>
</template>

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> c942112 (로그인 프론트와 백 연결)
=======
>>>>>>> e6b54fb (asdu)
=======
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
<style scoped>
  .input {
    width: 500px;
  }
  .buttonGroup {
    margin-top: 100px;
<<<<<<< HEAD
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
=======
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
  }
  .account-error-list {
    color: red;
  }
</style>

<script>
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e6b54fb (asdu)
// import { reactive } from '@vue/reactivity'
=======
>>>>>>> c2bb4de (공지사항 파일 버그 수정)
import { mapGetters, mapActions, useStore } from 'vuex'
import {onBeforeMount} from 'vue'
<<<<<<< HEAD
import {useRouter, useRoute} from 'vue-router'
=======
// import { reactive } from '@vue/reactivity'
import { mapGetters, mapActions } from 'vuex'
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
=======
import {useRouter} from 'vue-router'
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c8c893f (Feat: 로그인 여부 & 사용자 여부에 따른 접근 제한)
import AccountErrorList from '@/components/AccountErrorList.vue'
=======
// import AccountErrorList from '@/components/AccountErrorList.vue'
>>>>>>> 5264803 (프론트 버그 수정2)
=======
>>>>>>> c2bb4de (공지사항 파일 버그 수정)
import ButtonGroup from '@/components/ButtonGroup.vue'

export default {
  name: 'LoginView',
  components: {
    ButtonGroup
  },
<<<<<<< HEAD
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
=======
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
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
    ...mapGetters(['authError', 'isLoggedIn']),
    Error() {
      return this.authError
    }
  },
  methods: {
    ...mapActions(['login'])
  },
<<<<<<< HEAD
  setup () {
    const store = useStore()
    const router = useRouter()
    onBeforeMount(() => {
      if (store.getters.isLoggedIn) {
<<<<<<< HEAD
        console.log(router)
        console.log(route)
=======
        router.push('/educolab')
>>>>>>> c8c893f (Feat: 로그인 여부 & 사용자 여부에 따른 접근 제한)
      }
    })
  },
  created() {
    if (this.isLoggedIn) {
      this.$router.back()
    }
  }
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
=======
}
</script>
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
