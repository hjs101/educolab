<template>
  <main>
    <header>CHANGE INFO</header>
    아이디
    비밀번호
    <q-btn color="primary" label="변경" />
    <search-school :school="userInfo.school" />
    <teacher-or-student />
    <user-birthday />
    <email-confirm />
    <user-phone-number />
    <q-btn color="primary" label="수정" />
    <q-btn color="primary" label="마이페이지" />
  </main>
</template>

<script>
import { useStore } from 'vuex'
import EmailConfirm from '@/components/EmailConfirm.vue'
import SearchSchool from '@/components/SearchSchool.vue'
import TeacherOrStudent from '@/components/TeacherOrStudent.vue'
import UserBirthday from '@/components/UserBirthday.vue'
import UserPhoneNumber from '@/components/UserPhoneNumber.vue'
export default {
  name: 'ChangeUserInfo',
  components: {
    SearchSchool,
    TeacherOrStudent,
    UserBirthday,
    EmailConfirm,
    UserPhoneNumber
  },
  setup() {
    const store = useStore()
    const userInfo = store.getters.getUserInfo
    return {
      userInfo
    }
  }

}
</script>