<template>
  <div class="q-pa-lg flex flex-center">
    <q-pagination
      v-model="current"
      color="primary"
      :max="limit"
      :max-pages="6"
      :boundary-links="limit>6"
      direction-links
      @click="changePage"
    />
  </div>
</template>

<script>
import {ref} from 'vue'
export default {
  name: 'ThePagination',
  props: {
    limit: Number,
    target: String,
  },
  setup(props,{emit}) {
    const current = ref(1)
    const changePage = () => {
      emit('change-page', current.value, props.target)
    }
    return {
      current,
      changePage
    }
  }
}
</script>