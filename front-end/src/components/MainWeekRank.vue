<template>
  <div>
    <q-card class="my-card bg-orange-13">
      <q-card-section class="row justify-between items-center card-bt">
        <div class="text-h6">저번주 포인트 랭킹</div>
      </q-card-section>

      <q-card-section v-for="mainWeekRank in mainWeekRank" :key="mainWeekRank"
      class="row items-center card-pad">
        <div class="q-px-sm text-subtitle2">{{ mainWeekRank }}</div>
      </q-card-section>
    </q-card>
  </div>
</template>

<script>
export default {
  name: 'MainWeekRank',
  props: {
    mainWeekRank: Object
  }
}
</script>

<style scoped>
  .my-card {
    width:400px;  
  }
  .card-bt {
    border-bottom: 1px solid #FF9966
  }
</style>