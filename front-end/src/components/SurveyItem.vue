<template>
  <div>
    <select name="" id="" @change="selectedSurvey" v-model="selected">
      <option value="">==문항 선택==</option>
      <option value="choice">객관식 설문조사</option>
      <option value="question">주관식 설문조사</option>
    </select>

    <br>

    <div v-if="selected === 'question'">
      <input type="text">주관식 문제
    </div>

    <div v-else-if="selected === 'choice'">
      <div class="q-pa-md">
        <div class="q-gutter-sm" disabled>
          <q-radio v-model="shape" val="0" label="매우 좋음" />
          <q-radio v-model="shape" val="1" label="좋음" />
          <q-radio v-model="shape" val="2" label="중간" />
          <q-radio v-model="shape" val="3" label="나쁨" />
          <q-radio v-model="shape" val="4" label="매우 나쁨" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {ref} from 'vue'
export default {
  name: 'SurveyItem',
  props: {
    survey: Number,
  },
  setup () {
    return {
      shape: ref(''),
      selected: ref('')
    }
  },
}
</script>