<template>
  <div class="baseStyle">
    <img src="@/assets/quiz.png" alt="quiz">
      <div class="row justify-end">
        <q-btn @click="QuizCreate" color="green-13 q-mx-lg q-py-sm text-bold text-size" 
        label="퀴즈 등록" />
      </div>

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
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default({
  setup() {

  },
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
  /* #quiz {
    margin: auto;
    width: 80%;
    font-family: "jooa";
  } */
  .text-size {
    font-size: 1.1rem;
  }
  .text-nodec {
    text-decoration: none;
  }
</style>
