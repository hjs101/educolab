<template>
<<<<<<< HEAD
<<<<<<< HEAD
  <div>
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
    <div class="center">
=======
    <div class="baseStyle">
>>>>>>> d127577 (기능별 메인 페이지 구성)
      <h3>제목 : {{ noticeItem.notice.title }}</h3>
      <p>등록일 : {{ noticeItem.notice.updated_at }}</p>
      <p>작성자 : {{ noticeItem.notice.teacher.name }}</p>
      <h4>내용 : {{ noticeItem.notice.content }}</h4>
      <div v-for="(file, index) in noticeItem.files" :key="index">
        파일이름: 
        <button @click="openFile(file.atch_file)">{{ file.atch_file_name }}</button>
        <br>
<<<<<<< HEAD
>>>>>>> 3646f0b (공지사항 파일 업로드)
=======
  <div class="row justify-center q-my-xl">
=======
  <div class="BASE">
>>>>>>> ef40aec (버그 수정)
    <div>
      <div class="q-mb-md">
        <div class="row justify-between items-center">
          <div class="row start items-center">
            <p class="title-size">[{{ noticeDetail.notice.classification }}]</p>
            <p class="title-size">{{ noticeDetail.notice.title }}</p>
          </div>
        </div>
        <div class="row justify-between">
          <p class="item-size text-start q-pl-sm text-grey-13">{{ noticeDetail.notice.teacher.name }}</p>
          <p class="item-size text-right q-px-md">{{ timeInfo(noticeDetail.notice.updated_at) }}</p>
        </div>
<<<<<<< HEAD
        <p class="item-size text-start q-pl-sm text-grey-13">{{ noticeDetail.notice.teacher.name }}</p>
<<<<<<< HEAD
>>>>>>> 38a5ff1 (공지사항  수정 해결)
=======
        <hr>
>>>>>>> 7f2a492 (설문조사  sass)
=======
      </div>
>>>>>>> 61e042d (설문조사  통계 sass)

        <div class="row justify-center">
          <q-card class="bord">
            <q-card-section>
              <p class="content-size bg-white" style="min-height:500px">{{ noticeDetail.notice.content }}</p>
            </q-card-section>
          </q-card>
        </div>
      <hr>
    
      <div class="row q-py-sm q-pl-sm">
        <p class="text-size text-grey-13 q-pb-sm">첨부파일 ({{ noticeDetail.files.length }}) </p> 
        <div v-for="file in noticeDetail.files" :key="file">
          <q-btn @click="openFile(file.atch_file)" color="grey-12" class="text-black">
          <q-icon name="mdi-paperclip"/>
          {{ file.atch_file_name }}
          </q-btn>
        </div> 
      </div>
<<<<<<< HEAD
    </div>
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8ad08b5 (비밀번호  변경으로 인한 로그인 이슈)
=======
    
>>>>>>> b39710a (공지사항  수정 구현)
=======
=======

      </div>
    </div>
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)

    <button @click="updateData">수정</button>
    <button @click="deleteNotice(noticeItem.notice.id)">삭제</button>
    <br>
    <router-link to="/notice"><button>목록</button></router-link>
<<<<<<< HEAD
>>>>>>> 3646f0b (공지사항 파일 업로드)
=======
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
=======
      <hr>

      <div class="row justify-center q-mt-xl q-gutter-md">
        <q-btn class="text-size q-px-xl q-py-md" @click="deleteNotice(noticePk)" color="red-7">삭제</q-btn>
        <q-btn class="text-size q-px-xl q-py-md" @click="updateNotice(noticePk)" color="blue-7">수정</q-btn>
      </div>

      <div class="btn-mag row justify-center">
        <q-btn @click="goNotice" class="text-size q-px-xl q-py-md" color="grey-8" label="목록" />
      </div> 
    </div>  
>>>>>>> 38a5ff1 (공지사항  수정 해결)
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import { ref } from 'vue'

export default {
  setup() {
    return {
      model: ref(null)
    }
  },
  data() {
    return {
      noticePk : this.$route.params.noticePk
    }
  },
  computed: {
    ...mapGetters(['noticeDetail', 'isLoggedIn'])
  },
  methods: {
    ...mapActions(['deleteNotice', 'getNoticeDetail']),
    timeInfo(time) {
      const d = new Date(time)
      return d.getFullYear() + ". " + (d.getMonth()+1) + ". " + d.getDate()
    },
    updateData(noticePk) {
      this.$router.push({name: 'NoticeCreate', params : {noticePk : noticePk}})
    },
    openFile(url) {
      window.open('https://i7c102.p.ssafy.io/'+ url)
    },
    goNotice() {
      this.$router.push({name:'Notice'})
    },
    updateNotice(noticePk) {
      this.$router.push({name:'NoticeCreate', params:{ noticePk: noticePk}})
    }
  },
  created() {
    if (!this.isLoggedIn) {
      this.$router.push('/educolab/login/')
    } else {
      this.getNoticeDetail(this.noticePk)
    }
  }
}
</script>

<<<<<<< HEAD
<style>

<<<<<<< HEAD
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
=======
</style>
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
=======
<style scoped>
  .title-size {
    font-size : 3vmin;
  }
  .content-size {
    font-size : 2.5vmin;
  }
  .item-size {
    font-size: 2vmin;
  }
  .my-card {
    width: 70%
  }
  p {
    margin: 0;
  }
  h3 {
    margin: 0;
  }
  .notice_form {
    width: 60%;
  }
  .color1 {
    color: #FF9966;
  }
  .text-size {
    font-size: 1rem;
  }
  .bord-bt {
    border-bottom: 1px solid #99DFF9;
  }
  .btn-mag {
    margin-top: 100px;
  }
<<<<<<< HEAD
</style>
>>>>>>> 38a5ff1 (공지사항  수정 해결)
=======
  .bord {
    border: 1px solid ;
  }
</style>
>>>>>>> 7f2a492 (설문조사  sass)
