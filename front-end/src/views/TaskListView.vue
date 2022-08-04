<template>
  <main>
    <h1>{{userType}} 과제 페이지</h1>
    <section class="q-pa-md">
      <!-- 검색창 + 검색했을 때 결과 -->
      <search-task/>
      <!-- 검색하지 않았을 때 -->
      <article class="q-gutter-y-md" style="max-width: 800px">
        <student-task-tab v-if="!isTeacher"/>
        <teacher-task-tab v-else />
      </article>
    </section>
  </main>
</template>

<script>
import {useRoute} from 'vue-router'
import SearchTask from '@/components/SearchTask.vue'
import StudentTaskTab from '@/components/StudentTaskTab.vue'
import TeacherTaskTab from '@/components/TeacherTaskTab.vue'
import { computed } from '@vue/runtime-core'
export default {
  name: 'StudentTaskListView',
  components: {
    SearchTask,
    StudentTaskTab,
    TeacherTaskTab,
  },
  setup () {
    const route = useRoute()
    const userType = route.params.userType
    const isTeacher = computed(() => userType === 'teacher')
    return {
      userType,
      isTeacher
    }
  }
}
</script>
