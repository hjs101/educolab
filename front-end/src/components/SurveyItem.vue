<template>
  <div>
    <div @change="goSurvey(credentials)">
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
          선택지 1. <input type="text" v-model="credentials.num1">
          선택지 2. <input type="text" v-model="credentials.num2">
          선택지 3. <input type="text" v-model="credentials.num3">
          선택지 4. <input type="text" v-model="credentials.num4">
          선택지 5. <input type="text" v-model="credentials.num5">
        </div>
      </div>
    </div>
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
    const credentials = reactive({ 
      survey_question: '',
      question_number : props.survey,
      fullNum: computed(() => {
        if(this.selected === 'question') {
          return null
        } else {
          return `${this.num1}/${this.num2}/${this.num3}/${this.num4}/${this.num5}` 
        }
      })
    })
    const selected = ref('')
    return {
      credentials,
      shape: ref(''),
    }
  },
  data() {
    // const fullNum = `${this.num1}/${this.num2}/${this.num3}/${this.num4}/${this.num5}`? `${this.num1}/${this.num2}/${this.num3}/${this.num4}/${this.num5}` : null
    return {
      selected: '',
      num1 : '',
      num2 : '',
      num3 : '',
      num4 : '',
      num5 : '',
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
    ...mapActions(['goSurvey']),
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