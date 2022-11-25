<template>
  <main flat bordered class="noticeDetailStyle row justify-center">
    <h4 class="text-center col-12">과제</h4>
    <section class="col-6">
      <!-- 과제 내용 & 교사용 -->
      <task-detail-content class="col-6" v-if="!isEmptyTask" :pk="pk" :task="task" :isTeacher="user.isTeacher"/>
      <!-- 학생용 -->
      <!-- 채점 안 한 과제 -->
      <student-task-submit class="col-6" v-if="!user.isTeacher && isLecture && !task.homework?.check_flag" />
      <!-- 자신이 만든 페이지에서만 보임 -->
      <div class="buttonGroup">
        <div v-if="user.editPossible">
          <router-link
            class="button q-mx-sm"
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
        </div>
        <router-link :to="user.path" class="button">
          <q-btn
            color="primary"
            label="목록"
            class="text-size q-mx-lg q-py-sm"/>
        </router-link>
      </div>
    </section>
  </main>
</template>

<script>
import {computed, onMounted, reactive} from 'vue'
import {useStore} from 'vuex'
import {useRoute, useRouter} from 'vue-router'
import {isEmpty} from 'lodash'
import dayjs from 'dayjs'
import StudentTaskSubmit from '@/components/StudentTaskSubmit.vue'
import TaskDetailContent from '@/components/TaskDetailContent.vue'
import MessagePopUp from '@/components/MessagePopUp.vue'
export default {
  name: 'TaskDetailView',
  components: {
    StudentTaskSubmit,
    TaskDetailContent,
    MessagePopUp,
  },
  setup() {
    const route = useRoute()
    const router = useRouter()
    const store = useStore()
    const pk = route.params.taskPk
    const isLecture = computed(() => route.params.taskType === 'lecture'? 1:0)
    onMounted(() => {
      if (store.getters.isLoggedIn) {
        store.dispatch('taskDetail', {
          pk,
          teacher_flag: isLecture.value
        })
      } else {
        router.push('/educolab/login')
      }
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
      editPossible: computed(() => {
        if (route.params.taskType === 'lecture' && user.type === 'teacher' && task.value.homework?.deadline >= dayjs().format('YYYY-MM-DD')) {
          return true
        } else {
          return false
        }
      }),
      path: computed(() => user.isTeacher? '/teacher/task':'/student/task')

      })
    const deleteTask = (signal) => {
      if (signal) {
        const data = {
          pk,
          teacher_flag: user.isTeacher,
        }
        store.dispatch('taskDelete', data)
      }
      confirm.prompt = false
    }

    return {
      user,
      task,
      pk,
      confirm,
      deleteTask,
      isEmptyTask,
      isLecture
    }
  },
}
</script>

