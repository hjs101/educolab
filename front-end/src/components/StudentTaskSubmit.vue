<template>
  <q-form
    @submit="onSubmit"
    @reset="onReset"
    class="q-my-lg">
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
      @update:model-value="val => { student.files = val }"
      mutiple
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
      <message-pop-up
        v-if="submit.confirm"
        message="제출되었습니다"
        path="/student/task"
        @reverse="submit.prompt = false"
      />
    </div>
  </q-form>
</template>

<script>
import {computed, reactive} from 'vue'
import {useStore} from 'vuex'
import MessagePopUp from './MessagePopUp.vue'
import {isEmpty} from 'lodash'
export default {
    name: 'StudentTaskSubmit',
    props: {
      MessagePopUp,
    },
    setup() {
    const store = useStore()
    const storeTask = computed(() => store.getters.getTask)
    const change = computed(() => storeTask.value.student_submit)
    const student = reactive({
      content: !isEmpty(change.value)? change.value[0].content: '',
      files: !isEmpty(change.value)? change.value[0].atch_file_name: ''
    })
    const onSubmit = () => {
      let form = new FormData()
      form.append('submit_pk', change.value[0].id)
      form.append('teacher_flag', 1)
      form.append('content', student.content)
      for (let i=0; i<student.files.length; i++) {
        form.append('files', student.files[i])
      }
      store.dispatch('submitTask', form)
    }
    const submit = reactive({
      prompt: false,
      confirm: computed(() => submit.prompt),
    })
    const onReset = () => {
      for (let key in student) {
        student[key] = null
      }
    }
    return {
      student,
      onSubmit,
      onReset,
      submit
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