<template>
  <q-card>
    <q-tabs
      v-model="tab"
      dense
      class="text-grey"
      active-color="primary"
      indicator-color="primary"
      align="justify"
      narrow-indicator
    >
      <q-tab name="todoTask" label="제출 전 과제 목록" />
      <q-tab name="myTask" label="자율학습 과제 목록" />
      <q-tab name="doneTask" label="제출한 과제 목록" />
    </q-tabs>

    <q-separator />

    <q-tab-panels v-model="tab">
      <q-tab-panel name="todoTask">
        <q-list bordered class="rounded-borders" v-for="sample in samples" :key="sample.pk">
          <task-item :sample = sample />
        </q-list>
        <the-pagination />
      </q-tab-panel>

      <q-tab-panel name="myTask">
        <q-list bordered class="rounded-borders" v-for="sample in samples" :key="sample.pk">
          <task-item :sample = sample />
        </q-list>
      </q-tab-panel>

      <q-tab-panel name="doneTask">
        <q-list bordered class="rounded-borders" v-for="sample in samples" :key="sample.title">
          <task-item :sample = sample />
        </q-list>
      </q-tab-panel>
    </q-tab-panels>
  </q-card>
</template>

<script>
import {ref} from 'vue'
import TaskItem from '@/components/TaskItem.vue'
import ThePagination from '@/components/ThePagination.vue'
export default {
  name: 'StudentTaskTab',
  components: {
    TaskItem,
    ThePagination,
  },
  setup() {
    let tab = ref('todoTask')
    let samples =[
      {pk: 1, title : '과제 제목', name: '출제자', content: '내용'},
      {pk: 2, title : '과제 제목2', name: '출제자2', content: '내용2'}]
    return {
      tab,
      samples
    }
  }
}
</script>