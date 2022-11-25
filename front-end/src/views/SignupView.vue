<template>
  <div class="q-mx">
    <h3>SIGN UP</h3>
    <!-- form 부분 -->
    <q-form
<<<<<<< HEAD
      @submit="submitData"
=======
      @submit="onSubmit"
>>>>>>> 147871f (Feat : 회원가입 틀 제작 후 이름까지 완료 (그 이후 부분은 미완성))
      class="q-gutter row"
    >
      <div class="input col-8 offset-2 col-md-2 offset-md-6">
      <!-- 여기에 아이디, 비밀번호 입력 창 -->
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
        <!-- 학교 검색 버튼 -->
        <search-school />
        <!-- 교사와 학생에 따라 다른 항목 (파라미터 넘겨주기) -->
        <teacher-or-student :userType="$route.params" />
        <!-- 생년월일 (두 창 연결해야 함) -->
        <q-input
          color="teal"
          label="생년월일"
          lazy-rules
          :rules="[ val => val && val.length > 0 || '생년월일을 입력해주세요']"
          disable
        />
        <q-date
          v-model="birthday"
          minimal
          default-year-month="1988/01"
        />
        <!-- 이메일 -->
        <email-confirm />
        <!-- 전화번호 -->
        <q-input
          color="teal"
          label="전화번호"
          v-model="userInfo.phoneNumber"
          lazy-rules
          :rules="[ val => val && val.length > 0 || '전화번호를 입력해주세요']"
        />
        <!-- 회원가입 버튼 -->
        <q-btn color="primary" label="SIGN UP" @submit="signup"/>
>>>>>>> 147871f (Feat : 회원가입 틀 제작 후 이름까지 완료 (그 이후 부분은 미완성))
      </div>
    </q-form>
  </div>
</template>

<script>
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
import LoginInfo from '@/components/LoginInfo.vue'
import searchSchool from '@/components/searchSchool.vue'
import EmailConfirm from '@/components/EmailConfirm.vue'
import TeacherOrStudent from '@/components/TeacherOrStudent.vue'
>>>>>>> 147871f (Feat : 회원가입 틀 제작 후 이름까지 완료 (그 이후 부분은 미완성))
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
  },
  // emit: [
  //   school,
  //   schoolName
  // ],
  setup () {
    // 교사와 학생 필수 정보만 보내기 (선택 정보는 X)
    // options 나중에 수정할 수도 있음
    // 비밀번호1, 2 같이 보내기
    const userInfo = reactive({
      username: '',
      password1: '',
      password2: '',
      name: '',
      school: 0, // code
      subject: '',
      grade: null,
      classField: 0,
      phoneNumber: '',
      birthday: 0,
      email: '',
    })
    const signup = () => {
      // userInfo 보내기
      // console.log(this.userData)
    }
    const changeData = (data) => {
      userInfo.username = data.username
      userInfo.password1 = data.password1
      userInfo.password2 = data.password2
    }
    return {
      userInfo,
      signup,
      changeData
    }
  }
>>>>>>> 147871f (Feat : 회원가입 틀 제작 후 이름까지 완료 (그 이후 부분은 미완성))
}
</script>