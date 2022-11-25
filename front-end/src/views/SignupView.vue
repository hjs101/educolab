<template>
  <div class="q-mx">
    <h3>SIGN UP</h3>
    <!-- form 부분 -->
    <q-form
<<<<<<< HEAD
<<<<<<< HEAD
      @submit="submitData"
=======
      @submit="onSubmit"
>>>>>>> 147871f (Feat : 회원가입 틀 제작 후 이름까지 완료 (그 이후 부분은 미완성))
=======
      @submit="signup"
>>>>>>> 03de9fd (Feat: 회원가입 학교 검색, 이름, 전화번호, 생년월일, 학년/반/번호)
      class="q-gutter row"
    >
      <div class="input col-8 offset-2 col-md-2 offset-md-6">
      <!-- 여기에 아이디, 비밀번호 입력 창 -->
<<<<<<< HEAD
<<<<<<< HEAD
        <login-info/>
        <!-- 학교 검색 버튼 -->
        <search-school />
        <!-- 이름 & 전화번호 -->
        <user-name />
        <user-phone-number />
        <!-- 생년월일-->
        <user-birthday :userType="userType" />
        <!-- 교사와 학생에 따라 다른 항목-->
        <teacher-or-student :userType="userType" />
        <!-- 이메일 -->
        <email-confirm />
        <!-- 회원가입 버튼 -->
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
        <user-phone-number />
        <!-- 생년월일-->
        <user-birthday :userType="userType" />
        <!-- 교사와 학생에 따라 다른 항목-->
        <teacher-or-student :userType="userType" />
        <!-- 이메일 -->
        <email-confirm />
        <!-- 회원가입 버튼 -->
        <q-btn color="primary" label="SIGN UP" @submit="signup"/>
>>>>>>> 147871f (Feat : 회원가입 틀 제작 후 이름까지 완료 (그 이후 부분은 미완성))
      </div>
    </q-form>
  </div>
</template>

<script>
<<<<<<< HEAD
<<<<<<< HEAD
import {useRoute} from 'vue-router'
import {useStore} from 'vuex'
import {onMounted} from 'vue'
import LoginInfo from '@/components/LoginInfo.vue'
import SearchSchool from '@/components/SearchSchool.vue'
import EmailConfirm from '@/components/EmailConfirm.vue'
import TeacherOrStudent from '@/components/TeacherOrStudent.vue'
import UserBirthday from '@/components/UserBirthday.vue'
import UserPhoneNumber from '@/components/UserPhoneNumber.vue'
import UserName from '@/components/UserName.vue'

// import { onMounted } from '@vue/runtime-core'
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
export default {
  name: "SignupView",
  components: {
    LoginInfo,
<<<<<<< HEAD
    SearchSchool,
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
  },
=======
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
<<<<<<< HEAD
  }
>>>>>>> 147871f (Feat : 회원가입 틀 제작 후 이름까지 완료 (그 이후 부분은 미완성))
=======
  },
  // created () {
  //   this.mdiCalendarCursorOutline = mdiCalendarCursorOutline
  // }
>>>>>>> 03de9fd (Feat: 회원가입 학교 검색, 이름, 전화번호, 생년월일, 학년/반/번호)
}
</script>