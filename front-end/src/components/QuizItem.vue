<template>
  <div @change="onQuiz({...credentials})">
    <div class="q-my-lg row items-center">
      <span class="text-size">퀴즈 {{ quiz }}.</span>
      <q-input outlined v-model="credentials.quiz_question" style="width:50%" placeholder="문제를 입력해주세요."/>
    </div>
    <div class="row items-center">
      <span class="bogi-size">보기 1.</span><q-input outlined v-model="num1" style="width:40%" placeholder="보기를 입력해주세요."/>
    </div>
    <div class="row items-center">
      <span class="bogi-size">보기 2.</span><q-input outlined v-model="num2" style="width:40%" placeholder="보기를 입력해주세요."/>
    </div>
    <div class="row items-center">
      <span class="bogi-size">보기 3.</span><q-input outlined v-model="num3" style="width:40%" placeholder="보기를 입력해주세요."/>
    </div>
    <div class="row items-center">
      <span class="bogi-size">보기 4.</span><q-input outlined v-model="num4" style="width:40%" placeholder="보기를 입력해주세요."/>
    </div>
    <div>
      <p class="q-pt-sm title-size">제출 답안</p>
      <q-input class="answer-border" outlined v-model="credentials.answer" style="width:40px;"></q-input>
    </div>        
    <hr>
    <!-- <div class="row">
      <div class="row q-mb-xl items-center" v-for="answer in quizList" :key="answer">
        <p class="bogi-size">답안 {{ answer }}.</p>
      </div>
    </div> -->
  </div>
</template>

<script>
import { ref } from 'vue'
import { mapGetters, mapActions } from 'vuex'
import { reactive, computed } from '@vue/reactivity'

export default {
  name: 'QuizItem',
  props: {
    quiz: Number,
    quizDetail: Object,
  },
  setup(props) {
    let num1 = ref('')
    let num2 = ref('')
    let num3 = ref('')
    let num4 = ref('')
    let credentials = reactive({
      quiz_question : ref(''),
      question_number: props.quiz,
      answer : ref(''), 
      multiple_bogi: computed(() => {
        return `${num1.value}/${num2.value}/${num3.value}/${num4.value}/` 
      }),
    })
    return {
      credentials,
      num1,
      num2,
      num3,
      num4,
    }
  },  
  computed: {
    ...mapGetters(['quizData'])
  },
  methods: {
    ...mapActions(['onQuiz'])
  },
  mounted() {
    for (var i=1; i < this.quizDetail.length; i++) {
      if (this.quiz === i) {
        this.credentials.quiz_question = this.quizDetail[i].quiz_question
        this.credentials.answer = this.quizDetail[i].answer
        this.num1 = this.quizDetail[i].multiple_bogi[0]
        this.num2 = this.quizDetail[i].multiple_bogi[1]
        this.num3 = this.quizDetail[i].multiple_bogi[2]
        this.num4 = this.quizDetail[i].multiple_bogi[3]
      }
    }
  }
}
</script>

<style scoped>
 p {
  margin : 0;
 }
</style>