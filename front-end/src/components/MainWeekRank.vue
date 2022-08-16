<template>
  <div>
    <q-card class="my-card bg-orange-13">
      <q-card-section class="row justify-between items-center card-bt">
        <div class="text-h6">저번주 포인트 랭킹</div>
      </q-card-section>

      <q-markup-table>
        <tbody class="text-center" v-for="(mainWeekRank, index) in mainWeekRank" :key="index">
          <tr v-if="index+1 == 1" class="bg-pink-13">
            <td class="text-size">{{ index+1 }}등.</td>
            <td class="text-size">{{ mainWeekRank.student }}</td>
            <td class="text-size">학년</td>
            <td class="text-size">반</td>
            <td class="text-size">{{ mainWeekRank.score }}p</td>
          </tr>

          <tr v-else-if="index+1 == 2" class="bg-indigo-13">
            <td class="text-size">{{ index+1 }}등.</td>
            <td class="text-size">{{ mainWeekRank.student }}</td>
            <td class="text-size">학년</td>
            <td class="text-size">반</td>
            <td class="text-size">{{ mainWeekRank.score }}p</td>
          </tr>

          <tr v-else-if="index+1 == 3" class="bg-green-13">
            <td class="text-size">{{ index+1 }}등.</td>
            <td class="text-size">{{ mainWeekRank.student }}</td>
            <td class="text-size">학년</td>
            <td class="text-size">반</td>
            <td class="text-size">{{ mainWeekRank.score }}p</td>
          </tr>

          <tr v-else>
            <td>{{ index+1 }}등.</td>
            <td>{{ mainWeekRank.student }}</td>
            <td>학년</td>
            <td>반</td>
            <td>{{ mainWeekRank.score }}p</td>
          </tr>
        </tbody>
      </q-markup-table>
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
  .text-size { font-size: 1rem;}
  .my-card {
    width:400px;  
  }
  .card-bt {
    border-bottom: 1px solid #FF9966
  }
</style>