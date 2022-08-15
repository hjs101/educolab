<template>
  <q-card-section>
    <q-card-section>
      {{task.homework?.id || task.id}}
      <div class="text-h6">{{task.homework?.title || task.title}}</div>
      {{date}}
    </q-card-section>

    <q-card-section class="q-pt-none">
      <header>
        <span v-if="isLecture.value"> {{task.homework['check_flag']? '채점 완료':'채점 미완료'}}</span>
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
          <q-btn color="primary" label="채점 완료" @click="checkComplete" v-if="check.possible" />
          <q-list bordered class="rounded-borders" v-for="item in task.student_submit" :key="item.id">
            <task-target-student
              :item="item"
              :deadline="task.homework?.deadline"
              :totalCheckFlag="task.homework?.check_flag"
              :checkFlag="item.check_flag"/>
          </q-list>
          <!-- 채점 완료 팝업 -->
          <message-pop-up
            v-if="check.confirm"
            message="채점이 완료되었습니다"
            path="/teacher/task"
            @reverse="check.prompt = false"
          />
        </div>
        <!-- 학생이 작성한 과제 상세 페이지에서 -->
        <div v-else-if="!task.agreement">
          <q-input v-if="task.student" v-model="point" type="number" label="점수" min="-1" max="5"/>
          <div  v-if="!task.homework?.check_flag">
            <q-btn color="primary" label="채점 완료" @click="checkStudent" />
          </div>
          <hr>
          <message-pop-up
            v-if="check.confirmStudent"
            message="채점이 완료되었습니다"
            path="/teacher/task"
            @reverse="check.student = false"
          />
        </div>
      </article>
    </q-card-section>
  </q-card-section>
</template>

<script>
import {useStore} from 'vuex'
import {computed, reactive, ref} from 'vue'
import {useRoute} from 'vue-router'
import drf from '@/api/drf.js'
import dayjs from 'dayjs'
import axios from 'axios'
import TaskTargetStudent from '@/components/TaskTargetStudent.vue'
import MessagePopUp from '@/components/MessagePopUp.vue'
export default {
  name: 'TaskDetailContent',
  components: {
    TaskTargetStudent,
    MessagePopUp
  },
  props: {
    isTeacher: Boolean,
    task: Object,
    pk: String,
  },
  setup(props) {
    const store = useStore()
    const route = useRoute()
    const url = drf.file.path()
    let isLecture = ref(computed(() => route.params.taskType === 'lecture'? 1:0))
    let point = ref(null)
    const check = reactive({
      state: computed(() => {
        if (isLecture.value) {
          return props.task.homework['check_flag']? '채점 완료':'채점 미완료'
        } else {
          return props.task['agreement']? '채점 완료':'채점 미완료'
        }
      }),
      prompt: false,
      confirm: computed(() => check.prompt),
      possible: computed(() => {
        if (props.task.homework?.deadline >= dayjs().format('YYYY-MM-DD') || props.task.homework?.check_flag) {
          return false
        } else {
          return true
        }
      }),
      student: false,
      confirmStudent: computed(() => check.student)
    })
    
    const files = computed(() => {
      if (isLecture.value) {
        return props.task.homework?.teacher_file
      } else {
        return props.task.student_file
      }
    })
    const date = computed(() => {
      if (!isLecture.value) {
        return dayjs(props.task.updated_at).format('YYYY-MM-DD HH:mm')
      } else {
        return dayjs(props.task.homework?.updated_at).format('YYYY-MM-DD HH:mm')
      }
    })
    const data = {
      teacher_flag: isLecture.value+'',
      pk: props.pk
    }
    const checkComplete = () => {
      axios({
        url: drf.task.checkDone(),
        method: 'post',
        headers: store.getters.authHeader,
        data,
      })
        .then(() => {
          check.prompt = true
        })
        .catch((err) => {
          console.log(err)
        })
    }
    const checkStudent = () => {
      axios({
        url: drf.task.check(),
        method: 'post',
        headers: store.getters.authHeader,
        data: {
          ...data,
          username: props.task.student.username,
          point: point.value * 1,
        }
      })
      .then((() => {
        axios({
          url: drf.task.checkDone(),
          method: 'post',
          headers: store.getters.authHeader,
          data,
        })
          .then((() => {
            check.student = true
          }))
          .catch((err) => {
            console.log(err)
          })
      }))
      .catch((err) => {
        console.log(err)
      })
    }
    return {
      url,
      date,
      check,
      checkComplete,
      checkStudent,
      point,
      files,
      isLecture,
    }
  },
}
</script>