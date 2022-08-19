<template>
  <div>
    <q-card class="my-card bg-cyan-13">

      <q-card-section class="row justify-between items-center card-bt">
        <div class="text-h6">누적 포인트 랭킹</div>
      </q-card-section>

      <q-markup-table>
        <tbody v-for="(mainAccRank, index) in mainAccRank" :key="index">
          <tr v-if="index+1 == 1" class="bg-pink-13">
            <td class="text-size text-center">{{ index+1 }}등.</td>
            <td class="text-size text-center">{{ mainAccRank.name }}</td>
            <td class="text-size text-center">{{ mainAccRank.grade }}학년</td>
            <td class="text-size text-center">{{ mainAccRank.class_field }}반</td>
            <td class="text-size text-center">{{ mainAccRank.acc_point }}p</td>
          </tr>

          <tr v-else-if="index+1 == 2" class="bg-indigo-13">
            <td class="text-size text-center">{{ index+1 }}등.</td>
            <td class="text-size text-center">{{ mainAccRank.name }}</td>
            <td class="text-size text-center">{{ mainAccRank.grade }}학년</td>
            <td class="text-size text-center">{{ mainAccRank.class_field }}반</td>
            <td class="text-size text-center">{{ mainAccRank.acc_point }}p</td>
          </tr>

          <tr v-else-if="index+1 == 3" class="bg-green-13">
            <td class="text-size text-center">{{ index+1 }}등.</td>
            <td class="text-size text-center">{{ mainAccRank.name }}</td>
            <td class="text-size text-center">{{ mainAccRank.grade }}학년</td>
            <td class="text-size text-center">{{ mainAccRank.class_field }}반</td>
            <td class="text-size text-center">{{ mainAccRank.acc_point }}p</td>
          </tr>

          <tr v-else>
            <td class="text-size text-center">{{ index+1 }}등.</td>
            <td class="text-size text-center">{{ mainAccRank.name }}</td>
            <td class="text-size text-center">{{ mainAccRank.grade }}학년</td>
            <td class="text-size text-center">{{ mainAccRank.class_field }}반</td>
            <td class="text-size text-center">{{ mainAccRank.acc_point }}p</td>
          </tr>
        </tbody>
      </q-markup-table>
      
    </q-card>
  </div>
</template>

<script>
export default {
  name:'MainAccRank',
  props: {
    mainAccRank: Object,
  }
}
</script>

<style scoped>
  .text-size {font-size:1rem;}
  .card-bt {
    border-bottom: 1px solid #99DFF9;
  }
  .my-card {
    width: 400px;
  }
</style>