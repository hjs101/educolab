<template>
  <q-form
    @submit="onSubmit"
    @reset="onReset">
    <span>과제 제출</span>
    <q-input
      v-model="student.content"
      outlined
      label="내용"
      type="textarea"
    />
    <q-input
      @update:model-value="val => { student.files = val }"
      multiple
      type="file"
    />
    <q-btn color="primary" type="reset" flat label="초기화"/>
    <q-btn color="primary" type="submit" label="과제 제출"/>
  </q-form>
</template>

<script>
import {reactive} from 'vue'
import {useStore} from 'vuex'
import {useRoute} from 'vue-router'
export default {
  name: 'StudentTaskSubmit',
  setup() {
    const store = useStore()
    const route = useRoute()
    const student = reactive({
      content: null,
      files: null,
    })
    const onSubmit = (event) => {
      event.preventDefault()
      let form = new FormData()
      const task = store.getters.getTask
      let pk = null
      let teacher = null
      if (route.params.taskType === 'lecture') {
        teacher = 1
      } else {
        pk = task['my_submit'][0].id
        teacher = 0
      }
      form.append('submit_pk', pk)
      form.append('teacher', teacher)
      form.append('content', student.content)
      if (student['files'] !== null) {
        for (let i=0; i < student.files.length; i++) {
          form.append('files', student.files[i])
        }
      }
      store.dispatch('submitTask', form)
    }
    const onReset = () => {
      for (let key in student) {
        student[key] = null
      }
    }
    return {
      student,
      onSubmit,
      onReset
    }
  },
}
</script>