<template>
  <article div class="q-gutter-md" style="max-width: 300px">
    <q-input label="제목 검색" v-model="search.query"/>
    <q-btn color="primary" label="검색" @click="search.search = search.query"/>
    <br>
    검색 결과
    <div v-for="num in taskLength" :key="num">
      <div v-if="num === page">
        <q-list bordered class="rounded-borders" v-for="item in taskList.slice((num-1)*10, num*10)" :key="item.id">
          <task-item v-if="item.title.includes(search.search)" :item = item :teacher="1" :submit="false" />
        </q-list>
      </div>
    </div>
    <the-pagination
      v-if="taskLength"
      :limit="taskLength"
      @change-page="changePage" />
    <q-btn color="primary" label="메인" />
  </article>
</template>

<script>
import {onBeforeMount, ref, computed, reactive} from 'vue'
import {useStore} from 'vuex'
import {useRoute} from 'vue-router'
import TaskItem from '@/components/TaskItem.vue'
import ThePagination from '../components/ThePagination.vue'
// import {isEmpty} from 'lodash'
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
    const search = reactive({
      query: route.query.query,
      search: route.query.query,
    })
    const taskList = computed(() => userType === 'teacher'? store.getters.getTeacherAll : store.getters.getStudentAll)
    const taskLength = computed(() => userType === 'teacher'? store.getters.cntTeacherAll : store.getters.cntStudentAll)
    let page = ref(1)
    const changePage = (value) => {
      page.value = value
    }
    onBeforeMount(() => {
      // console.dir(taskList)
      // if (isEmpty(taskList)) {
      //   store.dispatch('taskList')
      // }
    })
    return {
      taskList,
      taskLength,
      store,
      page,
      changePage,
      search
    }
  }
}
</script>