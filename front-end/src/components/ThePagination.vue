<template>
  <div class="q-pa-lg flex flex-center">
    <q-pagination
      v-model="current"
      color="primary"
      :max="10"
      :max-pages="6"
      boundary-links
      direction-links
    />
  </div>
</template>

<script>
// import { computed } from '@vue/runtime-core'
import {ref} from 'vue'
export default {
  name: 'ThePagination',
  props: {
  },
  setup() {
    return {
      current: ref(1)
    }
  }
}
</script>