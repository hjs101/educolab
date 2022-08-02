<template>
  <div>
    <div v-for="item in noticeItem" :key="item.pk">
      <h3>{{ item }}</h3>
      <h4>{{ item.teacher }}</h4>
      <p>{{ item.updated_at }}</p>
      <p>{{ item.content}}</p>
      <p>{{ item.atch_file_name }}</p>

      <button>수정</button>
      <button>삭제</button>
      <button>목록</button>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  data() {
  },
  computed: {
    ...mapGetters(['noticeItem'])
  },
  method : {
  }
}
</script>

<style>

</style>