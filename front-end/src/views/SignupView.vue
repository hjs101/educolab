<template>
  <div class="q-mx">
    <h3>SIGN UP</h3>
    <!-- form 부분 -->
    <q-form
      @submit="submitData"
      class="q-gutter row"
    >
      <div class="input col-8 offset-2 col-md-2 offset-md-6">
      <!-- 여기에 아이디, 비밀번호 입력 창 -->
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
      </div>
    </q-form>
  </div>
</template>

<script>
import {useRoute} from 'vue-router'
import {useStore} from 'vuex'
import {onMounted} from 'vue'
import LoginInfo from '@/components/LoginInfo.vue'
import searchSchool from '@/components/searchSchool.vue'
import EmailConfirm from '@/components/EmailConfirm.vue'
import TeacherOrStudent from '@/components/TeacherOrStudent.vue'
import UserBirthday from '@/components/UserBirthday.vue'
import UserPhoneNumber from '@/components/UserPhoneNumber.vue'
import UserName from '@/components/UserName.vue'

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
}
</script>