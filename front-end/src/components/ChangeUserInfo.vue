<template>
  <main>
    <q-input
      stack-label
      label="아이디"
      v-model="user.username"
      disable />
      <a href="/change/password" class="button">
        <q-btn color="primary" label="비밀번호 변경" />
      </a>
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
    <!-- 취소 시 어떤 페이지로 이동할 것인가 -->
    <q-btn color="primary" flat label="취소" />
    <message-pop-up
      v-if="confirm.presentState"
      :message="confirm.message"
      :reload="true"
      path="/educolab"
    />
  </main>
</template>

<script>
import { useStore } from 'vuex'
import {computed, reactive} from 'vue'
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
    const userInfo = computed(() => store.getters.getUserInfo)
    const user = reactive({
      name: userInfo.value.name,
      username: userInfo.value.username,
      schoolname: store.getters.currentUser.schoolname,
      email: userInfo.value.email,
      grade: userInfo.value.grade,
      classField: userInfo.value.class_field,
      phone: userInfo.value.phone_number,
      birthday: userInfo.value.birthday,
      subject: userInfo.value.subject,
      homeroomFlag: userInfo.value.homeroom_teacher_flag
    })
    const confirm = reactive({
      prompt: false,
      message: '',
      presentState: computed(() => confirm.prompt)
    })
    const updateInfo = () => {
      const data= store.getters.getUserInfo
      console.log(data)
      axios({
        url: drf.myPage.main(),
        method: 'put',
        headers: store.getters.authHeader,
        data,
      })
      .then(() => {
        confirm.message = "수정되었습니다"
      })
      .catch(() => {
        confirm.message = "오류가 발생했습니다"
      })
      .finally(() => {
        confirm.prompt = true
      })
    }
    return {
      userInfo,
      user,
      confirm,
      updateInfo
    }
  }

}
</script>