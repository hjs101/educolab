<template>
  <q-form
    @submit="onSubmit"
    @reset="onReset">
    <q-input
      v-model="student.text"
      outlined
      label="내용"
      type="textarea"
    />
    <q-input
      @update:model-value="val => { student.files = val }"
      multiple
      type="file"
    />
    <!-- 학생에게만 보임 (생성, 수정 모두) -->
    <q-btn color="primary" type="reset" flat label="초기화"/>
    <q-btn color="primary" type="submit" label="과제 제출"/>
  </q-form>
</template>

<script>
import {reactive} from 'vue'
import {useStore} from 'vuex'
export default {
  name: 'StudentTaskSubmit',
  setup() {
    const store = useStore()
    const student = reactive({
      text: null,
      files: null,
    })
    const onSubmit = (event) => {
      event.preventDefault()
      let form = new FormData()
      form.append('text', student.text)
      if (student['files'] !== null) {
        for (let i=0; i < student.files.length; i++) {
          form.append('files', student.files[i])
        }
      }
      store.dispatch('submitTask', form)
    }
    const onReset = (event) => {
      event.preventDefault()
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