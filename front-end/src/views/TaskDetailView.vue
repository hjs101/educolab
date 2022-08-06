<template>
  <div>
    <h1>과제 상세 페이지</h1>
    <section>
      <!-- 과제 내용 & 교사용 -->
      <task-detail-content />
      <!-- 학생용 -->
      <student-task-submit v-if="!user.isTeacher" />
      <!-- 자신이 만든 페이지에서만 보임 -->
      <div>
        <router-link
          class="button"
          :to="{name: 'TaskUpdateView', params: {
          userType: user.type, taskPk:taskPk
        }}">
          <q-btn color="primary" label="수정"/>
        </router-link>
        <q-btn color="primary" label="삭제" @click="confirm = true"/>
        <!-- 여기에 삭제 확인 메시지 -->
      </div>
      <router-link :to="user.path" class="button">
        <q-btn color="primary" label="목록"/>
      </router-link>
    </section>
  </div>
</template>

<script>
import {computed, reactive, ref} from 'vue'
import {useStore} from 'vuex'
import {useRoute} from 'vue-router'
import StudentTaskSubmit from '@/components/StudentTaskSubmit.vue'
import TaskDetailContent from '@/components/TaskDetailContent.vue'
export default {
  name: 'TaskDetailView',
  components: {
    StudentTaskSubmit,
    TaskDetailContent,
  },
  created() {
    const route = useRoute()
    const store = useStore()
    store.dispatch('taskDetail', route.params.taskPk)
  },
  setup() {
    const route = useRoute()
    let taskPk = ref(route.params.taskPk)
    const user = reactive({
      type: route.params.userType,
      isTeacher: computed(() => user.type === 'teacher'),
      path: computed(() => user.isTeacher? '/teacher/task':'/student/task')
      })
    
    return {
      taskPk,
      user,
    }
  },
}
</script>