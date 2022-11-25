<template>
  <div style="height:700px;" class="q-mx column justify-center">

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
          label="ID"
          lazy-rules
          :rules="[ val => val && val.length > 0 || '아이디를 입력해주세요']"
        />

        <q-input
          class="col-10"
          color="teal"
          v-model="credentials.password"
          label="Password"
          type="password"
          @keyup.enter="login(credentials)"
          lazy-rules
          :rules="[
            val => val !== null && val !== '' || '비밀번호를 입력해주세요',
          ]"
        />
      </div>
      <!-- 여기에 로그인버튼 -->
      <q-btn
        color="secondary"
        class="q-ml-xl"
        label="LOGIN"
        type="submit"/>
    </q-form>

    <div class="text-center account-error-list">
      <p>{{ Error }}</p>
    </div>

    <!-- 여기에 회원가입 / ID 찾기 / 비밀번호 찾기 -->
    <button-group :currentUrl="currentUrl"/>
    <router-view></router-view>

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

<style scoped>
  .input {
    width: 500px;
  }
  .buttonGroup {
    margin-top: 100px;
  }
  .account-error-list {
    color: red;
  }
</style>

<script>
import { mapGetters, mapActions, useStore } from 'vuex'
import {onBeforeMount} from 'vue'
import {useRouter} from 'vue-router'
import ButtonGroup from '@/components/ButtonGroup.vue'

export default {
  name: 'LoginView',
  components: {
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
    ...mapGetters(['authError', 'isLoggedIn']),
    Error() {
      return this.authError
    }
  },
  methods: {
    ...mapActions(['login'])
  },
  setup () {
    const store = useStore()
    const router = useRouter()
    onBeforeMount(() => {
      if (store.getters.isLoggedIn) {
        router.push('/educolab')
      }
    })
  }
}
</script>