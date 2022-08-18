<template>
  <div>
    <div @change="onSurvey({...credentials})">
      <div class="q-py-md">
        <q-select class="text-size q-ml-sm" style="width:150px;" outlined v-model="selected" 
        :options="selSelected" label="문항 선택" emit-value map-options/>
      </div>

      <div class="row items-center" v-if="selected === 'question'">
        <span class="q-mx-lg text-center text-size">문항 {{ survey }}.</span>
        <q-input outlined class="text-size" v-model="credentials.survey_question" 
        style="width: 685px;" placeholder="설문 문항을 입력해주세요." />
      </div>
      
      <div class="column items-start" v-else-if="selected === 'choice'"><br>
        <div class="row items-center">
          <span class="q-mx-lg text-center text-size">문항 {{ survey }}.</span>
          <q-input outlined class="text-size" v-model="credentials.survey_question" 
          style="width: 685px;" placeholder="설문 문항을 입력해주세요." />
        </div>
        <div class="q-mt-lg q-ml-lg">
          <q-input outlined class="text-size" label="보기 1" style="width:685px;" v-model="num1" /><br>
          <q-input outlined class="text-size" label="보기 2" style="width:685px;" v-model="num2" /><br>
          <q-input outlined class="text-size" label="보기 3" style="width:685px;" v-model="num3" /><br>
          <q-input outlined class="text-size" label="보기 4" style="width:685px;" v-model="num4" /><br>
          <q-input outlined class="text-size" label="보기 5" style="width:685px;" v-model="num5" />
        </div>
      </div>
      <hr>

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
    surveyPk: String
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
      selSelected: [
        {
          label: '객관식',
          value: 'choice'
        },
        {
          label: '주관식',
          value: 'question'
        },
      ],
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
    ...mapActions(['onSurvey', 'getSurveyDetail']),
  },
  created() {
    if (this.surveyPk) {
      // this.getSurveyDetail(this.surveyPk)
      for (var i=1; i < this.surveyItem.length; i++) {
        if (this.survey === this.surveyItem[i].question_number) {
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
  .text-size {
    font-size: 1rem;
  }
  .button-size {
    font-size: 1.1rem;
  }
</style>