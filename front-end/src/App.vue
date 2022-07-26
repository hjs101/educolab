<template>
  <div>
    <!-- 로그인된 경우-->
    <!-- <the-nav-bar/> -->
    <!-- 로그인 안 된 경우 login 페이지로 push ?? beforeEach 사용-->
    <router-view></router-view>
  </div>
</template>

<style>
  h3 {
    text-align: center;
  }
  .button {
    text-decoration: none;
  }
  .buttonGroup {
  display: flex;
  justify-content: center;
  text-align: center;
  gap: 10px;
  }
  .center {
    text-align: center;
  }

</style>

<script>
// import TheNavBar from './components/TheNavBar.vue'
// import {created} from 'vue'
export default {
  name: 'LayoutDefault',

  components: {
    // TheNavBar,
  }
}
</script>
