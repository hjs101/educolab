<template>
  <div class="q-mx">
    <h3>SIGN UP</h3>
    <!-- form 부분 -->
    <q-form
      class="q-gutter row justify-content-around"
    >
      <div class="col-6 offset-3 col-md-4 offset-md-4">
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
        <q-btn color="primary" label="SIGN UP" class="submitButton" @click="submitData"/>
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
import {useRoute, useRouter} from 'vue-router'
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
export default {
  name: "SignupView",
  components: {
    LoginInfo,
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
}
</script>