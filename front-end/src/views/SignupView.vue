<template>
  <div class="q-mx">
    <h3>SIGN UP</h3>
    <!-- form 부분 -->
    <q-form
      @submit="signup"
      class="q-gutter row"
    >
      <div class="input col-8 offset-2 col-md-2 offset-md-6">
      <!-- 여기에 아이디, 비밀번호 입력 창 -->
        <login-info/>
        <!-- 학교 검색 버튼 -->
        <search-school />
        <!-- 이름 & 전화번호 -->
        <user-phone-number />
        <!-- 생년월일-->
        <user-birthday :userType="userType" />
        <!-- 교사와 학생에 따라 다른 항목-->
        <teacher-or-student :userType="userType" />
        <!-- 이메일 -->
        <email-confirm />
        <!-- 회원가입 버튼 -->
        <q-btn color="primary" label="SIGN UP" @submit="signup"/>
      </div>
    </q-form>
  </div>
</template>

<script>
import {useRoute} from 'vue-router'
import {useStore} from 'vuex'
import LoginInfo from '@/components/LoginInfo.vue'
import searchSchool from '@/components/searchSchool.vue'
import EmailConfirm from '@/components/EmailConfirm.vue'
import TeacherOrStudent from '@/components/TeacherOrStudent.vue'
import UserBirthday from '@/components/UserBirthday.vue'
import UserPhoneNumber from '@/components/UserPhoneNumber.vue'
// import { onMounted } from '@vue/runtime-core'
export default {
  name: "SignupView",
  components: {
    LoginInfo,
    searchSchool,
    EmailConfirm,
    TeacherOrStudent,
    UserBirthday,
    UserPhoneNumber,
  },
  setup () {
    // 교사와 학생 필수 정보만 보내기 (선택 정보는 X)
    const store = useStore()
    const router = useRoute()
    const userType = router.params.userType
    // const moveTo404 = (() => {
    //   if (userType !=='student' && userType !== 'teacher') {
    //     router.push({name: 'notFound'})
    //   }
    // })
    // onMounted(() => {
    //   moveTo404()
    // })
    // 비밀번호1, 2 같이 보내기
    const signup = () => {
      console.log(store)
      // userInfo 보내기
      // console.log(this.userData)
    }
    return {
      userType,
      signup,
      router,
    }
  },
  // created () {
  //   this.mdiCalendarCursorOutline = mdiCalendarCursorOutline
  // }
}
</script>