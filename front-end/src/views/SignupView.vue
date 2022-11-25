<template>
  <div class="baseStyle">
    <h3>SIGN UP</h3>
    <!-- form 부분 -->
    <q-form
    class="q-mt-md row justify-center"
    >
      <div class="col-6">
      <!-- 여기에 아이디, 비밀번호 입력 창 -->
        <login-info class="q-my-md"/>
        <!-- 학교 검색 버튼 -->
        <search-school class="q-my-md" />
        <!-- 이름 & 전화번호 -->
        <user-name class="q-my-md" />
        <user-phone-number class="q-my-md" />
        <!-- 생년월일-->
        <user-birthday :userType="userType"  class="q-my-md"/>
        <!-- 교사와 학생에 따라 다른 항목-->
        <teacher-or-student :userType="userType" class="q-my-md" />
        <!-- 이메일 -->
        <email-confirm class="q-my-md" />
        <!-- 회원가입 버튼 -->
        <q-btn
          color="primary"
          label="SIGN UP"
          class="submitButton q-mt-sm"
          @click="submitData"/>
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
import {useRoute, useRouter} from 'vue-router'
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
      if (store.getters.isLoggedIn) {
        router.push('/educolab')
      } else if (userType !== 'student' && userType !== 'teacher') {
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
}
</script>