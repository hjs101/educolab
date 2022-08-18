<template>
  <div>
    <q-card class="my-card bg-orange-13">
      <q-card-section class="row justify-between items-center card-bt">
        <div class="text-h6">저번주 포인트 랭킹</div>
      </q-card-section>

      <q-markup-table>
        <tbody v-if="EmptyWeekRank">
          <tr>
            <td class="text-size bg-orange-13">아직 저번주에 대한 랭킹 데이터가 없어요 ㅠㅠ</td>
          </tr>
        </tbody>
        <tbody class="text-center" v-for="(mainWeekRank, index) in mainWeekRank" :key="index">
          <tr v-if="index+1 == 1" class="bg-pink-13">
            <td class="text-size">{{ index+1 }}등.</td>
            <td class="text-size">{{ mainWeekRank.student.name }}</td>
            <td class="text-size">{{ mainWeekRank.student.grade}}학년</td>
            <td class="text-size">{{ mainWeekRank.student.class_field }}반</td>
            <td class="text-size">{{ mainWeekRank.score }}p</td>
          </tr>

          <tr v-else-if="index+1 == 2" class="bg-indigo-13">
            <td class="text-size">{{ index+1 }}등.</td>
            <td class="text-size">{{ mainWeekRank.student.name }}</td>
            <td class="text-size">{{ mainWeekRank.student.grade }}학년</td>
            <td class="text-size">{{ mainWeekRank.student.class_field }}반</td>
            <td class="text-size">{{ mainWeekRank.score }}p</td>
          </tr>

          <tr v-else-if="index+1 == 3" class="bg-green-13">
            <td class="text-size">{{ index+1 }}등.</td>
            <td class="text-size">{{ mainWeekRank.student.name }}</td>
            <td class="text-size">{{ mainWeekRank.student.grade }}학년</td>
            <td class="text-size">{{ mainWeekRank.student.class_field }}반</td>
            <td class="text-size">{{ mainWeekRank.score }}p</td>
          </tr>

          <tr v-else>
            <td class="text-size">{{ index+1 }}등.</td>
            <td class="text-size">{{ mainWeekRank.student.name }}</td>
            <td class="text-size">{{ mainWeekRank.student.grade }}학년</td>
            <td class="text-size">{{ mainWeekRank.student.class_field }}반</td>
            <td class="text-size">{{ mainWeekRank.score }}p</td>
          </tr>
        </tbody>
      </q-markup-table>
    </q-card>
  </div>
</template>

<script>
import { isEmpty } from 'lodash'

export default {
  name: 'MainWeekRank',
  computed: {
    EmptyWeekRank() {
      return isEmpty(this.mainWeekRank)
    }
  },
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