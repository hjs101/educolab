<template>
  <main>
    <h1>{{userType}} 과제 페이지</h1>
    <section class="q-pa-md">
      <!-- 검색창 + 검색했을 때 결과 -->
      <search-task/>
      <!-- 검색하지 않았을 때 -->
      <article class="q-gutter-y-md" style="max-width: 800px">
        <router-link
        :to="{name:'TaskCreateView', params:{userType,}}"
        class="button">
          <q-btn color="primary" label="과제 생성" />
        </router-link>
        <student-task-tab v-if="!isTeacher"/>
        <teacher-task-tab v-else />
      </article>
    </section>
  </main>
</template>

<script>
import {useRoute} from 'vue-router'
import {useStore} from 'vuex'
import { computed, onBeforeMount, onMounted } from 'vue'
import SearchTask from '@/components/SearchTask.vue'
import StudentTaskTab from '@/components/StudentTaskTab.vue'
import TeacherTaskTab from '@/components/TeacherTaskTab.vue'
export default {
  name: 'StudentTaskListView',
  components: {
    SearchTask,
    StudentTaskTab,
    TeacherTaskTab,
  },
  setup () {
    const route = useRoute()
    const store = useStore()
    const {userType} = route.params
    const isTeacher = computed(() => userType === 'teacher')
    onBeforeMount(() => {
      // 현재 로그인이 되어있는지 확인 (토큰이 있는지 확인)
      // 현재 사용자 타입과 로그인한 사용자 타입이 맞는지 확인
      // 데이터 받아오기
    })
    onMounted(() => {
      store.dispatch('taskList')
    })
    return {
      userType,
      isTeacher
    }
  }
}
</script>
