<template>
  <div class="baseStyle">
    <h4 class="text-center">Quiz</h4>
    <hr>
    <!-- 제목, 퀴즈 문제, 퀴즈 보기 -->
    <div v-for="quizItem in quizDetail" :key="quizItem">
      <h4 class="title-size">{{ quizItem.quiz_name }}</h4>
      <q-card class="row" v-if="quizItem.question_number" style="width:80%">
        <q-card-section>
          <p class="bogi-size">퀴즈 {{ quizItem.question_number}} . {{ quizItem.quiz_question }}</p>
          <div class="center">
            <div class="column items-start bogi-size">
              <div class="row items-center q-ml-md">
                <p>보기 1.</p>
                <p class="q-mx-md" style="max-width:1000px;">
                {{ quizItem.multiple_bogi[0]}}</p>
              </div>
              <div class="row items-center q-ml-md">
                <p>보기 2.</p>
                <p class="q-mx-md" style="max-width:1000px;">
                {{ quizItem.multiple_bogi[1]}}</p>                
              </div>
              <div class="row items-center q-ml-md">
                <p>보기 3.</p>
                <p class="q-mx-md" style="max-width:1000px;">
                {{ quizItem.multiple_bogi[2]}}</p>                 
              </div>
              <div class="row items-center q-ml-md">
                <p>보기 4.</p>
                <p class="q-mx-md" style="max-width:1000px;">
                {{ quizItem.multiple_bogi[3]}}</p>                   
              </div>
            </div>
          </div>
        </q-card-section>
      </q-card>
    </div>
    <!-- 퀴즈 답 -->
    <q-card class="q-mt-xl" style="width:80%">
      <q-card-section class="bogi-size">
        <p class="answer-size">제출답안</p>
        <div class="row bogi-size">
          <div v-for="quizItem in quizDetail" :key="quizItem">
            <div class="q-ml-sm row" v-if="quizItem.question_number">
              <p class="q-ml-md q-mr-xs question-border2">답안 {{ quizItem.question_number }}.</p>
              <p class="question-border">{{ quizItem.answer }}번</p>
            </div>
          </div>
        </div>
      </q-card-section>
    </q-card>
    
    <div class="row justify-center q-mt-xl q-gutter-md">
      <q-btn @click="deleteQuiz(quizPk)" class="text-size q-px-xl q-py-md" color="red-6">삭제</q-btn>
      <q-btn @click="updateQuiz(quizPk)" class="text-size q-px-xl q-py-md" color="blue-6">수정</q-btn>
    </div>

    <div class="btn-mag row justify-center">
      <q-btn @click="goQuiz" class="text-size q-px-xl q-py-md" color="grey-8" label="목록"></q-btn>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'QuizDetailView',
  data() {
    return {
      quizPk : this.$route.params.quizPk
    }
  },
  computed: {
    ...mapGetters(['quizDetail', 'isLoggedIn', 'currentUser'])
  },
  methods: {
    ...mapActions(['getQuizDetail', 'deleteQuiz']),
    updateQuiz(quizPk) {
      this.$router.push({name:'QuizCreate', params: {quizPk : quizPk}})
    },
    goQuiz() {
      this.$router.push({name:'Quiz'})
    }
  },
  created() {
    if (!this.isLoggedIn) {
      this.$router.push('/educolab/login/')
    } else if (!this.currentUser.userflag) {
      this.$router.push('/educolab')
    } else {
      this.getQuizDetail(this.quizPk)
    }
  }
}
</script>

<style scoped>
  .title-size {
    font-size : 3vmin;
  }
  .bogi-size {
    font-size : 2vmin;
  }
  .answer-size {
    font-size : 2.5vmin
  }
  .btn-mag {
    margin-top: 100px;
  }
</style>