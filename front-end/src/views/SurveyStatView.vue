<template>
  <div>
    <h1>설문조사 통계</h1>
    <hr>
    <h3>설문조사 제목 : {{ surveyStat.survey_title }}</h3>
    <div v-for="item in surveyStat" :key="item">
      <div v-for="index in item" :key="index">
        <div class="row" v-if="index.multiple_bogi !== null">
          <p>{{ index.num1 }}</p>
          <p>{{ index.num2 }}</p>
          <p>{{ index.num3 }}</p>
          <p>{{ index.num4 }}</p>
          <p>{{ index.num5 }}</p>        
        </div>
        <div v-if="index.multiple_bogi">
          <p>{{ index.question_number }} . {{ index.survey_question }}</p>
        </div>
        <div v-else-if="index.multiple_bogi === null">
          <button @click="onQuestion(index.id)">
            {{ index.question_number }} . {{ index.survey_question }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'SurveyStat',
  computed: {
    ...mapGetters(['surveyStat',])
  },
  methods: {
    ...mapActions(['onQuestion'])
  }
}
</script>

<style>

</style>