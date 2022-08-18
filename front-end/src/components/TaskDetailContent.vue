<template>
  <div class="row justify-center q-my-xl">
    <div class="notice_form">
        <hr>
        <div class="row justify-between items-center">
          <div class="row start items-center">
            <p class="title-size">{{ task.homework?.title || task.title }}</p>
          </div>
          <p class="item-size text-right q-px-md"> {{date}}</p>
        </div>
        <span class="item-size text-start q-pl-sm text-grey-13">
          <span v-if="isLecture.value"> {{task.homework['check_flag']? '채점 완료':'채점 미완료'}}</span>
          <span v-else> {{task.agreement? '채점 완료':'채점 미완료'}}</span>
        </span>
        <span class="item-size text-end q-pl-sm text-grey-13">
          ( ~{{task.homework?.deadline || task.deadline}}) 
        </span>
        <hr>

        <div>
          <q-card class="bord">
            <q-card-section>
              <p class="content-size bg-white" style="min-height:500px">{{task.homework?.content || task.content}}</p>
            </q-card-section>
          </q-card>
        </div>
      <hr>

      <div class="q-py-sm q-pl-sm">
        <p class="text-size text-grey-13 q-pb-sm">첨부파일 ({{ files? 1:0 }}) </p>
          <q-btn @click="openFile(url+files['atch_file'])" color="grey-12" class="text-black">
            <q-icon name="mdi-paperclip"/>
            {{ files.atch_file_name }}
            </q-btn>
        </div>
      </div>
      <hr>
      <!-- 교사용 -->
      <article v-if="isTeacher">
        <!-- 자신이 작성한 상세 페이지에서 -->
        <div v-if="isLecture" class="q-my-md row">
          <span class="col-3 align-baseline text-h6"> 학생 목록 </span>
          <q-btn
            color="primary"
            label="채점 완료"
            @click="checkComplete"
            v-if="check.possible"
            class="offset-7 col-2 q-my-md"
            />
          <q-list
            bordered
            class="rounded-borders col-12"
            v-for="item in task.student_submit"
            :key="item.id">
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
        <div v-else-if="!task.agreement" class="row justify-center items-baseline">
          <q-input
            v-if="task.student"
            v-model="point"
            type="number"
            label="점수"
            min="-1"
            max="5"
            class="q-ml-md col-9" 
          />
          <q-btn
            v-if="!task.homework?.check_flag"
            color="primary"
            label="채점 완료"
            @click="checkStudent"
            class="q-ml-md col-2"
          />
          <hr>
          <message-pop-up
            v-if="check.confirmStudent"
            message="채점이 완료되었습니다"
            path="/teacher/task"
            @reverse="check.student = false"
          />
        </div>
      </article>
  </div>
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
    const openFile = (url) => {
      window.open(url)
    }
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
      openFile,
      isLecture,
    }
  },
}
</script>

<style scoped>
  .title-size {
    font-size : 3vmin;
  }
  .content-size {
    font-size : 2.5vmin;
  }
  .item-size {
    font-size: 2vmin;
  }
  .my-card {
    width: 70%
  }
  p {
    margin: 0;
  }
  h3 {
    margin: 0;
  }
  .notice_form {
    width: 60%;
    /* margin : 0; */
    /* font-family: "jooa"; */
  }
  .color1 {
    color: #FF9966;
  }
  .text-size {
    font-size: 1rem;
  }
  .bord-bt {
    border-bottom: 1px solid #99DFF9;
  }
  .btn-mag {
    margin-top: 100px;
  }
  .bord {
    border: 1px solid ;
  }
</style>