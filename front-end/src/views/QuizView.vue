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
    <img src="@/assets/quiz.png" alt="quiz">
>>>>>>> 6ecfa2b (기본 폰트, 스타일 적용)
=======
    <img src="@/assets/퀴즈.png" alt="quiz" style="height:150px;">
>>>>>>> d127577 (기능별 메인 페이지 구성)
      <div class="row justify-end">
        <q-btn @click="QuizCreate" class="text-size" 
        color="green-13 q-mx-lg q-py-sm" label="퀴즈 등록" />
      </div>
<<<<<<< HEAD

<<<<<<< HEAD
>>>>>>> 4918ec5 (퀴즈 CRUD 폼 작성)
=======
=======
>>>>>>> d127577 (기능별 메인 페이지 구성)
    <div class="q-pa-md">
      <q-markup-table>
        <thead>
          <tr>
            <th class="text-left text-size">번호</th>
            <th class="text-center text-size">제목</th>
            <th class="text-center text-size">등록일</th>           
            <th class="text-center text-size">퀴즈 시작</th> 
          </tr>
        </thead>
        <tbody>
          <tr v-for="quiz in quiz" :key="quiz">
            <td class="text-left text-size">{{ quiz.pk }}</td>
              <td @click="quizDetail(quiz.pk)" class="text-size cursor-pointer">{{ quiz.title }}</td>
            <td class="text-center text-size">{{ timeInfo(quiz.updated_at) }}</td>
            <!-- 퀴즈 시작 버튼에서 함수 구현 -->
            <td class="text-center text-size">
              <q-btn @click="startQUiz" color="indigo-13">Go Quiz!</q-btn>
            </td>
          </tr>
        </tbody>
      </q-markup-table>
    </div>
>>>>>>> c9ecd87 (퀴즈 임베디드 연동)
=======
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
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
>>>>>>> c9ecd87 (퀴즈 임베디드 연동)

export default({
  name: 'QuizView',
  computed: { 
    ...mapGetters(['quiz'])
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
    startQUiz() {
      console.log('test')
    }
  },
  created() {
    this.quizList()
  }
})
</script>

<style scoped>
  .text-size {
    font-size: 1.2rem;
  }
  .text-nodec {
    text-decoration: none;
  }
</style>
>>>>>>> 4918ec5 (퀴즈 CRUD 폼 작성)
=======
</script>
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
