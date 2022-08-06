<template>
  <div class="q-pa-lg flex flex-center">
    <q-pagination
      v-model="current"
      color="primary"
      :max="limit"
      :max-pages="6"
      :boundary-links="limit>10"
      direction-links
      @change="changePage"
    />
  </div>
</template>

<script>
// import { computed } from '@vue/runtime-core'
import {ref} from 'vue'
export default {
  name: 'ThePagination',
  props: {
    limit: Number,
  },
  emits: [
    'changePage'
  ],
  setup(props,{emit}) {
    const current = ref(1)
    const changePage = () => {
      emit('change-page', current.value)
    }
    return {
      current,
      changePage
    }
  }
}
</script>