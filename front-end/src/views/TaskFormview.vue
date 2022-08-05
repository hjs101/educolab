<template>
  <main>
    <h1>{{userType}} 과제 작성, 수정 페이지 {{taskPk}}</h1>
    <section class="q-pa-md" style="max-width: 400px">
      <q-form
        @submit="onSubmit"
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
            v-model="task.targetGrade"
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
            v-model="task.targetClass"
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
          <q-btn label="등록" type="submit" color="primary"/>
          <q-btn label="초기화" type="reset" color="primary" flat class="q-ml-sm" />
        </div>
      </q-form>
    </section>
  </main>
</template>

<script>
import { ref, reactive, computed } from 'vue'
import { useRoute } from 'vue-router'
import {useStore} from 'vuex'
export default {
  name: 'TaskFormView',
  setup () {
    const route = useRoute()
    const store = useStore()
    const subjectOptions = store.getters.getSubject
    let userType = route.params.userType
    let isTeacher = computed(() => userType === 'teacher')
    let taskPk = route.params.taskPk
    const task = reactive({
      teacher: store.getters.currentUser.username,
      subject: store.getters.currentUser.subject,
      title: null,
      content: null,
      grade: null,
      class_field: null,
      files: null,
      deadline: null,
    })
    const accept = ref(false)
    const onSubmit = (event) => {
      event.preventDefault()
      store.dispatch('createTask', task)
    }
    const onReset = (event) => {
      event.preventDefault()
      for (let key in task) {
        task[key] = null
      }
    }

    return {
      task,
      accept,
      userType,
      taskPk,
      isTeacher,
      onSubmit,
      onReset,
      subjectOptions
    }
  }
}
</script>

import {reactive} from 'vue'
setup() {
  credential
}