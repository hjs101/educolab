<template>
  <div class="baseStyle">
    <h4>{{ getTitle }}</h4>

    <div class="row q-mr-xl justify-end">
      <q-btn @click="addQuiz" class="text-size"
      color="orange-6" label="문제 추가" />
    </div>

    <q-form>
      <div class="row q-mt-xl">
          <span class="q-py-md q-mx-lg text-center text-size">제목</span>
          <q-input class="text-size" outlined v-model="credentials.quiz.title" 
          style="width: 700px;" placeholder="퀴즈 제목을 입력해주세요." 
          lazy-rules
          :rules="[ val => val && val.length > 0 || '제목을 입력해주세요']"
          autofocus
          />
      </div>
      <hr>

      <div v-if="quizPk">
        <div v-for="quiz in quizList" :key="quiz">
          <div class="row justify-end q-mt-xl q-mr-xl">
            <q-btn @click.prevent="deleteQuiz(quiz, $event)" class="text-size" color="orange-6">문제 삭제</q-btn>
          </div>
          <quiz-item
          :quiz="quiz"
          :quizPk="quizPk"
          />
        </div>
      </div>

      <div v-else>
        <div v-for="quiz in quizList" :key="quiz">
          <div class="row justify-end q-mt-md q-mr-xl">
            <q-btn @click="deleteQuiz(quiz, $event)" class="text-size" color="orange-6">문제 삭제</q-btn>
          </div>
          <quiz-item
          :quiz="quiz"
          :quizPk="quizPk"
          />
        </div>
      </div>

      <div class="row justify-center q-my-xl">
        <q-btn @click="goQuiz" class="text-size q-px-xl q-py-md" color="grey-8">취소</q-btn>
        <q-btn @click="quizPk ? updateQuiz(credentials) : createQuiz(credentials)"
        class="text-size q-px-xl q-py-md q-mx-lg q-py-sm" color="blue-6">
        {{ quizPk ? '수정' : '등록'}}
        </q-btn>
      </div>
    </q-form>

  </div>
</template>

<script>
import { useRoute } from 'vue-router'
import { reactive } from '@vue/reactivity'
import { ref } from 'vue'
import { mapActions, mapGetters } from 'vuex'
import QuizItem from '@/components/QuizItem.vue'

export default {
  name: 'QuizCreateView',
  components: { QuizItem },
  setup() {
    const route = useRoute()
    const { quizPk } = route.params
    const credentials = reactive({
      quiz_num : quizPk,
      quiz: {
        title : ref('')
      },
      question : {},
    })
    // let quizDetail = null
    return {
      credentials,
      quizPk,
    }
  },
  data() {
    return {
      quizList : 1
    }
  },
  computed: {
    ...mapGetters(['quizDetail', 'quizData', 'isLoggedIn', 'currentUser', 'quizItemLength']),
    getTitle() {
      if (this.quizPk) return "퀴즈 수정"
      return "퀴즈 등록"
    }
  },
  methods: {
    ...mapActions(['createQuiz', 'getQuizDetail', 'updateQuiz', 'quizTotalData']),
    addQuiz() {
      this.quizList++
      this.quizData.push({})
    },
    deleteQuiz(quiz, event) {
      if (quiz === 1 && this.quizList === 1) {
        alert('퀴즈는 한 문제 이상 작성되어야 합니다.')
      } else if (confirm('문제를 정말 삭제하시겠습니까?')) {
          event.preventDefault()
          this.quizList = this.quizList - 1
          this.quizData.splice(quiz-1, 1)
        }
    },
    goQuiz() {
      if (confirm('페이지에서 나가시겠습니까? 글은 저장되지 않습니다.'))
      this.$router.push({name:'Quiz'})
    }
  },
  created() {
    if (!this.isLoggedIn) {
      this.$router.push('/educolab/login/')
    } else if (!this.currentUser.userflag) {
      this.$router.push('/educolab')
    } else if (this.quizPk) {
      this.getQuizDetail(this.quizPk)
      this.credentials.quiz.title = this.quizDetail[0].quiz_name
      this.quizTotalData(this.quizDetail.slice(1, this.quizItemLength))
      this.quizList = this.quizItemLength-1
    } 
  }
}
</script>

<style scoped>
  .title-size {
    font-size: 1.5rem;
  }
  .text-size {
    font-size: 1rem;
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