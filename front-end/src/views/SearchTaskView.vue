<template>
  <article div class="baseStyle">
    <h4 class="text-center">과제 검색</h4>
    <hr>
    <div class="q-pa-md">
      <article class="row items-baseline justify-center">
        <q-input
          label="과제 제목검색"
          v-model="search.query"
          class="col-5 q-mr-md"
          @keyup.enter="refresh"/>
        <q-btn
          color="primary"
          label="검색"
          class="col-1 text-size q-mx-lg q-py-sm"
          @click="refresh" />
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
import {useRoute, useRouter} from 'vue-router'
import TaskListTable from '@/components/TaskListTable.vue'
import ThePagination from '@/components/ThePagination.vue'
import {isEmpty} from 'lodash'
export default {
  name: 'SearchTask',
  components: {
    TaskListTable,
    ThePagination
  },
  setup() {
    const store = useStore()
    const route = useRoute()
    const router = useRouter()
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
    const refresh = () => {
      router.push({name: 'SearchTaskView', params:{userType,}, query:{query:search.query}})
      router.go(1)
    }
    onBeforeMount(() => {
      if (!store.getters.isLoggedIn) {
        router.push('educolab/login/')
      } else if (isEmpty(taskList.value)) {
        store.dispatch('taskList')
      }
    })
    return {
      taskList,
      page,
      userType,
      changePage,
      search,
      refresh
    }
  }
}
</script>

<style scoped>
  .text-size{font-size: 1rem;}
</style>