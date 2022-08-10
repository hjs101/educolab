<template>
  <q-card flat bordered>
    <h1>과제 상세 페이지</h1>
    <section>
      <!-- 과제 내용 & 교사용 -->
      <task-detail-content v-if="!isEmptyTask" :task="task" :isLecture="isLecture" :isTeacher="user.isTeacher"/>
      <!-- 학생용 -->
      <section v-if="!user.isTeacher">
      <!-- 채점 안 한 과제 -->
        <student-task-submit v-if="isLecture && !isSubmit" />
        <!-- 채점한 과제 -->
        <student-submit-content v-else />
      </section>
      <!-- 자신이 만든 페이지에서만 보임 -->
      <div class="buttonGroup">
        <router-link
          class="button"
          :to="{name: 'TaskUpdateView', params: {
          userType: user.type, taskPk:pk
        }}">
          <q-btn color="primary" label="수정"/>
        </router-link>
        <q-btn color="primary" label="삭제" @click="confirm.prompt = true"/>
        <!-- 여기에 삭제 확인 메시지 -->
        <message-pop-up
          v-if="confirm.isTrue"
          title="삭제 확인"
          message="정말 삭제하시겠습니까?"
          :cancel="true"
          :reload="true"
          :path="user.path"
          @reverse="deleteTask"
        />
        <router-link :to="user.path" class="button">
          <q-btn color="primary" label="목록"/>
        </router-link>
      </div>
    </section>
  </q-card>
</template>

<script>
import {computed, onMounted, reactive} from 'vue'
import {useStore} from 'vuex'
import {useRoute} from 'vue-router'
import {isEmpty} from 'lodash'
import StudentTaskSubmit from '@/components/StudentTaskSubmit.vue'
import TaskDetailContent from '@/components/TaskDetailContent.vue'
import MessagePopUp from '@/components/MessagePopUp.vue'
import StudentSubmitContent from '@/components/StudentSubmitContent.vue'
export default {
  name: 'TaskDetailView',
  components: {
    StudentTaskSubmit,
    TaskDetailContent,
    MessagePopUp,
    StudentSubmitContent,
  },
  setup() {
    const route = useRoute()
    const store = useStore()
    const pk = route.params.taskPk
    const isLecture = computed(() => route.params.taskType === 'lecture'? 1:0)
    onMounted(() => {
      store.dispatch('taskDetail', {
        pk,
        teacher_flag: isLecture.value
      })
    })
    const task = computed(() => store.getters.getTask)
    const isEmptyTask = computed(() => isEmpty(task.value))
    
    const confirm = reactive({
      prompt: false,
      isTrue: computed(() => confirm.prompt)  
    })
    const user = reactive({
      type: route.params.userType,
      isTeacher: computed(() => user.type === 'teacher'),
      path: computed(() => user.isTeacher? '/teacher/task':'/student/task')
      })
    const deleteTask = (signal) => {
      if (signal) {
        const data = {
          pk,
          teacher: user.isTeacher,
        }
        store.dispatch('taskDelete', data)
      }
      confirm.prompt = false
    }
    const isSubmit = computed(() => {
        if (isLecture.value) {
          if (task.value.student_submit) {
            return task.value.student_submit[0].submit_flag
          }
        } else if (task.value.my_submit) {
          return task.value.my_submit[0].submit_flag
        }
        return false
      })

    return {
      user,
      task,
      pk,
      confirm,
      deleteTask,
      isSubmit,
      isEmptyTask,
      isLecture
    }
  },
}
</script>