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
          <q-btn color="primary" label="채점 완료" @click="checkComplete" />
          <q-list bordered class="rounded-borders" v-for="item in task.student_submit" :key="item.id">
            <task-target-student :item="item" />
          </q-list>
        </div>
        <!-- 학생이 작성한 과제 상세 페이지에서 -->
        <div v-else>
          <q-input v-if="task.student" v-model="point" type="number" label="점수" min="-1" max="5"/>
          <div  v-if="!task.homework?.check_flag">
            <q-btn color="primary" label="채점 완료" @click="checkStudent" />
          </div>
        </div>
          <hr>
      </article>
    </q-card-section>
  </q-card-section>
</template>

<script>
import {useStore} from 'vuex'
import {computed, ref} from 'vue'
import {useRoute} from 'vue-router'
import drf from '@/api/drf.js'
import dayjs from 'dayjs'
import axios from 'axios'
import TaskTargetStudent from '@/components/TaskTargetStudent.vue'
export default {
  name: 'TaskDetailContent',
  components: {
    TaskTargetStudent,
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
    let checkState = computed(() => {
      if (isLecture.value) {
        return props.task.homework['check_flag']? '채점 완료':'채점 미완료'
      } else {
        return props.task['agreement']? '채점 완료':'채점 미완료'
      }
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
        .then(((res) => {
          console.log(res.data)
        }))
        .catch((err) => {
          console.log(err)
        })
    }
    const checkStudent = () => {
      axios({
        url: drf.task.check(),
        method: 'post',
        headers: store.getters.authHeader,
        data,
      })
      .then((() => {
        axios({
          url: drf.task.checkDone(),
          method: 'post',
          headers: store.getters.authHeader,
          data: {
            username: props.task.student.username,
            point: point.value * 1,
          },
        })
          .then(((res) => {
            console.log(res.data)
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
      checkState,
      checkComplete,
      checkStudent,
      point,
      files,
      isLecture
    }
  },
}
</script>