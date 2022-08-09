<template>
  <q-card-section>
    <q-card-section>
      {{task.id}}
      <div class="text-h6">{{task.title}} | {{date}}</div>
    </q-card-section>

    <q-card-section class="q-pt-none">
      <header>
        <span> {{checkState}}</span>
      </header>
      <article>
        제출기한 : {{task.deadline}}
        <br>
        <!-- 학생용 과제 제출 안 한 상세 페이지에는 안 보이게 -->
        <div>
          내용 : {{task.content}}
          <br>
          첨부파일 :
          <div v-for="file in task['teacher_file']" :key="file">
            <a :href="url+file['atch_file']" class="button">{{file['atch_file_name']}}</a>
          </div>
        </div>
      </article>
      <hr>
      <!-- 교사용 -->
      <article v-if="isTeacher">
        <!-- 학생이 작성한 과제 상세 페이지에서 -->
        <q-input v-if="task.student" type="number" label="점수" min="-1" max="5"/>
        <div  v-if="!task['check_flag']">
          <q-btn color="primary" label="채점 완료" @click="checkComplete" />
          <hr>
        <!-- 자신이 작성한 상세 페이지에서 -->
          <q-list bordered class="rounded-borders" v-for="item in task['student_submit']" :key="item.student?.username">
            <task-target-student :item="item" />
          </q-list>
        </div>
      </article>
    </q-card-section>
  </q-card-section>
</template>

<script>
import {useStore} from 'vuex'
import {computed} from 'vue'
import drf from '@/api/drf.js'
import dayjs from 'dayjs'
import TaskTargetStudent from '@/components/TaskTargetStudent.vue'
export default {
  name: 'TaskDetailContent',
  components: {
    TaskTargetStudent,
  },
  props: {
    isTeacher: Boolean,
  },
  setup() {
    const store = useStore()
    const task = computed(() => store.getters.getTask)
    const url = drf.file.path()
    const date = dayjs(task.value['updated_at']).format('YYYY-MM-DD HH:mm')
    let checkState = computed(() => task.value['check_flag']? '완료':'미완료')
    const checkComplete = () => {

    }
    return {
      task,
      url,
      date,
      checkState,
      checkComplete
    }
  },
}
</script>