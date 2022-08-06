<template>
  <main>
    <h1>{{userType}} 과제 페이지</h1>
    <section class="q-pa-md">
      <!-- 검색창-->
      <article div class="q-gutter-md" style="max-width: 300px">
        <q-input label="과제 검색" v-model="query"/>
        <router-link :to="{name: 'SearchTaskView', params:{userType,}, query:{query,}}" >
          <q-btn color="primary" label="검색" />
        </router-link>
      </article>
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
import { computed, onBeforeMount, onMounted, ref } from 'vue'
import StudentTaskTab from '@/components/StudentTaskTab.vue'
import TeacherTaskTab from '@/components/TeacherTaskTab.vue'
export default {
  name: 'StudentTaskListView',
  components: {
    StudentTaskTab,
    TeacherTaskTab,
  },
  setup () {
    const route = useRoute()
    const store = useStore()
    const {userType} = route.params
    const isTeacher = computed(() => userType === 'teacher')
    let search = ref(false)
    let query = ref(null)
    onBeforeMount(() => {
      store.dispatch('taskList')
    })
    onMounted(() => {
    })
    return {
      userType,
      isTeacher,
      search,
      query,
    }
  }
}
</script>
