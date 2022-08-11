<template>
  <main>
    <h1>{{userType}} 과제 {{type}} 페이지 {{taskPk}}</h1>
    <section class="q-pa-md" style="max-width: 400px">
      <q-form
        @reset="onReset"
        class="q-gutter-md"
      >
        <q-input
          outlined
          v-model="task.title"
          label="제목"
          required
        />

        <q-input
          outlined
          type="textarea"
          label="내용"
          v-model="task.content"
        />

        <!-- 교사에게만 보임 -->
        <div v-if="isTeacher">
          <q-select
            outlined
            v-model="task.subject"
            label="과목"
            :options="subjectOptions"
          />
          <q-input
            outlined
            type="number"
            :min="1"
            :max="3"
            label="학년"
            v-model="task.grade"
            lazy-rules
            :rules="[
            val => val === '' || val === null || val > 0 && val < 4 || '값이 올바르지 않습니다'
          ]"
          />
          <q-input
            outlined
            type="number"
            label="반"
            :min="1"
            :max="20"
            v-model="task.class_field"
            lazy-rules
            :rules="[
            val => val === '' || val === null || val > 0 && val < 21 || '값이 올바르지 않습니다'
            ]"
          />
        </div>
        <q-input
          outlined
          stack-label
          type="date"
          label="제출기한"
          v-model="task.deadline"
        />
        <q-input
          label="첨부파일"
          stack-label
          outlined
          @update:model-value="val => { task.files = val }"
          multiple
          type="file"
        />
        <div>
          <q-btn label="초기화" type="reset" color="primary" flat class="q-ml-sm" />
          <q-btn :label="type" color="primary" @click="onSubmit(false)" />
          <q-btn v-if="!isTeacher" label="제출" color="primary" @click="onSubmit(true)"/>
          <router-link class="button" :to="{name:'TaskListView', params: {userType,}}">
            <q-btn label="목록" color="primary"/>
          </router-link>
        </div>
      </q-form>
    </section>
  </main>
</template>

<script>
import { reactive, computed, onBeforeMount} from 'vue'
import { useRoute } from 'vue-router'
import {useStore} from 'vuex'
export default {
  name: 'TaskFormView',
  setup () {
    const route = useRoute()
    const store = useStore()
    let {userType, taskPk} = route.params
    onBeforeMount(() => {
      if (taskPk) {
        store.dispatch('initTask')
        store.dispatch('taskDetail', {pk: taskPk, teacher_flag: userType === 'teacher'? 1:0})
    }
    })
    const subjectOptions = store.getters.getSubject
    let isTeacher = computed(() => userType === 'teacher')
    let type = computed(() => taskPk? '수정':'등록')
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
      teacher_flag: isTeacher.value? 1:0,
      subject: taskPk? computedTask.subject: '',
      title: taskPk? computedTask.title: '',
      content: taskPk? computedTask.content : '',
      grade: taskPk? computedTask.grade : '',
      class_field: taskPk? computedTask.class_field : '',
      files: taskPk? computedTask.files : '',
      deadline: taskPk? computedTask.deadline : '',
    })
    const onSubmit = (arg) => {
      let form = new FormData()
      for (let key in task) {
        if (key === 'files' && task[key]) {
          for (let i=0; i < task.files.length; i++) {
            form.append(key, task[key][i])
          }
        } else {
          form.append(key, task[key])
        }
      }
      if (arg) {
        form.append('submit_pk', storeTask.value['my_submit'][0].id)
        store.dispatch('submitTask', form)
      } else if (taskPk) {
        form.append('pk', taskPk)
        store.dispatch('taskUpdate', form)
        console.log('update')
      } else {
        store.dispatch('createTask', form)
        console.log('create')
      }
    }
    const onReset = (event) => {
      event.preventDefault()
      if (taskPk) {
        for (let key in task) {
          if (key === 'teacher') {
              task[key] = store.getters.currentUser.username
            } else if (key === 'subject') {
              task[key] = store.getters.currentUser.subject
            } else {
            task[key] = storeTask.value[key]
          }
        }
      } else {
        for (let key in task) {
          task[key] = ''
        }
      }
    }
    return {
      task,
      storeTask,
      userType,
      taskPk,
      type,
      isTeacher,
      onSubmit,
      onReset,
      subjectOptions,
      computedTask
    }
  }
}
</script>