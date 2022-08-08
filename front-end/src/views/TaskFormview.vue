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
        <q-select
          outlined
          v-model="task.subject"
          label="과목"
          :options="subjectOptions"
        />

        <!-- 교사에게만 보임 -->
        <div v-if="isTeacher">
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
          <q-input
            outlined
            stack-label
            type="date"
            label="제출기한"
            v-model="task.deadline"
          />
        </div>
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
import { ref, reactive, computed} from 'vue'
import { useRoute } from 'vue-router'
import {useStore} from 'vuex'
import {isEmpty} from 'lodash'
export default {
  name: 'TaskFormView',
  created() {
    const store = useStore()
    const route = useRoute()
    let {taskPk} = route.params
    if (taskPk && isEmpty(store.getters.getTask)) {
        store.dispatch('taskDetail', taskPk)
    }
  },
  setup () {
    const route = useRoute()
    const store = useStore()
    const subjectOptions = store.getters.getSubject
    let {userType, taskPk} = route.params
    let isTeacher = computed(() => userType === 'teacher')
    let type = computed(() => taskPk? '수정':'등록')
    const storeTask = ref(computed(() => store.getters.getTask))
    const computedTask = reactive({
      teacher: computed(() => store.getters.currentUser.username),
      subject: computed(() => store.getters.currentUser.subject),
      title: computed(() => taskPk? storeTask.value.title : null),
      content: computed(() => taskPk? storeTask.value.content : null),
      grade: computed(() => taskPk? storeTask.value.grade : null),
      class_field: computed(() => taskPk? storeTask.value.class_field : null),
      files: computed(() => taskPk? storeTask.value.files : null),
      deadline: computed(() => taskPk? storeTask.value.deadline : null),
    })
    const task = reactive({
      teacher: computedTask.teacher,
      subject: computedTask.subject,
      title: computedTask.title,
      content: computedTask.content,
      grade: computedTask.grade,
      class_field: computedTask.class_field,
      files: computedTask.files,
      deadline: computedTask.deadline,
    })
    const accept = ref(false)
    const onSubmit = (arg) => {
      let form = new FormData()
      form.append('pk', taskPk)
      for (let key in task) {
        if (key === 'files' && task[key]) {
          for (let i=0; i < task.files.length; i++) {
            console.log(task[key][i])
            form.append(key, task[key][i])
          }
        } else {
          form.append(key, task[key])
        }
      }
      if (arg) {
        store.dispatch('submitTask', form)
      } else if (taskPk) {
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
          task[key] = null
        }
      }
    }
    return {
      task,
      accept,
      userType,
      taskPk,
      type,
      isTeacher,
      onSubmit,
      onReset,
      subjectOptions,
    }
  }
}
</script>