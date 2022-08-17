<template>
  <div class="account-error-list">
    <div class="row" v-for="(errors, field) in authError" :key="field">
      {{ errors }}
      <div v-for="(error, idx) in errors" :key="idx">
        <!-- <span class="row">{{ error }}</span> -->
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'AccountErrorList',
  computed: {
    ...mapGetters(['authError'])
  },
}
</script>

<style>
  .account-error-list {
    color: red;
  }
</style>