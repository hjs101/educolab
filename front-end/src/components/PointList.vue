<template>
  <div class="q-pa-md">
    <q-card>
      <q-card-section>
        <div class="text-h6">상/벌점 내역</div>
      </q-card-section>
      <q-markup-table>
        <thead>
          <tr>
            <!-- <th class="text-center">번호</th> -->
            <th class="text-center">날짜</th>
            <th class="text-center">상세 내역</th>
            <th class="text-center">추가 점수</th>
            <th class="text-center">현재 상점</th>
            <th class="text-center">누적 벌점</th>
          </tr>
        </thead>
        <tbody v-for="each in point.slice((page-1)*10, page*10)" :key="each.id">
          <tr>
            <!-- <td class="text-center">{{each.id}}</td> -->
            <td class="text-center">{{each.created_at}}</td>
            <td class="text-center">{{each.content}} ({{each.teacher.name}})</td>
            <td class="text-center">{{each.point}}</td>
            <td class="text-center">{{each.acc_point}}</td>
            <td class="text-center">{{each.acc_minus}}</td>
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