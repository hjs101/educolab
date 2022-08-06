<template>
  <div>
    <div @change="onSurvey({...credentials})">
      <select v-model="selected">
        <option value="">==문항 선택==</option>
        <option value="choice">객관식 설문조사</option>
        <option value="question">주관식 설문조사</option>
      </select>
      <br>
  
      <div class="surveymargin" v-if="selected === 'question'">
        문항 {{ survey }}. <input class="inputWidth" type="text" placeholder="주관식 문항을 입력해주세요." v-model="credentials.survey_question">
      </div>
  
      <div v-else-if="selected === 'choice'"><br>
        문항 {{ survey }}. <input class="inputWidth" type="text" placeholder="객관식 문항을 입력해주세요." v-model="credentials.survey_question">
        <!-- <button @click="deleteSurvey">X</button> -->
        <div class="surveymargin">
          선택지 1. <input type="text" v-model="num1">
          선택지 2. <input type="text" v-model="num2">
          선택지 3. <input type="text" v-model="num3">
          선택지 4. <input type="text" v-model="num4">
          선택지 5. <input type="text" v-model="num5">
        </div>
      </div>
    </div>
    {{num1}}
  </div>
</template>

<script>
import { ref } from 'vue'
import { mapActions } from 'vuex'
import { reactive, computed } from 'vue'

export default {
  name: 'SurveyItem',
  props: {
    survey: Number,
  },
  setup(props) {
    let selected = ref('')
    let shape = ref('')
    let num1 = ref('')
    let num2 = ref('')
    let num3 = ref('')
    let num4 = ref('')
    let num5 = ref('')
    let credentials = reactive({ 
      survey_question: '',
      question_number : props.survey,
      fullNum: computed(() => {
        if(selected.value === 'question') {
          return null
        } else {
          return `${num1.value}/${num2.value}/${num3.value}/${num4.value}/${num5.value}` 
        }
      })
    })
    return {
      credentials,
      selected,
      shape,
      num1,
      num2,
      num3,
      num4,
      num5
    }
  },
  // computed: {
  //   fullNum: {
  //     get() {
  //       if(this.selected === 'question') {
  //         return null
  //       } else {
  //         return `${this.num1}/${this.num2}/${this.num3}/${this.num4}/${this.num5}` 
  //       }
  //     }
  //   }
  // },
  methods: {
    ...mapActions(['onSurvey']),
  },
}
</script>

<style scoped>
  .inputWidth {
    width: 50%;
  }
  .surveymargin {
    margin: 40px;
  }
</style>