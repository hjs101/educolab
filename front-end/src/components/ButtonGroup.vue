<template>
  <div class="buttonGroup">
    <a href="/signup" class="button" v-if="currentUrl !== 'signup'">
      <q-btn color="primary" label="SIGN UP" v-close-popup/>
    </a>
    <a href="/" class="button" v-if="currentUrl !== 'login'">
      <q-btn color="teal" label="LOG IN" v-close-popup/>
    </a>
    <a href="/find/id" class="button" v-if="currentUrl !== 'findId'">
      <q-btn color="amber" label="FIND ID" />
    </a>
    <a href="/find/password" class="button" v-if="currentUrl !== 'findPw'">
      <q-btn color="light" text-color="black" label="FIND PW" v-close-popup />
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