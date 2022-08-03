<template>
  <div>
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 64e711e (공지사항 상세페이지 버그 수)
=======
>>>>>>> e6b54fb (asdu)
    <h1>...</h1>
=======
    <div v-for="item in noticeItem" :key="item.pk">
      <h3>{{ item }}</h3>
      <h4>{{ item.teacher }}</h4>
      <p>{{ item.updated_at }}</p>
      <p>{{ item.content}}</p>
      <p>{{ item.atch_file_name }}</p>
=======
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
>>>>>>> fec931d (공지사항  상세페이지 구현)
=======
    <div class="center">
      <h3>제목 : {{ noticeItem.notice.title }}</h3>
      <p>등록일 : {{ noticeItem.notice.updated_at }}</p>
      <p>작성자 : {{ noticeItem.notice.teacher.name }}</p>
      <h4>내용 : {{ noticeItem.notice.content }}</h4>
      <div v-for="(file, index) in noticeItem.files" :key="index">
        파일이름: 
        <button @click="openFile(file.atch_file)">{{ file.atch_file_name }}</button>
        <br>
>>>>>>> 3646f0b (공지사항 파일 업로드)

      </div>
    </div>
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8ad08b5 (비밀번호  변경으로 인한 로그인 이슈)
=======
    
>>>>>>> b39710a (공지사항  수정 구현)
=======

    <button @click="updateData">수정</button>
    <button @click="deleteNotice(noticeItem.notice.id)">삭제</button>
    <br>
    <router-link to="/notice"><button>목록</button></router-link>
>>>>>>> 3646f0b (공지사항 파일 업로드)
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

<<<<<<< HEAD
</style>
=======
    <h1>공지 상세 페이지</h1>
  <router-view />
  </div>
</template>
>>>>>>> e66f000 (navbar 생성)
=======
</style>
>>>>>>> e6b54fb (asdu)
