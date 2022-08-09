<template>
  <div>
    <div class="test">
      <!-- 첫번째 라인 -->
      <div class="test hor">
        <div class="test">퀴즈 번호 & title</div>
        <div class="test">
          <div class="test">퀴즈 대기중</div>
          <div class="test hor">
            <div class="test">사람수 확인 {{dummy_name.length}}</div>
            <button class="test" @click='testInfo()'>더미데이터 추가 버튼</button>
            <router-link to="/quiz/online02"><button>화면 전환</button></router-link>
          </div>
        </div>
       </div>
      <!-- 두번째 라인 -->
      <div class="test hor">
        <div class="test" v-for="item in dummy_name" :key="item">{{item}}</div>
      </div>
    </div>
  <!-- <div class="center"> -->
    <!-- <h1>공지사항</h1>
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
    </table> -->
  </div>
</template>

<script>
// import { mapActions, mapGetters } from 'vuex'
// import NoticeItem from '@/components/NoticeItem.vue'

export default {
  name: "QuizWait",
  data() {
    return {
      dummy_name:['안녕하세요','데이터 입력 테스트 중입니다']
    }
  },
  // components: {
  //   NoticeItem
  // },
  // computed: {
  //   ...mapGetters(['notice2', 'noticeItem'])
  // },
  methods: {
    // ...mapActions(['noticeList', 'noticeDetail']),
    testInfo() {
      this.dummy_name.push('더미 데이터를 추가합니다.')
    },
    // rowClicked(row) {
    //   this.$router.push({
    //     path: `/board/detail/${row.id}`
    //   })
    // }
  },
  // mounted() {
  //   this.noticeList()
  // }
}

</script>

<style>
  /* .searchWrap{border-radius:5px; text-align:center; padding:20px 0; margin-bottom:10px;}
  /* .tbList th{border-top:1px solid #888;} */
	/* .tbList th, .tbList td{border-bottom:1px solid #eee; padding:5px 0;}
	.tbList td.txt_left{text-align:left;} */
  .test{
    border:2px solid black;
    }
  /* .vert{
    display: flex;
    flex-direction: column;
  } */
  .hor{
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
  }
</style>