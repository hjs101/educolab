<template>
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 5d02b22 (네브바, 컴포넌트 구성)
=======
>>>>>>> e6b54fb (asdu)
  <div class="row">
    <div class="col-2">1</div>
    <div class="col-8">퀴즈 메인 페이지</div>
    <div class="col-2">2</div>
<<<<<<< HEAD
<<<<<<< HEAD
=======
  <div>
    <h1>퀴즈 메인 페이지</h1>
  <router-view />
>>>>>>> e66f000 (navbar 생성)
=======
>>>>>>> 5d02b22 (네브바, 컴포넌트 구성)
=======
>>>>>>> e6b54fb (asdu)
=======
=======
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
  <div>

    <!-- <q-form @submit="test">
      <label for="title">테스트: </label>
      <input type="text" id="title" v-model="title">
      <button type="submit">테스트</button>
    </q-form> -->

  <router-view />
<<<<<<< HEAD
>>>>>>> 2553da4 (공지사항  삭제)
=======
  <div>
    <h1>퀴즈 메인페이지</h1>
=======
  <div class="baseStyle">
<<<<<<< HEAD
<<<<<<< HEAD
    <img src="@/assets/quiz.png" alt="quiz">
>>>>>>> 6ecfa2b (기본 폰트, 스타일 적용)
=======
    <img src="@/assets/퀴즈.png" alt="quiz" style="height:150px;">
>>>>>>> d127577 (기능별 메인 페이지 구성)
      <div class="row justify-end">
        <q-btn @click="QuizCreate" class="button-size" 
        color="green-13 q-mx-lg q-py-sm" label="퀴즈 등록" />
      </div>
<<<<<<< HEAD

<<<<<<< HEAD
>>>>>>> 4918ec5 (퀴즈 CRUD 폼 작성)
=======
=======
>>>>>>> d127577 (기능별 메인 페이지 구성)
=======
    <h4 class="text-center">Quiz</h4>
    <hr>
    <div class="row justify-end q-mt-lg">
      <q-btn @click="QuizCreate" class="create-btn q-mx-lg q-py-sm" 
      color="blue-6" label="퀴즈 등록" />
    </div>

>>>>>>> 61e042d (설문조사  통계 sass)
    <div class="q-pa-md">
      <q-markup-table>
        <thead>
          <tr class="text-center">
            <th class="text-size">번호</th>
            <th class="text-center text-size">제목</th>
            <th class="text-center text-size">등록일</th>           
            <th class="text-center text-size">퀴즈 시작</th> 
          </tr>
        </thead>
        <tbody>
          <tr v-for="(quiz, index) in quiz.slice((page-1)*10, page*10)" :key="index">
            <td class="text-size">{{ index+1+((page-1)*10) }}</td>
              <td @click="quizDetail(quiz.pk)" class="text-size cursor-pointer text-left">{{ quiz.title }}</td>
            <td class="text-center text-size">{{ timeInfo(quiz.updated_at) }}</td>
            <!-- 퀴즈 시작 버튼에서 함수 구현 -->
            <td class="text-center text-size">
<<<<<<< HEAD
              <q-btn @click="startQUiz" class="button-size" color="amber-9">Go Quiz!</q-btn>
=======
              <q-btn @click="startQUiz(quiz.pk)" color="indigo-13">Go Quiz!</q-btn>
>>>>>>> 7ae675e (Feat : 웹 퀴즈 기능 완료)
            </td>
          </tr>
        </tbody>
      </q-markup-table>
    </div>
<<<<<<< HEAD
>>>>>>> c9ecd87 (퀴즈 임베디드 연동)
=======
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
=======

    <div>
      <the-pagi-nation v-if="quizLength" :limit="quizLength" @change-page="changePage">
      </the-pagi-nation>
    </div>

>>>>>>> 61e042d (설문조사  통계 sass)
  </div>
</template>

<script>
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
export default {
  name: 'testList',
  // data() {
  //   return {
  //     title : '',
  //   }
  // },
  // methods: {
  //   test() {
  //     console.log(this.title)
  //   }
  // }
}
<<<<<<< HEAD
</script>
=======
=======
import { mapActions, mapGetters } from "vuex";
<<<<<<< HEAD
>>>>>>> c9ecd87 (퀴즈 임베디드 연동)
=======
import { ref } from 'vue'
import ThePagiNation from '@/components/ThePagination.vue'
>>>>>>> 61e042d (설문조사  통계 sass)

export default({
  name: 'QuizView',
  components: { ThePagiNation },
  setup() {
    let page = ref(1)
    const changePage = (value) => {
      page.value = value
    }
    return {
      page,
      changePage,
    }
  },
  computed: { 
    ...mapGetters(['quiz', 'quizLength'])
  },
  methods: {
    ...mapActions(['quizList']),
    timeInfo(time) {
      const d = new Date(time)
      return d.getFullYear() + ". " + (d.getMonth()+1) + ". " + d.getDate()
    },
    quizDetail(quizPk) {
      this.$router.push({name:'QuizDetail', params:{ quizPk: quizPk }},)
    },
    QuizCreate() {
      this.$router.push({name:'QuizCreate'})
    },
    // 여기서 구현 진행하시면 됩니다..
    startQUiz(quizPk) {
      this.$router.push({name:'QuizWait', params:{ quizPk: quizPk }})
    }
  },
  created() {
    this.quizList()
  }
})
</script>

<style scoped>
  .text-size { font-size: 2vmin; }
  .button-size {
    font-size: 1.6vmin;
  }
  .text-nodec {
    text-decoration: none;
  }
  .button-magn {
    margin-right: 200px;
  }
  .create-btn {font-size: 1rem;}
</style>
>>>>>>> 4918ec5 (퀴즈 CRUD 폼 작성)
=======
</script>
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
