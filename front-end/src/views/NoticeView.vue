<template>
  <div>
    <!-- <h2>공지사항 메인 페이지(교사)</h2>
    <input type="search" name="" id="" v-model="searchTitle">
    <button for="searchTitle" @click="searchNotice">검색</button>
    <tr :key="search.content_id" v-for="search in searchNoticeList">
      <td>{{ search.content_id }}</td>
      <td>{{ search.title }}</td>
      <td>{{ search.created_at }}</td>
      <td>{{ search.user_id }}</td> 
    </tr>
    
    <router-link to="/notice/create"><button>글쓰기</button></router-link> -->
    <!-- <button @click="notice"></button> -->
    <h1>공지사항 메인 페이지</h1>
    <div v-if="notice2">
      <div v-for="notice in notice2"
      :key="notice.pk">>
        {{ notice.title}}
      </div>
    </div>


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
    ...mapGetters(['notice2'])
  },
  methods: {
    ...mapActions(['noticeList']),
  },
  mounted() {
    this.noticeList()
  }
}

</script>

<style>
  .searchWrap{border-radius:5px; text-align:center; padding:20px 0; margin-bottom:10px;}
  .tbList th{border-top:1px solid #888;}
	.tbList th, .tbList td{border-bottom:1px solid #eee; padding:5px 0;}
	.tbList td.txt_left{text-align:left;}
  .btn{margin-bottom:40px;}
</style>