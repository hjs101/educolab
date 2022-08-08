<template>
  <div>
    <h1>퀴즈 등록 페이지</h1>
    <button @click="addQuiz">문제 추가</button>
    <br>
    퀴즈 제목 : <input type="text">
    <div v-for="quiz in quizList" :key="quiz">
      퀴즈 {{ quiz }}. : <input type="text" placeholder="퀴즈 문제를 입력해주세요.">
      <div>
        1. <input type="text" placeholder="문제 보기를 입력해주세요.">
        2. <input type="text" placeholder="문제 보기를 입력해주세요.">
        3. <input type="text" placeholder="문제 보기를 입력해주세요.">
        4. <input type="text" placeholder="문제 보기를 입력해주세요.">
      </div>
    </div>

    <div class='row'>
      <div v-for="answer in quizList" :key="answer">
        {{ answer }} 답안. <input type="text">
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'QuizCreateView',
  data() {
    return {
      quizList : 1,
    }
  },
  methods: {
    addQuiz() {
      this.quizList++
    }
  }
}
</script>

<style>

</style>