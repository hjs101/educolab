<template>
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
    <div v-for="item in content"
    :key="item.content_id">
    <p>{{ item.title }}</p>
    <p>{{ item.context }}</p>
    </div>

  </div>
</template>

<script>
import noticeList from '@/data/index.js'

export default {
  name: "NoticeView",
  data() {
    return {
      content: noticeList.Content
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