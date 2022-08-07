<template>
  <div>
    <div class="center" v-if="bogi">
      <div class="row q-pa-md">
        <div class="q-px-md">
          <q-radio disabled/>
          <p class="surveyMargin">{{ surveyBogi[surveyItem.question_number][0] }}</p>
        </div>
        <div class="q-px-md">
          <q-radio disabled/>
          <p class="surveyMargin">{{ surveyBogi[surveyItem.question_number][1] }}</p>
        </div>
        <div class="q-px-md">
          <q-radio disabled/>
          <p class="surveyMargin">{{ surveyBogi[surveyItem.question_number][2] }}</p>
        </div>
        <div class="q-px-md">
          <q-radio disabled/>
          <p class="surveyMargin">{{ surveyBogi[surveyItem.question_number][3] }}</p>
        </div>
        <div class="q-px-md">
          <q-radio disabled/>
          <p class="surveyMargin">{{ surveyBogi[surveyItem.question_number][4] }}</p>
        </div>
      </div>
    </div>  
  </div>
  
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name : 'surveyBogi',
  props: {
    bogi : Number,
    surveyItem : Object,
    qusNumber : Number,
  },
  computed: {
    ...mapGetters(['surveyBogi'])
  },
}
</script>

<style scoped>

</style>