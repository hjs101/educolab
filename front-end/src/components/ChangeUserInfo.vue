<template>
  <main>
    <q-input
      stack-label
      label="아이디"
      v-model="user.username"
      disable />
    <q-btn color="primary" label="비밀번호 변경" />
    <search-school type="change" :schoolname="user.schoolname" />
    <teacher-or-student
      type="change"
      :userType="userInfo.userflag? 'teacher':'student'"
      :homeroomFlag="user.homeroomFlag"
      :data="user"
    />
    <user-birthday
      type="change"
      :date="user.birthday"
    />
    <user-phone-number
      type="change"
      :number="user.phone"
    />
    <email-confirm
      type="change"
      :fullEmail="user.email"
    />
    <q-btn color="primary" label="수정" @click="updateInfo"/>
    <q-btn color="primary" flat label="취소" />
    <message-pop-up
      message=""
      :reload="true"
      path=""
    />
  </main>
</template>

<script>
import { useStore } from 'vuex'
import {reactive} from 'vue'
import drf from '@/api/drf.js'
import axios from 'axios'
import EmailConfirm from '@/components/EmailConfirm.vue'
import SearchSchool from '@/components/SearchSchool.vue'
import TeacherOrStudent from '@/components/TeacherOrStudent.vue'
import UserBirthday from '@/components/UserBirthday.vue'
import UserPhoneNumber from '@/components/UserPhoneNumber.vue'
import MessagePopUp from './MessagePopUp.vue'
export default {
  name: 'ChangeUserInfo',
  components: {
    SearchSchool,
    TeacherOrStudent,
    UserBirthday,
    EmailConfirm,
    UserPhoneNumber,
    MessagePopUp
  },
  setup() {
    const store = useStore()
    const userInfo = store.getters.getUserInfo
    const user = reactive({
      name: userInfo.name,
      username: userInfo.username,
      schoolname: store.getters.currentUser.schoolname,
      email: userInfo.email,
      grade: userInfo.grade,
      classField: userInfo.class_field,
      phone: userInfo.phone_number,
      birthday: userInfo.birthday,
      subject: userInfo.subject,
      homeroomFlag: userInfo.homeroom_teacher_flag
    })
    const updateInfo = () => {
      axios({
        url: drf.myPage.main(),
        method: 'put',
        headers: store.getters.authHeader,
        data: store.getters.getUserInfo
      })
      .then(() => {
        
      })
    }
    return {
      userInfo,
      user,
      updateInfo
    }
  }

}
</script>