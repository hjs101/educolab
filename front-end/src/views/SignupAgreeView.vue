<template>
  <div class="q-ma-md">
    <h3>SIGN UP</h3>
    <!-- 여기에 약관 동의-->
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e6b54fb (asdu)
=======
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
    <div class="row">
      <q-scroll-area class="col-6 offset-3 scroll">
        <use-provision />
      </q-scroll-area>
      <q-scroll-area class="col-6 offset-3 scroll">
        <use-info />
      </q-scroll-area>
      <!-- 여기에 체크 박스 -->
      <q-checkbox v-model="isChecked" label="위의 약관에 모두 동의합니다" color="teal" class="col-5 offset-5" />
      <br>
    </div>
      <!-- 여기에 버튼 -->
    <div class="buttonGroup" v-if="isChecked">
<<<<<<< HEAD
<<<<<<< HEAD
=======
    <div class="row">
      <q-scroll-area class="col-6 offset-3 scroll">
        <use-provision />
      </q-scroll-area>
      <q-scroll-area class="col-6 offset-3 scroll">
        <use-info />
      </q-scroll-area>
      <!-- 여기에 체크 박스 -->
      <q-checkbox v-model="isChecked" label="위의 약관에 모두 동의합니다" color="teal" class="col-4 offset-4" />
      <!-- 여기에 버튼 -->
      <br>
    </div>
<<<<<<< HEAD
    <div class="buttonGroup">
>>>>>>> 860f864 (Refactor : 로그인, 회원가입 동의 페이지 코드 수정 & 404 페이지 만듦)
=======
    <div class="buttonGroup" v-if="isChecked">
>>>>>>> 8e42007 ( Feat : 이메일 인증 제한 시간 추가)
=======
>>>>>>> e6b54fb (asdu)
=======
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
      <router-link to="/signup/teacher" class="button">
        <q-btn color="teal" label="교사용"/>
      </router-link>
      <router-link to="/signup/student" class="button">
        <q-btn color="teal" label="학생용"/>
      </router-link>
    </div>
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
    <q-scroll-area style="height: 200px; max-width: 700px;">
      <div v-for="n in 100" :key="n" class="q-py-xs">
        Lorem ipsum dolor sit amet, consectetur adipisicing
        elit, sed do eiusmod tempor incididunt ut labore et
        dolore magna aliqua.
      </div>
    </q-scroll-area>
    <!-- 여기에 체크 박스 -->
    <q-checkbox v-model="isChecked" label="위의 약관에 동의합니다" color="teal" />
    <!-- 여기에 버튼 -->
    <!-- 학생용 -->
    <router-link to="" class="button">
      <q-btn color="teal" label="SIGN UP"/>
    </router-link>
    <!-- 교사용 -->
>>>>>>> 23e74e9 (Feat : 로그인 화면 제작 완료 & 기능 구현 미완료 & 약관 동의 화면 구현)
=======
>>>>>>> 860f864 (Refactor : 로그인, 회원가입 동의 페이지 코드 수정 & 404 페이지 만듦)
=======
>>>>>>> e6b54fb (asdu)
=======
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
    <router-view></router-view>
  </div>
</template>

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 860f864 (Refactor : 로그인, 회원가입 동의 페이지 코드 수정 & 404 페이지 만듦)
=======
>>>>>>> e6b54fb (asdu)
=======
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
<style scoped>
  /* 버튼 사이즈 키우기 */
  /* 약관 가운데 정렬 */
  /* 약관 테두리 */
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> bb316aa ( Feat : 회원가입 시 입력받은 정보를 취합하는 중)
=======
>>>>>>> e6b54fb (asdu)
=======
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
  .scroll {
    height: 300px;
    max-width: 750px;
    margin-top: 30px;
    margin-bottom: 50px;
    border-color: black;
    border-width: 1px;
  }
</style>

<script>
import { ref } from '@vue/reactivity'
import useProvision from '@/components/UseProvision.vue'
import useInfo from '@/components/UseInfo.vue'
<<<<<<< HEAD
import { mapGetters } from 'vuex'

=======
import { onBeforeMount } from '@vue/runtime-core'
import {useStore} from 'vuex'
import { useRouter } from 'vue-router'
>>>>>>> c8c893f (Feat: 로그인 여부 & 사용자 여부에 따른 접근 제한)
export default {
  name: 'signupAgreeView',
  components: {
    useProvision,
    useInfo
  },
  computed: {
    ...mapGetters(['isLoggedIn'])
  },
  setup () {
    const store = useStore()
    const router = useRouter()
    let isChecked = ref(false)
    onBeforeMount(() => {
      if (store.getter.isLoggedIn) {
        router.push('/educolab')
      }
    })
    return {
      isChecked
    }
  },
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<style>

=======
>>>>>>> 860f864 (Refactor : 로그인, 회원가입 동의 페이지 코드 수정 & 404 페이지 만듦)
</style>

<script>
import { ref } from '@vue/reactivity'
import useProvision from '@/components/UseProvision.vue'
export default {
<<<<<<< HEAD
  data: function() {
    return {
      isChecked : false,
    }
  }
>>>>>>> 23e74e9 (Feat : 로그인 화면 제작 완료 & 기능 구현 미완료 & 약관 동의 화면 구현)
=======
  name: 'signupAgreeView',
  components: {
    useProvision
  },
<<<<<<< HEAD
  // setup () {
  //   let isChecked = ref(false)
  //   return isChecked
  // },
>>>>>>> 860f864 (Refactor : 로그인, 회원가입 동의 페이지 코드 수정 & 404 페이지 만듦)
=======
  setup () {
    let isChecked = ref(false)
    return {
      isChecked
    }
  },
>>>>>>> 03de9fd (Feat: 회원가입 학교 검색, 이름, 전화번호, 생년월일, 학년/반/번호)
=======
>>>>>>> e6b54fb (asdu)
=======
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
=======
  created() {
    if (this.isLoggedIn) {
      this.$router.back()
    }
  }
>>>>>>> ef40aec (버그 수정)
}
</script>