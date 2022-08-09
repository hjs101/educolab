<template>
  <div id="notice" class="center">
    <h1>공지사항</h1>
    <router-link to="/notice/create"><button>글쓰기</button></router-link>
    <table class="center">
      <thead>
        <tr>
          <th>글 번호</th>
          <th>분류</th>
          <th>제목</th>
          <th>작성자</th>
          <th>등록일</th>
          <th>조회수</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="notice in notice2" :key="notice.id">
          <td>{{ notice.pk }}</td>  
          <td>{{ notice.classification }}</td>
          <router-link :to="{ name: 'NoticeDetail', params: {noticePk: `${notice.pk}`}}">
            <td @click="noticeDetail(notice.pk)">{{ notice.title }}</td>
          </router-link>
          <td>{{ notice.teacher.name }}</td>
          <td>{{ timeInfo(notice.updated_at) }}</td>
          <td>{{ notice.views }}</td>
        </tr>
      </tbody>
    </table>
    <!-- <div v-if="notice2">
      <div v-for="notice in notice2"
      :key="notice.pk">>
        {{ notice.title}}
      </div>
    </div> -->


  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
// import NoticeItem from '@/components/NoticeItem.vue'

export default {
  name: "NoticeView",
  data() {
    return {
      // content: noticeList.Content,
      // searchTitle: '',
      // searchNoticeList : [],
    }
  },
  // components: {
  //   NoticeItem
  // },
  computed: {
    ...mapGetters(['notice2', 'noticeItem'])
  },
  methods: {
    ...mapActions(['noticeList', 'noticeDetail']),
    timeInfo(time) {
      const d = new Date(time)
      return d.getFullYear() + ". " + (d.getMonth()+1) + ". " + d.getDate()
    },
    // rowClicked(row) {
    //   this.$router.push({
    //     path: `/board/detail/${row.id}`
    //   })
    // }
  },
  mounted() {
    this.noticeList()
  }
}

</script>

<style>
  #notice {
    margin: auto;
    width: 80%;
    font-family: "jooa";
  }
  .searchWrap{border-radius:5px; text-align:center; padding:20px 0; margin-bottom:10px;}
  .tbList th{border-top:1px solid #888;}
	.tbList th, .tbList td{border-bottom:1px solid #eee; padding:5px 0;}
	.tbList td.txt_left{text-align:left;}
  .btn{margin-bottom:40px;}
</style>