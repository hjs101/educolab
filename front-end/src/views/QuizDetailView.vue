<template>
  <div class="baseStyle">
    <!-- 제목, 퀴즈 문제, 퀴즈 보기 -->
    <div v-for="quizItem in quizDetail" :key="quizItem">
      <h4>{{ quizItem.quiz_name }}</h4>
      <div v-if="quizItem.question_number">
        <p class="title-size">퀴즈 {{ quizItem.question_number}}번: {{ quizItem.quiz_question }}</p>
        <div class="row justify-start bogi-size">          
          <p class="q-mx-md q-px-md bogi-border">① {{ quizItem.multiple_bogi[0]}}</p>
          <p class="q-mx-md q-px-md bogi-border">② {{ quizItem.multiple_bogi[1]}}</p>
          <p class="q-mx-md q-px-md bogi-border">③ {{ quizItem.multiple_bogi[2]}}</p>
          <p class="q-mx-md q-px-md bogi-border">④ {{ quizItem.multiple_bogi[3]}}</p>
        </div>
      </div>
    </div>
    <!-- 퀴즈 답 -->
    <div class="">
      <p class="title-size q-mt-xl q-mx-lg">제출답안 </p>
      <div class="row title-size ">
        <div v-for="quizItem in quizDetail" :key="quizItem">
          <div class="row" v-if="quizItem.question_number">
            <p class="q-px-sm question-border2">{{ quizItem.question_number }}</p>
            <p class="question-border q-px-sm">{{ quizItem.answer }}번</p>
          </div>
        </div>
      </div>
    </div>
    
    <div class="row justify-center q-my-lg">
      <q-btn @click="deleteQuiz(quizPk)" class="q-mx-lg" color="orange-6">퀴즈 삭제</q-btn>
      <q-btn @click="updateQuizx(quizPk)" class="q-mx-lg" color="orange-6">퀴즈 수정</q-btn>
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
    ...mapGetters(['quizDetail'])
  },
  methods: {
    ...mapActions(['getQuizDetail', 'deleteQuiz']),
    updateQuizx(quizPk) {
      this.$router.push({name:'QuizCreate', params: {quizPk : quizPk}})
    }
  },
  mounted() {
    this.getQuizDetail(this.quizPk)
  }
}
</script>

<style scoped>
.bogi-border {
  /* border: 1px inset #FFC000; */
  border-style: inset;
}
.question-border {
  border-radius: 5px;
  border: 1px solid #BDBDBD ;
}
.title-size {
  font-size : 1.5rem;
}
.bogi-size {
  font-size : 1.1rem;
}
.question-border2 {
  border-radius: 5px;
  border: 1px solid #BDBDBD ;
  background-color: #FF9966;
}
.test {
  border-bottom : 1px solid #BDBDBD;
}
</style>