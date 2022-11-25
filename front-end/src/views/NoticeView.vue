<template>
<<<<<<< HEAD
  <div>
<<<<<<< HEAD
    <h2>공지사항 메인 페이지(교사)</h2>
    <input type="search" name="" id="" v-model="searchTitle">
    <button for="searchTitle" @click="searchNotice">검색</button>
    <tr :key="search.content_id" v-for="search in searchNoticeList">
      <td>{{ search.content_id }}</td>
      <td>{{ search.title }}</td>
      <td>{{ search.created_at }}</td>
      <td>{{ search.user_id }}</td> 
    </tr>
    
    <router-link to="/notice/create"><button>글쓰기</button></router-link>

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
=======
    <h1>공지 메인 페이지</h1>
  </div>
</template>
>>>>>>> e66f000 (navbar 생성)
=======
  <div class="row">
    <div class="col-2"></div>

    <div class="col-8">
      <div class="searchWrap">
        <input type="text" width="10000px">
        <button>검색</button>
      </div>

      <div class="row justify-end">
        <router-link to="/notice/create"><button class="btn">공지사항 등록</button></router-link>
      </div>

      <div class="listWrap bg-grey-3 text-black flex flex-center">
        <table class="tbList">
          <!-- <colgroup>
            <col width="6%" />
            <col width="*" />
            <col width="10%" />
            <col width="15%" />
          </colgroup> -->
          <tr>
            <th width="6%">분류</th>
            <th width="300px *">제목</th>
            <th width="200px 10%">등록일</th>
            <th width="150px 15%">작성자</th>
          </tr>
        </table>
      </div>
    </div>

    <div class="col-2"></div>

  </div>
</template>

<script>

</script>

<style>
  .searchWrap{border-radius:5px; text-align:center; padding:20px 0; margin-bottom:10px;}
  .tbList th{border-top:1px solid #888;}
	.tbList th, .tbList td{border-bottom:1px solid #eee; padding:5px 0;}
	.tbList td.txt_left{text-align:left;}
  .btn{margin-bottom:40px;}
</style>
>>>>>>> 5d02b22 (네브바, 컴포넌트 구성)
