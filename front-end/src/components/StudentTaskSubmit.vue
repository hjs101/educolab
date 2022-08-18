<template>
  <q-form
    @submit="onSubmit"
    @reset="onReset"
    class="q-my-lg"
    >
    <span class="title-size">과제 제출</span>
    <br>
    <br>
    <q-input
      v-model="student.content"
      outlined
      label="내용"
      type="textarea"
    />
    <q-input
      outlined
      class="col-7 q-my-md"
      @update:model-value="val => { student.file = val[0] }"
      type="file"
    />
    <div class="buttonGroup">
      <q-btn
        color="primary"
        type="reset"
        flat
        label="초기화"
        class="text-size q-mx-lg q-py-sm"
      />
      <q-btn
        color="primary"
        type="submit"
        label="과제 제출"
        class="text-size q-mx-lg q-py-sm"
      />
    </div>
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
      content: change.value? change.value[0].content: null,
      file: change.value? change.value[0].atch_file_name: null
    })
    const onSubmit = () => {
      let form = new FormData()
      form.append('submit_pk', change.value[0].id)
      form.append('teacher_flag', 1)
      form.append('content', student.content)
      form.append('files', student.file)
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