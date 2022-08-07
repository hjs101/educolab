<template>
  <div>
    {{task.id}}
    <header>
      {{task.title}} | {{date}} |
      <!-- 학생이 볼 때만 교사 이름 보임? -->
      <span>
        {{task.teacher.name}} |
      </span>
        {{task.subject}} |
        <!-- 채점 완료? -->
        채점 완료 여부 : {{task['check_flag']}}
    </header>
    <article>
      제출기한 : {{task.deadline}}
      <br>
      {{task.content}} | 첨부파일
      <div v-for="file in task['teacher_file']" :key="file">
        <a :href="url+file['atch_file']" class="button">{{file['atch_file_name']}}</a>
      </div>
    </article>
    <!-- 교사용 -->
    <article v-if="isTeacher">
      <q-btn color="primary" label="채점 완료" />
      여기에 학생 정보가 들어감
      <q-list bordered class="rounded-borders" v-for="item in task['student_submit']" :key="item.student?.username">
        <task-target-student :item="item['student_submit']" />
      </q-list>
    </article>
  </div>
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
    return {
      task,
      url,
      date
    }
  },
}
</script>