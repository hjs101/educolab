<template>
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
  <div>
<<<<<<< HEAD
<<<<<<< HEAD
=======
  <div>
>>>>>>> 3d37e1b (공지사항 검색기능 구현)
=======
  <div>
>>>>>>> e6b54fb (asdu)
    <h2>공지사항 메인 페이지(교사)</h2>
=======
    <!-- <h2>공지사항 메인 페이지(교사)</h2>
>>>>>>> afe56c9 (공지사항 메인페이지)
    <input type="search" name="" id="" v-model="searchTitle">
    <button for="searchTitle" @click="searchNotice">검색</button>
    <tr :key="search.content_id" v-for="search in searchNoticeList">
      <td>{{ search.content_id }}</td>
      <td>{{ search.title }}</td>
      <td>{{ search.created_at }}</td>
      <td>{{ search.user_id }}</td> 
    </tr>
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e6b54fb (asdu)
    
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
<<<<<<< HEAD
</style>
=======
    <h1>공지 메인 페이지</h1>
  </div>
</template>
>>>>>>> e66f000 (navbar 생성)
=======
  <div class="row">
    <div class="col-2"></div>
=======
>>>>>>> 3d37e1b (공지사항 검색기능 구현)

    <table>
      <thead>
        <tr>
          <th>분류</th>
          <th>제목</th>
          <th>등록일</th>
          <th>등록자</th>          
        </tr>
      </thead>

      <tbody>
        <tr :key="notice.content_id" v-for="notice in content">
          <td>{{ notice.content_id }}</td>
          <td>{{ notice.title }}</td>
          <td>{{ notice.created_at }}</td>
          <td>{{ notice.user_id }}</td>          
        </tr>
      </tbody>
    </table>

  </div>
</template>

<script>
import noticeList from '@/data/index.js'

export default {
  name: "NoticeView",
  data() {
    return {
      content: noticeList.Content,
      searchTitle: '',
      searchNoticeList : [],
    }
  },
  methods: {
    searchNotice() {
      this.searchNoticeList = []
      for (let index = 0; index < this.content.length; index++) {
        if (this.content[index].title.includes(this.searchTitle)) {
          this.searchNoticeList.push(this.content[index])
        }
    }
  }
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
>>>>>>> 5d02b22 (네브바, 컴포넌트 구성)
=======
</style>
>>>>>>> e6b54fb (asdu)
