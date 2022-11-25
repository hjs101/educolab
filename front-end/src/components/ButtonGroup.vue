<template>
  <div class="buttonGroup">
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