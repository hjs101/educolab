<template>
  <div class="baseStyle">
    <h3>SIGN UP</h3>
    <!-- form 부분 -->
    <q-form
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
      @submit="submitData"
=======
      @submit="onSubmit"
>>>>>>> 147871f (Feat : 회원가입 틀 제작 후 이름까지 완료 (그 이후 부분은 미완성))
=======
      @submit="signup"
>>>>>>> 03de9fd (Feat: 회원가입 학교 검색, 이름, 전화번호, 생년월일, 학년/반/번호)
=======
      @submit="submitData"
>>>>>>> 80ba160 ( Feat : 백과의 통신 (학교 검색과 회원가입은 미완료))
=======
>>>>>>> f57c6b5 ( Fix : get 방식으로 요청)
=======
>>>>>>> e6b54fb (asdu)
      class="q-gutter row"
=======
      class="q-gutter row justify-content-around"
>>>>>>> bf45305 ( Fix : 버그 수정)
    >
      <div class="col-6 offset-3 col-md-4 offset-md-4">
      <!-- 여기에 아이디, 비밀번호 입력 창 -->
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e6b54fb (asdu)
=======
      class="q-gutter row justify-content-around"
=======
    class="q-mt-md row justify-center"
>>>>>>> db26c2a (Style & Fix : 스타일 및 오류 수정)
    >
      <div class="col-6">
      <!-- 여기에 아이디, 비밀번호 입력 창 -->
<<<<<<< HEAD
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
        <login-info/>
=======
        <login-info class="q-my-md"/>
>>>>>>> db26c2a (Style & Fix : 스타일 및 오류 수정)
        <!-- 학교 검색 버튼 -->
        <search-school class="q-my-md" />
        <!-- 이름 & 전화번호 -->
<<<<<<< HEAD
        <user-name />
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e6b54fb (asdu)
=======
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
        <user-phone-number />
=======
        <user-name class="q-my-md" />
        <user-phone-number class="q-my-md" />
>>>>>>> db26c2a (Style & Fix : 스타일 및 오류 수정)
        <!-- 생년월일-->
        <user-birthday :userType="userType"  class="q-my-md"/>
        <!-- 교사와 학생에 따라 다른 항목-->
        <teacher-or-student :userType="userType" class="q-my-md" />
        <!-- 이메일 -->
        <email-confirm class="q-my-md" />
        <!-- 회원가입 버튼 -->
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        <q-btn color="primary" label="SIGN UP" @submit="submitData"/>
=======
        <login-info @to-signup="changeData"/>
        <q-input
          color="teal"
          label="이름"
          v-model="userInfo.name"
          :dense="dense"
          lazy-rules
          :rules="[ val => val && val.length > 0 || '이름을 입력해주세요']"
        />
=======
        <login-info/>
>>>>>>> 03de9fd (Feat: 회원가입 학교 검색, 이름, 전화번호, 생년월일, 학년/반/번호)
        <!-- 학교 검색 버튼 -->
        <search-school />
        <!-- 이름 & 전화번호 -->
=======
>>>>>>> 89ccfeb ( Feat: 회원 가입 기능 완료 (백 통신해서 디버깅 해야 함))
        <user-phone-number />
        <!-- 생년월일-->
        <user-birthday :userType="userType" />
        <!-- 교사와 학생에 따라 다른 항목-->
        <teacher-or-student :userType="userType" />
        <!-- 이메일 -->
        <email-confirm />
        <!-- 회원가입 버튼 -->
<<<<<<< HEAD
        <q-btn color="primary" label="SIGN UP" @submit="signup"/>
>>>>>>> 147871f (Feat : 회원가입 틀 제작 후 이름까지 완료 (그 이후 부분은 미완성))
=======
        <q-btn color="primary" label="SIGN UP" @submit="submitData"/>
>>>>>>> 89ccfeb ( Feat: 회원 가입 기능 완료 (백 통신해서 디버깅 해야 함))
=======
        <q-btn color="primary" label="SIGN UP" @click="submitData"/>
>>>>>>> f57c6b5 ( Fix : get 방식으로 요청)
=======
        <q-btn color="primary" label="SIGN UP" @click="submitData"/>
>>>>>>> e6b54fb (asdu)
=======
        <q-btn color="primary" label="SIGN UP" class="submitButton" @click="submitData"/>
>>>>>>> bf45305 ( Fix : 버그 수정)
=======
        <q-btn color="primary" label="SIGN UP" class="submitButton" @click="submitData"/>
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
=======
        <q-btn
          color="primary"
          label="SIGN UP"
          class="submitButton q-mt-sm"
          @click="submitData"/>
>>>>>>> f86710a (Feat : 비밀번호 변경 구현 완료)
      </div>
      <message-pop-up
        v-if="prompt.computedConfirm"
        message="이메일 인증을 진행해주세요"
        @reverse="prompt.confirm = false"
      />
    </q-form>
  </div>
</template>

<style>
  .submitButton {
    margin-top: 50px;
    display: block;
    margin-left: auto;
    margin-right: auto;
  }
  .buttonCenter {
  display: block;
  margin-left: auto;
  margin-right: auto;
  }
</style>

<script>
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e6b54fb (asdu)
import {useRoute} from 'vue-router'
=======
import {useRoute, useRouter} from 'vue-router'
>>>>>>> 9c886eb (Feat : 이메일 인증 부분 수정 & 아이디/비밀번호 찾기 기능 완료 & 비밀번호 변경 기능 진행 중)
=======
import {useRoute, useRouter} from 'vue-router'
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
import {useStore} from 'vuex'
import {computed, onBeforeMount, reactive} from 'vue'
import LoginInfo from '@/components/LoginInfo.vue'
import SearchSchool from '@/components/SearchSchool.vue'
import EmailConfirm from '@/components/EmailConfirm.vue'
import TeacherOrStudent from '@/components/TeacherOrStudent.vue'
import UserBirthday from '@/components/UserBirthday.vue'
import UserPhoneNumber from '@/components/UserPhoneNumber.vue'
import UserName from '@/components/UserName.vue'
import MessagePopUp from '@/components/MessagePopUp.vue'

<<<<<<< HEAD
// import { onMounted } from '@vue/runtime-core'
<<<<<<< HEAD
<<<<<<< HEAD
=======
import {reactive} from '@vue/reactivity'
=======
import {useRoute} from 'vue-router'
import {useStore} from 'vuex'
>>>>>>> 03de9fd (Feat: 회원가입 학교 검색, 이름, 전화번호, 생년월일, 학년/반/번호)
import LoginInfo from '@/components/LoginInfo.vue'
import searchSchool from '@/components/searchSchool.vue'
import EmailConfirm from '@/components/EmailConfirm.vue'
import TeacherOrStudent from '@/components/TeacherOrStudent.vue'
<<<<<<< HEAD
>>>>>>> 147871f (Feat : 회원가입 틀 제작 후 이름까지 완료 (그 이후 부분은 미완성))
=======
import UserBirthday from '@/components/UserBirthday.vue'
import UserPhoneNumber from '@/components/UserPhoneNumber.vue'
// import { onMounted } from '@vue/runtime-core'
>>>>>>> 03de9fd (Feat: 회원가입 학교 검색, 이름, 전화번호, 생년월일, 학년/반/번호)
=======
>>>>>>> e6b54fb (asdu)
=======
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
=======
>>>>>>> f86710a (Feat : 비밀번호 변경 구현 완료)
export default {
  name: "SignupView",
  components: {
    LoginInfo,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 02d99cb ( Fix : 통신 확인)
=======
>>>>>>> e6b54fb (asdu)
=======
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
    SearchSchool,
    EmailConfirm,
    TeacherOrStudent,
    UserBirthday,
    UserPhoneNumber,
    UserName,
    MessagePopUp,
  },
  setup () {
    const store = useStore()
    const route = useRoute()
    const router = useRouter()
    const userType = route.params.userType
    const prompt = reactive({
      confirm: false,
      computedConfirm: computed(() => prompt.confirm)
    })
    const submitData = () => {
      // 모든 항목이 다 채워져 있을 경우에만 회원 가입
      if (store.getters.isValidEmail) {
        store.dispatch('signup')
      } else {
        // 이메일 인증을 진행해주세요 팝업
        prompt.confirm = true
      }
    }
    onBeforeMount(() => {
      if (userType !== 'student' && userType !== 'teacher') {
        router.push('/404')
      } else {
        store.dispatch('setUserType', userType)
      }
    })
    return {
      userType,
      router,
      prompt,
      submitData
    }
  },
<<<<<<< HEAD
<<<<<<< HEAD
=======
    searchSchool,
    EmailConfirm,
    TeacherOrStudent,
    UserBirthday,
    UserPhoneNumber,
    UserName,
  },
  setup () {
    const store = useStore()
    const router = useRoute()
    const userType = router.params.userType
    const submitData = () => {
      store.dispatch('signup')
    }
    onMounted(() => {
      store.dispatch('setUserType', userType)
    })
    return {
      userType,
      router,
      submitData
    }
<<<<<<< HEAD
  }
>>>>>>> 147871f (Feat : 회원가입 틀 제작 후 이름까지 완료 (그 이후 부분은 미완성))
=======
  },
<<<<<<< HEAD
  // created () {
  //   this.mdiCalendarCursorOutline = mdiCalendarCursorOutline
  // }
>>>>>>> 03de9fd (Feat: 회원가입 학교 검색, 이름, 전화번호, 생년월일, 학년/반/번호)
=======
>>>>>>> 89ccfeb ( Feat: 회원 가입 기능 완료 (백 통신해서 디버깅 해야 함))
=======
>>>>>>> e6b54fb (asdu)
=======
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
}
</script>