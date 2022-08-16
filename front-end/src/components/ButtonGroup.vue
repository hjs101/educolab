<template>
  <div class="buttonGroup">
<<<<<<< HEAD
    <a href="/signup" class="button" v-if="currentUrl !== 'signup'">
      <q-btn color="primary" class="text-size" label="SIGN UP" v-close-popup />
    </a>
    <a href="/" class="button" v-if="currentUrl !== 'login'">
      <q-btn color="teal" class="text-size" label="LOG IN" v-close-popup/>
    </a>
    <a href="/find/id" class="button" v-if="currentUrl !== 'findId'">
      <q-btn color="amber" class="text-size" label="FIND ID" />
    </a>
    <a href="/find/password" class="button" v-if="currentUrl !== 'findPw'">
      <q-btn color="light"  class="text-size" text-color="black" label="FIND PW" v-close-popup />
    </a>
=======
    <router-link to="/signup" class="button" v-if="currentUrl !== 'signup'">
      <q-btn color="primary" label="SIGN UP" v-close-popup/>
    </router-link>
    <router-link to="/" class="button" v-if="currentUrl !== 'login'">
      <q-btn color="teal" label="LOG IN" v-close-popup/>
    </router-link>
    <router-link to="/find/id" class="button" v-if="currentUrl !== 'findId'">
      <q-btn color="amber" label="FIND ID" />
    </router-link>
    <router-link to="/find/password" class="button" v-if="currentUrl !== 'findPw'">
      <q-btn color="light" text-color="black" label="FIND PW" v-close-popup />
    </router-link>
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
  </div>
</template>

<script>
export default {
  name: 'ButtonGroup',
  props: {
    currentUrl: String,
  },
}
</script>

<style scoped>
  .text-size {
    font-size: 1rem;
  }
</style>