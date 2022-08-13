<template>
  <div>
    <div class="center" v-if="bogi">
      <div class="column items-start bogi-size">
        <div class="row items-center q-ml-md">
          <p>보기 1.</p>
          <p class="q-mx-md q-px-md bogi-border" style="width:500px;">
          {{ surveyBogi[surveyItem.question_number][0] }}</p>
        </div>
        <div class="row items-center q-ml-md">
          <p>보기 2.</p>
          <p class="q-mx-md q-px-md bogi-border" style="width:500px;">
          {{ surveyBogi[surveyItem.question_number][1] }}</p>
        </div>
        <div class="row items-center q-ml-md">
          <p>보기 3.</p>
          <p class="q-mx-md q-px-md bogi-border" style="width:500px;">
          {{ surveyBogi[surveyItem.question_number][2] }}</p>
        </div>
        <div class="row items-center q-ml-md">
          <p>보기 4.</p>
          <p class="q-mx-md q-px-md bogi-border" style="width:500px;">
          {{ surveyBogi[surveyItem.question_number][3] }}</p>        
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
    font-size : 1.2rem;
  }
  .bogi-border {
    border-style: inset;
  }
</style>