<template>
  <div>
    <div>
      <div class="center">
        <h3>제목 : {{ noticeItem.notice.title }}</h3>
        <p>등록일 : {{ noticeItem.notice.updated_at }}</p>
        <p>작성자 : {{ noticeItem.notice.teacher.name }}</p>
        <h4>내용 : {{ noticeItem.notice.content }}</h4>
        <div v-for="(file, index) in noticeItem.files" :key="index">
          파일이름: {{ file.atch_file_name }}
          <br>
          파일경로: {{ file.atch_file }}
        </div>
      </div>

      <button @click="updateData">수정</button>
      <button @click="deleteNotice(noticeItem.notice.id)">삭제</button>
      <br>
      <router-link to="/notice"><button>목록</button></router-link>
    </div>
    
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  data() {
    const index = this.$route.params.noticePk
    return {
      // noticeItem : this.noticeItem,
      index : index
    }
  },
  computed: {
    ...mapGetters(['noticeItem'])
  },
  methods: {
    ...mapActions(['deleteNotice']),
    updateData() {
      this.$router.push({
        name: 'NoticeForm',
        params : {
          noticePk : this.index
        }
      })
    }
  }
}
</script>

<style>

</style>