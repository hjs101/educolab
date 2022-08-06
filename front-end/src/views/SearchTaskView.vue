<template>
  <article div class="q-gutter-md" style="max-width: 300px">
    <q-input label="과제 검색" v-model="query"/>
    <q-btn color="primary" label="검색" />
    <div v-for="item in taskList.value" :key="item.pk">
      <task-item :item="item" />
    </div>
    <q-btn color="primary" label="메인" />
    <the-pagination
      v-if="length.value"
    />
      <!-- v-if="number.notDone"
      :limit="number.notDone"
      @change-page="changePage" -->
  </article>
</template>

<script>
import {onBeforeMount, ref} from 'vue'
import {useStore} from 'vuex'
import {useRoute} from 'vue-router'
import TaskItem from '@/components/TaskItem.vue'
import ThePagination from '../components/ThePagination.vue'
import {isEmpty} from 'lodash'
export default {
  name: 'SearchTask',
  components: {
    TaskItem,
    ThePagination
  },
  setup() {
    const store = useStore()
    const route = useRoute()
    let {userType} = route.params
    let query = ref(route.query.query)
    const taskList = ref(userType === 'teacher'? store.getters.getTeacherAll : store.getters.getStudentAll)
    const length = ref(userType === 'teacher'? store.getters.cntTeacherAll: store.getters.cntStudentAll)
    onBeforeMount(() => {
      if (isEmpty(taskList)) {
        store.dispatch('taskList')
      }
    })
    return {
      taskList,
      query,
      length
    }
  }
}
</script>