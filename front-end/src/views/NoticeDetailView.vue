<template>
  <div>
    <div class="center">
      <h3>제목 : {{ noticeItem.notice.title }}</h3>
      <p>등록일 : {{ noticeItem.notice.updated_at }}</p>
      <p>작성자 : {{ noticeItem.notice.teacher.name }}</p>
      <h4>내용 : {{ noticeItem.notice.content }}</h4>
      <div v-for="(file, index) in noticeItem.files" :key="index">
        파일이름: 
        <button @click="openFile(file.atch_file)">{{ file.atch_file_name }}</button>
        <br>

      </div>
    </div>

    <button @click="updateData">수정</button>
    <button @click="deleteNotice(noticeItem.notice.id)">삭제</button>
    <br>
    <router-link to="/notice"><button>목록</button></router-link>
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
    },
    openFile(url) {
      window.open('http://127.0.0.1:8000'+ url)
    }
  }
}
</script>

<style>

</style>