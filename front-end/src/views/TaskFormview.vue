<template>
  <main class="baseStyle">
    <h4>과제 {{type}}</h4>
    <q-form
      v-if="!taskPk || computedTask">
      <div class="row">
        <span class="q-py-md q-mr-lg text-size" style="width:70px; text-align:center">제목</span>
        <q-input class="text-size" outlined v-model="task.title" label="title" style="width: 700px;" />
      </div>
      <hr>
      <div class="row">
        <span class="q-py-md q-mr-lg text-size" style="width:70px; text-align:center">내용</span>
        <div style="width:700px;">
          <q-input
            rows="20"
            type="textarea"
            outlined
            class="text-size"
            v-model="task.content"
            label="content"
            required/>
        </div>
      </div>
      <hr>
      <!-- 교사에게만 보임 -->
      <div v-if="task.teacher_flag">
        <div class="row">
          <span class="q-py-md q-mr-lg text-size" style="width:70px; text-align:center">과목 </span>
          <q-select
            v-model="task.subject"
            :options="subjectOptions"
            class="text-size"
            style="width: 300px;"
            outlined />
        </div>
        <hr>
        <div class="row">
          <span class="q-py-md q-mr-lg text-size" style="width:70px; text-align:center">학년</span>
          <q-input
            outlined
            style="width: 300px;"
            type="number"
            :min="1"
            :max="3"
            v-model="task.grade"
          />
          <span class="q-py-md q-mr-lg text-size" style="width:70px; text-align:center">반</span>
          <q-input
            outlined
            style="width: 300px;"
            type="number"
            :min="1"
            :max="10"
            v-model="task.class_field"
          />
        </div>
        <hr>
      </div>
      <div class="row">
        <span class="q-py-md q-ml-sm q-mr-lg text-size" style="width: 70px; text-align:center">제출기한</span>
        <q-input
          outlined
          stack-label
          type="date"
          v-model="task.deadline"
        />
      </div>
      <hr>
      <div class="row items-center">
        <span class="q-py-md q-ml-sm q-mr-lg text-size" style="width: 70px; text-align:center">첨부파일</span>
        <q-input
          type="file"
          outlined
          label-stack
          @update:model-value="val => { task.files = val }"
          multiple
          v-model="files"
          style="width: 700px;" />
      </div>
      <hr>
      <div class="row justify-center q-mt-xl q-gutter-md">
        <q-btn :label="type" color="primary" @click="onSubmit(false)"  class="text-size q-px-xl q-py-md" />
        <q-btn v-if="!task.teacher_flag" label="제출" color="primary" @click="onSubmit(true)"  class="text-size q-px-xl q-py-md"/>
        <router-link class="button" :to="{name:'TaskListView', params: {userType,}}">
          <q-btn label="목록" color="primary"  class="text-size q-px-xl q-py-md" />
        </router-link>
      </div>
    </q-form>
    <message-pop-up
      v-if="confirm.state"
      :message="confirm.message"
      @reverse="confirm.prompt = false"
    />
  </main>
</template>

<script>
import { reactive, computed, onBeforeMount} from 'vue'
import { useRoute, useRouter } from 'vue-router'
import {useStore} from 'vuex'
import MessagePopUp from '../components/MessagePopUp.vue'
export default {
  components: { MessagePopUp },
  name: 'TaskFormView',
  setup () {
    const route = useRoute()
    const store = useStore()
    const router = useRouter()
    let {userType, taskPk} = route.params
    onBeforeMount(() => {
      if (!store.getters.isLoggedIn) {
      router.push('/educolab/login')
      } else if (taskPk) {
        store.dispatch('taskDetail', {pk: taskPk, teacher_flag: userType === 'teacher'? 1:0})
    }})
    const subjectOptions = store.getters.getSubject
    let type = computed(() => taskPk? '수정':'등록')
    const confirm = reactive({
      prompt: false,
      message: '',
      state: computed(() => confirm.prompt)
    })
    const storeTask = computed(() => store.getters.getTask)
    const computedTask = reactive({
      subject: computed(() => storeTask.value.homework?.subject),
      title: computed(() => storeTask.value.homework?.title || storeTask.value.title),
      content: computed(() => storeTask.value.homework?.content || storeTask.value.content),
      grade: computed(() => storeTask.value.homework?.grade),
      class_field: computed(() => storeTask.value.homework?.class_field),
      files: computed(() => storeTask.value.homework?.files || storeTask.value['student_file']),
      deadline: computed(() => storeTask.value.homework?.deadline || storeTask.value.deadline),
    })
    const task = reactive({
      teacher_flag: userType === 'teacher'?1:0,
      subject: taskPk? computedTask.subject: '',
      title: taskPk? computedTask.title: '',
      content: taskPk? computedTask.content : '',
      grade: taskPk? computedTask.grade : '',
      class_field: taskPk? computedTask.class_field : '',
      files: taskPk? computedTask.files : '',
      deadline: taskPk? computedTask.deadline : '',
    })
    const isValid = computed(() => {
      if (task.title && task.content && task.deadline ) {
        if (task.teacher_flag) {
          if (task.subject && task.grade && task.class_field) {
            return true
          } else {
            return false
          }
        } else {
          return true
        }
      } else {
        return false
      }
    })
    const onSubmit = (arg) => {
      let form = new FormData()
      for (let key in task) {
        if (key === 'files') {
          for (let i=0; i<task.files.length; i++) {
            form.append('files', task['files'][i])
          }
        } else {
          form.append(key, task[key])
        }
      }
      if (arg) {
        form.append('submit_pk', task['my_submit'][0].id)
        store.dispatch('submitTask', form)
      } else if (taskPk) {
        form.append('pk', taskPk)
        store.dispatch('taskUpdate', form)
      } else {
        if (isValid.value) {
          store.dispatch('createTask', form)
        } else {
          confirm.message = '필수 항목을 채워주세요'
          confirm.prompt = true
        }
      }
    }
    return {
      task,
      userType,
      taskPk,
      type,
      onSubmit,
      subjectOptions,
      confirm,
      computedTask,
    }
  }
}
</script>

<style scoped>
  p {
    margin: 0;
  }
  .text-size {
    font-size: 1rem;
  }
</style>
