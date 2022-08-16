<template>
  <div class="q-py-lg" oncontextmenu="return false" onselectstart="return false" >
    <q-card>
      <q-card-section>
        <h5 class="text-center">내 상/벌점</h5>
      </q-card-section>
      <q-markup-table class="q-px-xl">
        <thead>
          <tr>
            <!-- <th class="text-center">번호</th> -->
            <th class="text-center text-size">날짜</th>
            <th class="text-center text-size">상세 내역</th>
            <th class="text-center text-size">추가 점수</th>
            <th class="text-center text-size">현재 상점</th>
            <th class="text-center text-size">누적 벌점</th>
          </tr>
        </thead>
        <tbody v-for="each in point.slice((page-1)*10, page*10)" :key="each.id">
          <tr>
            <!-- <td class="text-center">{{each.id}}</td> -->
            <td class="text-center text-size">{{each.created_at}}</td>
            <td class="text-center text-size">{{each.content}} ({{each.teacher.name}})</td>
            <td class="text-center text-size">{{each.point}}</td>
            <td class="text-center text-size">{{each.acc_point}}</td>
            <td class="text-center text-size">{{each.acc_minus}}</td>
          </tr>
        </tbody>
        <the-pagination
          v-if="cnt"
          :limit="cnt"
          @change-page="changePage"
        />
      </q-markup-table>
    </q-card>
  </div>
</template>

<script>
import {ref} from 'vue'
import ThePagination from '@/components/ThePagination.vue'
export default {
  components: {
    ThePagination
  },
  name: 'PointList',
  props: {
    point: Array,
  },
  setup(props) {
    let cnt = Math.ceil(props.point.length/10)
    let page = ref(1)
    const changePage = (value) => {
      page.value = value
    }
    return {
      cnt,
      page,
      changePage,
    }
  },
}
</script>

<style scoped>
  .text-size{font-size: 1rem;}
  .searchWrap{border-radius:5px; text-align:center; padding:20px 0; margin-bottom:10px;}
  .tbList th{border-top:1px solid #888;}
	.tbList th, .tbList td{border-bottom:1px solid #eee; padding:5px 0;}
	.tbList td.txt_left{text-align:left;}
  .btn{margin-bottom:40px;}
</style>