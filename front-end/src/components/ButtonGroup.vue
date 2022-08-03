<template>
  <div class="buttonGroup">
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