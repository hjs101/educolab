<template>
  <div class="noticeDetailStyle">
    <h4>공지사항 상세</h4>
      <hr>
      <div class="q-my-md">
        <div class="row justify-between items-center">
          <div class="row start items-center">
            <p class="title-size">[{{ noticeDetail.notice?.classification }}]</p>
            <p class="title-size">{{ noticeDetail.notice?.title }}</p>
          </div>
        </div>
        <div class="row justify-between">
          <p class="item-size text-start q-pl-sm text-grey-13">{{ noticeDetail.notice?.teacher.name }}</p>
          <p class="item-size text-right q-px-md">{{ timeInfo(noticeDetail.notice?.updated_at) }}</p>
        </div>
      </div>

        <div>
          <q-card class="bord">
            <q-card-section>
              <p v-html="content" class="content-size bg-white" style="min-height:500px"></p>
            </q-card-section>
          </q-card>
        </div>
      <hr>
    
      <div class="q-mt-md q-py-sm q-pl-sm">
        <p class="text-size text-grey-13 q-pb-sm">첨부파일 ({{ noticeDetail.files.length }}) </p> 
        <div v-for="file in noticeDetail.files" :key="file">
          <q-btn @click="openFile(file.atch_file)" color="grey-12" class="text-black">
          <q-icon name="mdi-paperclip"/>
          {{ file.atch_file_name }}
          </q-btn>
        </div> 
      </div>
      <hr>

      <div class="row justify-center q-mt-xl q-gutter-md">
        <q-btn v-if="currentUser.userflag" class="text-size q-px-xl q-py-md" @click="deleteNotice(noticePk)" color="red-7">삭제</q-btn>
        <q-btn v-if="currentUser.userflag" class="text-size q-px-xl q-py-md" @click="updateNotice(noticePk)" color="blue-7">수정</q-btn>
      </div>

      <div class="btn-mag row justify-center">
        <q-btn @click="goNotice" class="text-size q-px-xl q-py-md" color="grey-8" label="목록" />
      </div> 

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
    ...mapGetters(['noticeDetail', 'isLoggedIn', 'currentUser']),
    content() {
      return this.noticeDetail.notice?.content.split('\n').join('<br>')
    }
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

<style scoped>
  .noticeDetailStyle {
    width: 60%;
    margin: auto;
    min-width: 450px;
    height: 1200px;
  }
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
  .bord {
    border: 1px solid ;
  }
</style>