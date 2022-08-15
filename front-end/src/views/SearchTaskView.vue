<template>
  <article div class="q-gutter-md baseStyle" style="max-width: 300px" >
    <q-input label="제목 검색" v-model="search.query"/>
    <!-- a 태그로 바꿀 예정 -->
    <router-link :to="{name: 'SearchTaskView', params:
    {userType,}, query: {query: search.query}}" class="button">
      <q-btn color="primary" label="검색"/>
    </router-link>
    <br>
    검색 결과
    <q-list bordered class="rounded-borders" v-for="item in search.list.slice((page-1)*10, page*10)" :key="item.id">
      <task-item :item = item :teacher="1" :submit="false" />
    </q-list>
    <the-pagination
      v-if="search.length"
      :limit="search.length"
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