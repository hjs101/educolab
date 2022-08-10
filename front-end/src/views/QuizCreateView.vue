<template>
  <div class="baseStyle q-px-xl">
    <h4>퀴즈 등록 페이지</h4>
    <div class="row justify-end q-mx-xl">
      <q-btn class="q-mb-md text-bold q-pa-md" color="green-13">퀴즈 등록</q-btn>
    </div>

    <div class="row justify-start">
      <q-btn @click="addQuiz" 
      class="q-mx-lg"
      color="orange-6" label="문제 추가" />
    </div>
    <br>

    <div class="row q-pa-md justify-center">
      <div class="q-gutter-md" style="width:50%">
        <q-input outlined v-model="credentials.quiz.title" placeholder="퀴즈 제목을 입력해주세요."/>
      </div>
    </div>
    <hr>

    <form>
      <div v-if="quizPk">
        <div v-for="quiz in quizData.length" :key="quiz">
          <quiz-item
          :quiz="quiz"
          :quizDetail="quizDetail"
          />
          <button @click="deleteQuiz(quiz, $event)">퀴즈문제 삭제</button>
        </div>
      </div>

      <div v-else>
        <div v-for="quiz in quizList" :key="quiz">
          <quiz-item
          :quiz="quiz"
          :quizDetail="quizDetail"
          />
          <button @click="deleteQuiz(quiz, $event)">퀴즈문제 삭제</button>
        </div>
      </div>
    </form>

    <button @click="quizPk? updateQuiz({credentials, quizPk}) : createQuiz(credentials)">
    {{ quizPk? '퀴즈 수정' : '퀴즈 등록'}}
    </button>
  </div>
</template>

<script>
import QuizItem from '@/components/QuizItem.vue'
import {useRoute} from 'vue-router'
import { reactive } from '@vue/reactivity'
import { ref } from 'vue'
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'QuizCreateView',
  components: { QuizItem },
  setup() {
    const route = useRoute()
    let quizPk = ref(route.params.quizPk)
    let credentials = reactive({
      quiz: {
        title : ref('')
      },
      question : {},
    })
    return {
      credentials,
      quizPk,
    }
  },
  data() {
    return {
      quizList : 2
    }
  },
  computed: {
    ...mapGetters(['quizDetail', 'quizData'])
  },
  methods: {
    ...mapActions(['createQuiz', 'getQuizDetail']),
    addQuiz() {
      this.quizList++,
      this.quizData.push({})
    },
    deleteQuiz(quiz, event) {
      event.preventDefault()
      this.quizList = this.quizList - 1
      this.quizData.splice(quiz-1, 1)
    }
  },
  mounted() {
    if (this.quizPk) {
      this.getQuizDetail(this.quizPk)
      for (var i=0; i < this.quizDetail.length; i++) {
        if ( this.quizDetail[i].quiz_name) {
          this.credentials.quiz.title = this.quizDetail[i].quiz_name
        }
        return
      }
    }
  }
}
</script>

<style scoped>
  .title-size {
    font-size: 1.5rem;
  }
  .text-size {
    font-size: 1.1rem;
  }
  .bogi-size {
    font-size: 0.9rem;
  }
  .input-size {
    padding: 1px 2px;
  }
  .answer-border {
  border-radius: 5px;
  border: 1px solid #BDBDBD ;
  }
  .answer-border2 {
    border-radius: 5px;
    border: 1px solid #BDBDBD ;
    background-color: #FF9966;
  }
</style>