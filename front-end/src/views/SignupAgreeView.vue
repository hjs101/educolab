<template>
  <div class="q-ma-md">
    <h3>SIGN UP</h3>
    <!-- 여기에 약관 동의-->
    <div class="row">
      <q-scroll-area class="col-6 offset-3 scroll">
        <use-provision />
      </q-scroll-area>
      <q-scroll-area class="col-6 offset-3 scroll">
        <use-info />
      </q-scroll-area>
      <!-- 여기에 체크 박스 -->
      <q-checkbox v-model="isChecked" label="위의 약관에 모두 동의합니다" color="teal" class="col-5 offset-5" />
      <br>
    </div>
      <!-- 여기에 버튼 -->
    <div class="buttonGroup" v-if="isChecked">
      <router-link to="/signup/teacher" class="button">
        <q-btn color="teal" label="교사용"/>
      </router-link>
      <router-link to="/signup/student" class="button">
        <q-btn color="teal" label="학생용"/>
      </router-link>
    </div>
    <router-view></router-view>
  </div>
</template>

<style scoped>
  /* 버튼 사이즈 키우기 */
  /* 약관 가운데 정렬 */
  /* 약관 테두리 */
  .scroll {
    height: 300px;
    max-width: 750px;
    margin-top: 30px;
    margin-bottom: 50px;
    border-color: black;
    border-width: 1px;
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
}
</script>