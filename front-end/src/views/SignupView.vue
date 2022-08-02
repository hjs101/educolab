<template>
  <div class="q-mx">
    <h3>SIGN UP</h3>
    <!-- form 부분 -->
    <q-form
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
        <login-info/>
        <!-- 학교 검색 버튼 -->
        <search-school />
        <!-- 이름 & 전화번호 -->
        <user-name />
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e6b54fb (asdu)
        <user-phone-number />
        <!-- 생년월일-->
        <user-birthday :userType="userType" />
        <!-- 교사와 학생에 따라 다른 항목-->
        <teacher-or-student :userType="userType" />
        <!-- 이메일 -->
        <email-confirm />
        <!-- 회원가입 버튼 -->
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
      </div>
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
=======
>>>>>>> e6b54fb (asdu)
import {useRoute} from 'vue-router'
=======
import {useRoute, useRouter} from 'vue-router'
>>>>>>> 9c886eb (Feat : 이메일 인증 부분 수정 & 아이디/비밀번호 찾기 기능 완료 & 비밀번호 변경 기능 진행 중)
import {useStore} from 'vuex'
import {onBeforeMount} from 'vue'
import LoginInfo from '@/components/LoginInfo.vue'
import SearchSchool from '@/components/SearchSchool.vue'
import EmailConfirm from '@/components/EmailConfirm.vue'
import TeacherOrStudent from '@/components/TeacherOrStudent.vue'
import UserBirthday from '@/components/UserBirthday.vue'
import UserPhoneNumber from '@/components/UserPhoneNumber.vue'
import UserName from '@/components/UserName.vue'

// import { onMounted } from '@vue/runtime-core'
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
export default {
  name: "SignupView",
  components: {
    LoginInfo,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 02d99cb ( Fix : 통신 확인)
=======
>>>>>>> e6b54fb (asdu)
    SearchSchool,
    EmailConfirm,
    TeacherOrStudent,
    UserBirthday,
    UserPhoneNumber,
    UserName,
  },
  setup () {
    const store = useStore()
    const route = useRoute()
    const router = useRouter()
    const userType = route.params.userType
    const submitData = () => {
      store.dispatch('signup')
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
      submitData
    }
  },
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
}
</script>