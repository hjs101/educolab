<template>
  <article>
    학생 제출 과제
    <br>
    내용 : {{content}}
    <br>
    첨부파일
    <div v-for="(file, idx) in files" :key="idx">
      <a :href="url+task.student_submit[0].atch_file[idx]"> {{file}}</a>
    </div>
  </article>
</template>

<script>
import {computed} from 'vue'
import {useRoute} from 'vue-router'
import {useStore} from 'vuex'
import drf from '@/api/drf.js'
export default {
  setup() {
    const store = useStore()
    const route = useRoute()
    const task = computed(() => store.getters.getTask)
    const content = computed(() => {
      if (route.params.taskType === 'lecture') {
        return task.value.student_submit?task.value.student_submit[0].content:''
      } else {
        return task.value.my_submit?task.value.my_submit[0].content:''
      }
    })
    const files = computed(() => {
      if (route.params.taskType === 'lecture') {
        return task.value.student_submit?task.value.student_submit[0].atch_file_name:''
      } else {
        return task.value.my_submit?task.value.my_submit[0].atch_file_name:''
      }
    })
    const url = drf.file.path()
    return {
      task,
      content,
      files,
      url
    }
  },
}
</script>