<template>
  <div class="baseStyle" v-if="!emptyNotice">
    <h4 class="text-center">공지사항</h4>
    <hr>
    <div class="row justify-end q-mt-lg">
      <q-btn v-if="currentUser.userflag" @click="noticeCreate" class="text-size q-mx-lg q-py-sm" 
      color="blue-6" label="글 쓰기" />
    </div>

    <div class="q-pa-md">
      <q-markup-table class="notice-full">
        <thead>
          <tr class="text-center text-size">
            <th class="text-size">번호</th>
            <th class="text-size">분류</th>
            <th class="text-size">제목</th>
            <th class="text-size">작성자</th>
            <th class="text-size">등록일</th>
            <th class="text-size">조회수</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(notice, index) in notice2?.slice((page-1)*10, page*10)" :key="index"
          class="text-center">
            <td class="text-size">{{ index+1+((page-1)*10) }}</td>

            <td v-if="notice.classification === '변경'" class="text-size text-pink-13">{{ notice.classification }}</td>
            <td v-else-if="notice.classification === '공지'" class="text-size text-indigo-13">{{ notice.classification }}</td>
            <td v-else-if="notice.classification === '행사'" class="text-size text-green-13">{{ notice.classification }}</td>

            <td @click="noticeDetail(notice.pk)" class="cursor-pointer text-left text-size">{{ notice.title }}</td>
            <td class="text-size">{{ notice.teacher.name }}</td>
            <td class="text-size">{{ timeInfo(notice.created_at) }}</td>
            <td class="text-size">{{ notice.views }}</td>
          </tr>
        </tbody>
      </q-markup-table>

      <q-markup-table class="notice-small">
        <thead>
          <tr>
            <th class="text-center text-size">분류</th>
            <th class="text-center text-size">제목</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(notice, index) in notice2.slice((page-1)*10, page*10)" :key="index">
            <td v-if="notice.classification === '변경'" class="text-size text-center text-pink-13">{{ notice.classification }}</td>
            <td v-else-if="notice.classification === '공지'" class="text-size text-center text-indigo-13">{{ notice.classification }}</td>
            <td v-else-if="notice.classification === '행사'" class="text-size text-center text-green-13">{{ notice.classification }}</td>

            <td @click="noticeDetail(notice.pk)" class="cursor-pointer text-size">{{ notice.title }}</td>
          </tr>
        </tbody>
      </q-markup-table>
    </div>

    <div>
      <the-pagination v-if="noticeLenth" :limit="noticeLenth" @change-page="changePage">
      </the-pagination>
    </div>   

  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import { ref } from 'vue'
import ThePagination from '@/components/ThePagination.vue'
import {isEmpty} from 'lodash'

export default {
  name: "NoticeView",
  components: {ThePagination},
  setup() {
    let page = ref(1)
    const changePage = (value) => {
      page.value = value
    }
    return {
      page,
      changePage
    }
  },
  computed: {
    ...mapGetters(['notice2', 'noticeLenth', 'isLoggedIn', 'currentUser']),
    emptyNotice() {
      return isEmpty(this.notice2)
    }
  },
  methods: {
    ...mapActions(['noticeList']),
    timeInfo(time) {
      const d = new Date(time)
      return d.getFullYear() + ". " + (d.getMonth()+1) + ". " + d.getDate()
    },
    noticeCreate() {
      this.$router.push({name : 'NoticeCreate'})
    },
    noticeDetail(noticePk) {
      this.$router.push({name: 'NoticeDetail', params:{ noticePk:noticePk }})
    }
  },
  created() {
    if (!this.isLoggedIn) {
      this.$router.push('/educolab/login/')
    } else {
      this.noticeList()
    }
  }
}

</script>

<style scoped>
  .text-size{ font-size: 1rem; }
  .notice-small { display: none; }

  @media screen and (max-width: 950px) {
    .notice-full {
      display: none;
    }
    .notice-small {
      display: block;
    }
  }
</style>