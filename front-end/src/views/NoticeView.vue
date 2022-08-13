<template>
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
  <div class="center">
=======
  <div id="notice" class="center">
>>>>>>> 6ecfa2b (기본 폰트, 스타일 적용)
    <h1>공지사항</h1>
    <router-link to="/notice/create"><button>글쓰기</button></router-link>
>>>>>>> fec931d (공지사항  상세페이지 구현)
=======
  <div class="center">
    <h1>공지사항</h1>
    <router-link to="/notice/create"><button>글쓰기</button></router-link>
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
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
<<<<<<< HEAD
          <td>{{ notice.classification }}</td>
=======
          <td>{{ notice.classification}}</td>
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
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


=======
  <div class="baseStyle">
    <img src="@/assets/공지사항.png" alt="notice" style="height:150px;">
    <div class="row justify-end">
      <q-btn @click="noticeCreate" class="text-size q-mx-lg q-py-sm" 
      color="green-13" label="글 쓰기" />
    </div>

    <div class="q-pa-md">
      <q-markup-table class="notice-full">
        <thead>
          <tr>
            <th class="text-left text-size">번호</th>
            <th class="text-center text-size">분류</th>
            <th class="text-center text-size">제목</th>
            <th class="text-center text-size">작성자</th>
            <th class="text-center text-size">등록(수정)일</th>
            <th class="text-center text-size">조회수</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(notice, index) in notice2.slice((page-1)*10, page*10)" :key="index">
            <td class="text-left text-size">{{ index+1+((page-1)*10) }}</td>

            <td v-if="notice.classification === '변경'" class="text-size text-center text-pink-13">{{ notice.classification }}</td>
            <td v-else-if="notice.classification === '공지'" class="text-size text-center text-indigo-13">{{ notice.classification }}</td>
            <td v-else-if="notice.classification === '행사'" class="text-size text-center text-green-13">{{ notice.classification }}</td>

            <td @click="noticeDetail(notice.pk)" class="cursor-pointer text-size">{{ notice.title }}</td>
            <td class="text-center text-size">{{ notice.teacher.name }}</td>
            <td class="text-center text-size">{{ timeInfo(notice.updated_at) }}</td>
            <td class="text-center text-size">{{ notice.views }}</td>
          </tr>
        </tbody>
      </q-markup-table>

      <q-markup-table class="notice-small">
        <thead>
          <tr>
            <th class="text-center text-size">분류</th>
            <th class="text-center text-size">제목</th>
            <!-- <th class="text-center text-size">등록(수정)일</th> -->
          </tr>
        </thead>
        <tbody>
          <tr v-for="(notice, index) in notice2.slice((page-1)*10, page*10)" :key="index">
            <td v-if="notice.classification === '변경'" class="text-size text-center text-pink-13">{{ notice.classification }}</td>
            <td v-else-if="notice.classification === '공지'" class="text-size text-center text-indigo-13">{{ notice.classification }}</td>
            <td v-else-if="notice.classification === '행사'" class="text-size text-center text-green-13">{{ notice.classification }}</td>

            <td @click="noticeDetail(notice.pk)" class="cursor-pointer text-size">{{ notice.title }}</td>
            <!-- <td class="text-center text-size">{{ timeInfo(notice.updated_at) }}</td> -->
          </tr>
        </tbody>
      </q-markup-table>
    </div>
<<<<<<< HEAD
>>>>>>> d127577 (기능별 메인 페이지 구성)
=======

    <div>
      <the-pagi-nation v-if="noticeLenth" :limit="noticeLenth" @change-page="changePage">
      </the-pagi-nation>
    </div>   

>>>>>>> 38a5ff1 (공지사항  수정 해결)
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import { ref } from 'vue'
import ThePagiNation from '@/components/ThePagination.vue'

export default {
  name: "NoticeView",
  components: {ThePagiNation},
  setup() {
    let page = ref(1)
    const changePage = (value) => {
      page.value = value
    }
    // length: computed(() => Math.ceil(search.list.length/10))
    return {
      page,
      changePage
    }
  },
  computed: {
    ...mapGetters(['notice2', 'noticeLenth'])
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
    this.noticeList()
  }
}

</script>

<<<<<<< HEAD
<style>
<<<<<<< HEAD
  #notice {
    margin: auto;
    width: 80%;
    font-family: "jooa";
  }
=======
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
=======
<style scoped>
<<<<<<< HEAD
  .text-size{font-size: 1.2rem;}
>>>>>>> d127577 (기능별 메인 페이지 구성)
=======
  .text-size{font-size: 1.4rem;}
>>>>>>> 38a5ff1 (공지사항  수정 해결)
  .searchWrap{border-radius:5px; text-align:center; padding:20px 0; margin-bottom:10px;}
  .tbList th{border-top:1px solid #888;}
	.tbList th, .tbList td{border-bottom:1px solid #eee; padding:5px 0;}
	.tbList td.txt_left{text-align:left;}
  .btn{margin-bottom:40px;}
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
</style>
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
=======
  .notice-small {
    display: none;
  }

  @media screen and (max-width: 950px) {
    .notice-full {
      display: none;
    }
    .notice-small {
      display: block;
    }
  }
</style>
>>>>>>> 38a5ff1 (공지사항  수정 해결)
