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
        <div class="surveymargin">
          선택지 1. <input type="text" v-model="num1">
          선택지 2. <input type="text" v-model="num2">
          선택지 3. <input type="text" v-model="num3">
          선택지 4. <input type="text" v-model="num4">
          선택지 5. <input type="text" v-model="num5">
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'
import { mapActions, mapGetters } from 'vuex'
import { reactive, computed } from 'vue'

export default {
  name: 'SurveyItem',
  props: {
    survey: Number,
    surveyPk: Number,
  },
  setup(props) {
    let selected = ref('')
    let num1 = ref('')
    let num2 = ref('')
    let num3 = ref('')
    let num4 = ref('')
    let num5 = ref('')
    let credentials = reactive({ 
      survey_question: '',
      question_number : props.survey,
      multiple_bogi: computed(() => {
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
      num1,
      num2,
      num3,
      num4,
      num5
    }
  },
  computed: {
    ...mapGetters(['surveyItem', 'surveyData', 'surveyBogi'])
  },
  methods: {
    ...mapActions(['onSurvey']),
  },
  mounted() {
    if (this.surveyPk) {
      for (var i=1; i < this.surveyItem.length; i++) {
        if (this.survey == this.surveyItem[i].question_number) {
          this.credentials.survey_question = this.surveyItem[this.survey].survey_question
          if (this.surveyItem[this.survey].multiple_bogi === null) {
            this.selected = 'question'
            return
            } else {
            this.selected = 'choice'
            this.num1 = this.surveyBogi[this.survey][0]
            this.num2 = this.surveyBogi[this.survey][1]
            this.num3 = this.surveyBogi[this.survey][2]
            this.num4 = this.surveyBogi[this.survey][3]
            this.num5 = this.surveyBogi[this.survey][4]
            return
          }
        }
      }
    }
  }
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