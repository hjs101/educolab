<template>
  <div>
    <div class="center" v-if="bogi">
      <div class="column items-start bogi-size">

        <div class="row items-center q-ml-md q-mt-md">
          <p>보기 1.</p>
          <p class="q-mx-md" style="max-width:1000px;">
          {{ surveyBogi[surveyItem.question_number][0] }}</p>
        </div>
        <div class="row items-center q-ml-md">
          <p>보기 2.</p>
          <p class="q-mx-md bogi-border" style="max-width:1000px;">
          {{ surveyBogi[surveyItem.question_number][1] }}</p>
        </div>
        <div class="row items-center q-ml-md">
          <p>보기 3.</p>
          <p class="q-mx-md bogi-border" style="max-width:1000px;">
          {{ surveyBogi[surveyItem.question_number][2] }}</p>
        </div>
        <div class="row items-center q-ml-md">
          <p>보기 4.</p>
          <p class="q-mx-md bogi-border" style="max-width:1000px;">
          {{ surveyBogi[surveyItem.question_number][3] }}</p>        
        </div>
        <div class="row items-center q-ml-md">
          <p>보기 5.</p>
          <p class="q-mx-md bogi-border" style="max-width:1000px;">
          {{ surveyBogi[surveyItem.question_number][4] }}</p>        
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
  .bogi-size {
    font-size: 2vmin;
  }
</style>