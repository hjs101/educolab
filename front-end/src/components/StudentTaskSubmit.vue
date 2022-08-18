<template>
  <q-form
    @submit="onSubmit"
    @reset="onReset"
    class="row justify-center align-center">
    <span class="q-mb-lg title-size">과제 제출</span>
    <span class="col-12"></span>
    <q-input
      class="col-7"
      v-model="student.content"
      outlined
      label="내용"
      type="textarea"
    />
    <q-input
      class="col-7 q-my-md"
      @update:model-value="val => { student.files = val }"
      multiple
      type="file"
    />
    <span class="col-12"></span>
    <q-btn color="primary" type="reset" flat label="초기화"/>
    <q-btn color="primary" type="submit" label="과제 제출"/>
  </q-form>
</template>

<script>
import {computed, reactive} from 'vue'
import {useStore} from 'vuex'
export default {
  name: 'StudentTaskSubmit',
  setup() {
    const store = useStore()
    const storeTask = computed(() => store.getters.getTask)
    const change = computed(() => storeTask.value.student_submit)
    const student = reactive({
      content: change.value? change.value[0].content: '',
      files: change.value? change.value[0].atch_file_name: ''
    })
    const onSubmit = (event) => {
      event.preventDefault()
      let form = new FormData()
      form.append('submit_pk', change.value[0].id)
      form.append('teacher_flag', 1)
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

<style scoped>
  .text-size {
    font-size: 1rem;
  }
  .title-size {
    font-size : 3vmin;
  }
</style>