<template>
  <q-card-section>
    <q-card-section>
      {{task.homework?.id || task.id}}
      <div class="text-h6">{{task.homework?.title || task.title}}</div>
      <!-- {{date}} -->
    </q-card-section>

    <q-card-section class="q-pt-none">
      <header>
        <span v-if="isLecture"> {{task.homework['check_flag']? '채점 완료':'채점 미완료'}}</span>
        <span v-else> {{task.agreement? '채점 완료':'채점 미완료'}}</span>
      </header>
      <article>
        제출기한 : {{task.homework?.deadline || task.deadline}}
        <br>
        <!-- 학생용 과제 제출 안 한 상세 페이지에는 안 보이게 -->
        <div>
          내용 : {{task.homework?.content || task.content}}
          <br>
          첨부파일 :
          <div v-for="file in files" :key="file">
            <a :href="url+file['atch_file']" class="button">{{file['atch_file_name']}}</a>
          </div>
        </div>
      </article>
      <hr>
      <!-- 교사용 -->
      <article v-if="isTeacher">
        <!-- 자신이 작성한 상세 페이지에서 -->
        <div v-if="isLecture">
          <q-list bordered class="rounded-borders" v-for="item in task.student_submit" :key="item.id">
            <task-target-student :item="item" />
          </q-list>
        </div>
        <!-- 학생이 작성한 과제 상세 페이지에서 -->
        <div v-else>
          <q-input v-if="task.student" type="number" label="점수" min="-1" max="5"/>
          <div  v-if="!task.homework?.check_flag">
            <q-btn color="primary" label="채점 완료" @click="checkComplete" />
          </div>
        </div>
          <hr>
      </article>
    </q-card-section>
  </q-card-section>
</template>

<script>
// import {useStore} from 'vuex'
import {computed} from 'vue'
import drf from '@/api/drf.js'
// import dayjs from 'dayjs'
import TaskTargetStudent from '@/components/TaskTargetStudent.vue'
export default {
  name: 'TaskDetailContent',
  components: {
    TaskTargetStudent,
  },
  props: {
    isTeacher: Boolean,
    task: Object,
    isLecture: Number,
  },
  setup(props) {
    // const store = useStore()
    const url = drf.file.path()
    let checkState = computed(() => {
      if (props.isLecture) {
        return props.task.homework['check_flag']? '채점 완료':'채점 미완료'
      } else {
        return props.task['agreement']? '채점 완료':'채점 미완료'
      }
    })
    const files = computed(() => props.isLecture? props.task.homework['teacher_file']: props.task['student_file'])
    // const date = computed(() => {
    //   if (!props.params.teacher_flag) {
    //     return dayjs(props.task['updated_at']).format('YYYY-MM-DD HH:mm')
    //   } else {
    //     return dayjs(props.task.homework['updated_at']).format('YYYY-MM-DD HH:mm')
    //   }
    // })
    const checkComplete = () => {
      
    }
    return {
      url,
      // date,
      checkState,
      checkComplete,
      checkTask,
      files
    }
  },
}
</script>