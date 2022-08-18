<template>
  <div @change="onQuiz({...credentials})">
    <div class="q-my-lg row items-center">
      <span class="text-size q-mx-md text-center">퀴즈 {{ quiz }}.</span>
      <q-input class="text-size" outlined v-model="credentials.quiz_question" style="width:50%" placeholder="문제를 입력해주세요."
      lazy-rules
      :rules="[ val => val && val.length > 0 || '문제를 입력해주세요']"
      />
    </div>
    <div class="column items-start q-mx-md">
      <q-input outlined style="width:685px;" class="text-size" label="보기 1" v-model="num1"
      lazy-rules
      :rules="[ val => val && val.length > 0 || '보기를 입력해주세요']"/><hr>
      <q-input outlined style="width:685px;" class="text-size" label="보기 2" v-model="num2"
      lazy-rules
      :rules="[ val => val && val.length > 0 || '보기를 입력해주세요']"/><hr>
      <q-input outlined style="width:685px;" class="text-size" label="보기 3" v-model="num3"
      lazy-rules
      :rules="[ val => val && val.length > 0 || '보기를 입력해주세요']"/><hr>
      <q-input outlined style="width:685px;" class="text-size" label="보기 4" v-model="num4"
      lazy-rules
      :rules="[ val => val && val.length > 0 || '보기를 입력해주세요']"/>
    </div>     
    <div class="q-mx-md">
      <p class="text-size">제출 답안</p>
      <q-input class="answer-border q-ml-sm" outlined v-model="credentials.answer" style="width:40px;" />
    </div>  
    <hr>
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
    quizPk: String,
  },
  setup(props) {
    let num1 = ref('')
    let num2 = ref('')
    let num3 = ref('')
    let num4 = ref('')
    let credentials = reactive({
      quiz_question : '',
      question_number: props.quiz,
      answer : '', 
      multiple_bogi: computed(() => {
        return `${num1.value}/${num2.value}/${num3.value}/${num4.value}` 
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
    ...mapGetters(['quizData', 'quizDetail'])
  },
  methods: {
    ...mapActions(['onQuiz', 'getQuizDetail'])
  },
  created() {
    if (this.quizPk) {
      console.log(this.quizDetail)
      for (var i=1; i < this.quizDetail.length; i++) {
        if (this.quiz === this.quizDetail[i].question_number) {
          this.credentials.quiz_question = this.quizDetail[i].quiz_question
          this.credentials.answer = this.quizDetail[i].answer
          this.num1 = this.quizDetail[i].multiple_bogi[0]
          this.num2 = this.quizDetail[i].multiple_bogi[1]
          this.num3 = this.quizDetail[i].multiple_bogi[2]
          this.num4 = this.quizDetail[i].multiple_bogi[3]

          this.quizDetail[i].multiple_bogi = this.quizDetail[i].multiple_bogi.join('/')
          return
        }
      }
    }
  }
}
</script>

<style scoped>
  .text-size {
    font-size: 1rem;
  }
</style>