<template>
  <div class="q-ma-md">
    <h3>SIGN UP</h3>
    <!-- 여기에 약관 동의-->
<<<<<<< HEAD
<<<<<<< HEAD
    <div class="row">
      <q-scroll-area class="col-6 offset-3 scroll">
        <use-provision />
      </q-scroll-area>
      <q-scroll-area class="col-6 offset-3 scroll">
        <use-info />
      </q-scroll-area>
      <!-- 여기에 체크 박스 -->
      <q-checkbox v-model="isChecked" label="위의 약관에 모두 동의합니다" color="teal" class="col-4 offset-4" />
      <!-- 여기에 버튼 -->
      <br>
    </div>
    <div class="buttonGroup" v-if="isChecked">
=======
    <div class="row">
      <q-scroll-area style="height: 500px; max-width: 700px;" class="col-6 offset-3">
        <use-provision />
      </q-scroll-area>
      <!-- 여기에 체크 박스 -->
      <!-- <q-checkbox v-model="isChecked" label="위의 약관에 모두 동의합니다" color="teal" class="col-4 offset-4" /> -->
      <!-- 여기에 버튼 -->
      <br>
    </div>
    <div class="buttonGroup">
>>>>>>> 860f864 (Refactor : 로그인, 회원가입 동의 페이지 코드 수정 & 404 페이지 만듦)
      <router-link to="/signup/teacher" class="button">
        <q-btn color="teal" label="교사용"/>
      </router-link>
      <router-link to="/signup/student" class="button">
        <q-btn color="teal" label="학생용"/>
      </router-link>
    </div>
<<<<<<< HEAD
=======
    <q-scroll-area style="height: 200px; max-width: 700px;">
      <div v-for="n in 100" :key="n" class="q-py-xs">
        Lorem ipsum dolor sit amet, consectetur adipisicing
        elit, sed do eiusmod tempor incididunt ut labore et
        dolore magna aliqua.
      </div>
    </q-scroll-area>
    <!-- 여기에 체크 박스 -->
    <q-checkbox v-model="isChecked" label="위의 약관에 동의합니다" color="teal" />
    <!-- 여기에 버튼 -->
    <!-- 학생용 -->
    <router-link to="" class="button">
      <q-btn color="teal" label="SIGN UP"/>
    </router-link>
    <!-- 교사용 -->
>>>>>>> 23e74e9 (Feat : 로그인 화면 제작 완료 & 기능 구현 미완료 & 약관 동의 화면 구현)
=======
>>>>>>> 860f864 (Refactor : 로그인, 회원가입 동의 페이지 코드 수정 & 404 페이지 만듦)
    <router-view></router-view>
  </div>
</template>

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 860f864 (Refactor : 로그인, 회원가입 동의 페이지 코드 수정 & 404 페이지 만듦)
<style scoped>
  /* 버튼 사이즈 키우기 */
  /* 약관 가운데 정렬 */
  /* 약관 테두리 */
<<<<<<< HEAD
  .scroll {
    height: 300px;
    max-width: 700px;
    margin-top: 50px;
    margin-bottom: 50px;
  }
</style>

<script>
import { ref } from '@vue/reactivity'
import useProvision from '@/components/UseProvision.vue'
import useInfo from '@/components/UseInfo.vue'
export default {
  name: 'signupAgreeView',
  components: {
    useProvision,
    useInfo
  },
  setup () {
    let isChecked = ref(false)
    return {
      isChecked
    }
  },
=======
<style>

=======
>>>>>>> 860f864 (Refactor : 로그인, 회원가입 동의 페이지 코드 수정 & 404 페이지 만듦)
</style>

<script>
// import { ref } from '@vue/reactivity'
import useProvision from '@/components/UseProvision.vue'
export default {
<<<<<<< HEAD
  data: function() {
    return {
      isChecked : false,
    }
  }
>>>>>>> 23e74e9 (Feat : 로그인 화면 제작 완료 & 기능 구현 미완료 & 약관 동의 화면 구현)
=======
  name: 'signupAgreeView',
  components: {
    useProvision
  },
  // setup () {
  //   let isChecked = ref(false)
  //   return isChecked
  // },
>>>>>>> 860f864 (Refactor : 로그인, 회원가입 동의 페이지 코드 수정 & 404 페이지 만듦)
}
</script>