<template>
  <div>
    <h2>공지사항 메인 페이지(교사)</h2>
    <input type="search" name="" id="" v-model="searchTitle">
    <button for="searchTitle" @click="searchNotice">검색</button>
    <tr :key="search.content_id" v-for="search in searchNoticeList">
      <td>{{ search.content_id }}</td>
      <td>{{ search.title }}</td>
      <td>{{ search.created_at }}</td>
      <td>{{ search.user_id }}</td> 
    </tr>

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