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
<<<<<<< HEAD
<<<<<<< HEAD
=======
      size="20px"
>>>>>>> 38a5ff1 (공지사항  수정 해결)
=======
      size="17px"
>>>>>>> db26c2a (Style & Fix : 스타일 및 오류 수정)
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