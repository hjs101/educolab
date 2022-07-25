<template>
  <div class="q-ma-md">
    <h3>SIGN UP</h3>
    <!-- 여기에 약관 동의-->
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
    <router-view></router-view>
  </div>
</template>

<style>

</style>

<script>
export default {
  data: function() {
    return {
      isChecked : false,
    }
  }
}
</script>