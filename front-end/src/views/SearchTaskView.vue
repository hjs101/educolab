<template>
  <article div class="baseStyle">
    <h4 class="text-center">과제 검색</h4>
    <hr>
    <div class="q-pa-md">
      <article class="row items-baseline justify-evenly">
        <q-input label="과제 제목검색" v-model="query" class="col-8" />
        <router-link class="button" :to="{name: 'SearchTaskView', params:{userType,}, query:{query,}}" >
          <q-btn color="primary" label="검색" class="col-3" />
        </router-link>
      </article>
    </div>
    <h6 class="text-center q-pa-sm">검색 결과</h6>
    <q-list
      bordered
      class="rounded-borders">
      <task-list-table
        :list="search.list"
        :page="page"
        :teacher="0"
      />
    </q-list>
    <the-pagination
      v-if="search.length"
      :limit="search.length"
      @change-page="changePage" />
    <a :href="`/${userType}/task`" class="button row justify-center q-pa-lg">
      <q-btn color="primary" label="과제 메인" />
    </a>
  </article>
</template>

<script>
import {onBeforeMount, ref, computed, reactive} from 'vue'
import {useStore} from 'vuex'
import {useRoute} from 'vue-router'
import TaskListTable from '@/components/TaskListTable.vue'
import ThePagination from '@/components/ThePagination.vue'
// import {isEmpty} from 'lodash'
export default {
  name: 'SearchTask',
  components: {
    TaskListTable,
    ThePagination
  },
  setup() {
    const store = useStore()
    const route = useRoute()
    let {userType} = route.params
    const taskList = computed(() => userType === 'teacher'? store.getters.getTeacherAll : store.getters.getStudentAll)
    const search = reactive({
      query: route.query.query,
      search: route.query.query,
      list: computed(() => taskList.value.filter(element => {
        return element.title.includes(search.search)
      })),
      length: computed(() => Math.ceil(search.list.length/10))
    })
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
      page,
      userType,
      changePage,
      search
    }
  }
}
</script>