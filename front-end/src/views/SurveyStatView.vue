<template>
  <div class="baseStyle text-size">
    <h4>{{ surveyStat.survey_title }}</h4>
    <div v-for="item in surveyStat.questions" :key="item">   
      <q-card class="q-mb-lg" v-if="item.multiple_bogi">
        <q-card-section style="width:80%" class="q-mt-lg">
          <p class="title-size">문항 {{ item.question_number }} . {{ item.survey_question }}</p>    
          <div class="row q-my-md">
            <p class="q-pr-md">보기 1. </p>
            <p class="bg-red-13 border-left1" :style="{width: item.purcentNum[0]-20 + '%'}"></p>
            <p class="q-px-sm">{{ item.multiple_bogi[0] }}</p>
            <p>({{ item.num1 }})</p>
          </div>

          <div class="row q-my-md">
            <p class="q-pr-md">보기 2. </p>
            <p class="bg-blue-13 border-left2" :style="{width: item.purcentNum[1]-20 + '%'}"></p>
            <p class="q-px-sm">{{ item.multiple_bogi[1]}}</p>
            <p>({{ item.num2 }})</p>
          </div>

          <div class="row q-my-md">
            <p class="q-pr-md">보기 3. </p>
            <p class="bg-green-13 border-left3" :style="{width: item.purcentNum[2]-20 + '%'}"></p>
            <p class="q-px-sm">{{ item.multiple_bogi[2]}}</p>
            <p>({{ item.num3 }})</p>
          </div>

          <div class="row q-my-md">
            <p class="q-pr-md">보기 4. </p>
            <p class="bg-purple-13 border-left4" :style="{width: item.purcentNum[3]-20 + '%'}"></p>
            <p class="q-px-sm">{{ item.multiple_bogi[3]}}</p>
            <p>({{ item.num4 }})</p>
          </div>

          <div class="row q-my-md">
            <p class="q-pr-md">보기 5. </p>
            <p class="bg-grey-13 border-left5" :style="{width: item.purcentNum[4]-20 + '%'}"></p>
            <p class="q-px-sm">{{ item.multiple_bogi[4]}}</p>
            <p>({{ item.num5 }})</p>
          </div>
        </q-card-section>
      </q-card>

      <q-card class="q-mb-lg" v-else-if="!item.multiple_bogi">
        <q-card-section class="row justify-between items-center" @click="onQuestion">
          <p class="title-size">문항 {{ item.question_number }} . {{ item.survey_question }}</p>
          <div>
            <p @click="openModal = true, onQuestion(item.id)" class="q-pr-sm bordet-bot cursor-pointer">답변 보기</p>
          </div>
        </q-card-section>
      </q-card>
    </div>
    
    <div class="btn-mag row justify-center">
      <q-btn @click="goSurvey" class="text-size q-px-xl q-py-md" color="grey-8" label="목록"></q-btn>
    </div>
    <!-- 주관식 답변 (모달) -->
    <q-dialog v-model="openModal">
      <q-card style="min-width:80%; min-height:80%">
        <div v-if="surveyQuestion[0]">
          <q-card-section class="q-mt-md">
            <p class="title-size">{{ surveyQuestion[0].question.survey_question }}</p>
          </q-card-section>
  
          <q-card-section v-for="(question,index) in surveyQuestion" :key="index">
            <p class="text-size question-bod q-pa-sm"> {{ question.content }}</p>
          </q-card-section>
        </div>

        <div v-else-if="!surveyQuestion[0]">
          <q-card-section class="q-mt-md">
            <p class="title-size">현재 답변한 내용이 없습니다.</p>
          </q-card-section>
        </div>

      </q-card>
    </q-dialog>

  </div>
</template>

<script>
import { ref } from 'vue'
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'SurveyStat',
  data() {
    return {
      surveyPk : this.$route.params.surveyPk
    }
  },
  setup() {
    return {
      openModal: ref(false),
    }
  },
  computed: {
    ...mapGetters(['surveyStat', 'surveyQuestion'])
  },
  methods: {
    ...mapActions(['getSurveyStat', 'onQuestion']),
    goSurvey() {
      this.$router.push({name:'Survey'})
    }
  },
  mounted() {
    this.getSurveyStat(this.surveyPk)
  }
}
</script>

<style scoped>
  p {
    margin: 0;
  }
  .text-size {
    font-size: 2vmin;
  }
  .title-size {
    font-size : 2.5vmin;
  }
  .border-left1 {border-left : 1px solid #FF1744;}
  .border-left2 {border-left : 1px solid #2979FF;}
  .border-left3 {border-left : 1px solid #00E676;}
  .border-left4 {border-left : 1px solid #D500F9;}
  .border-left5 {border-left : 1px solid #BDBDBD;}

  .bordet-bot {
    color: #3D5AFE
  }
  .question-bod {
    border: 2px solid grey;
    border-radius: 10px;
  }
  .btn-mag {
    margin-top: 100px;
  }
</style>