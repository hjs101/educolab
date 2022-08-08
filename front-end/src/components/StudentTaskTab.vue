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
      <q-tab name="todoTask" label="제출 가능한 과제" />
      <q-tab name="myCheckedTask" label="제출한 자율 학습" />
      <q-tab name="myTask" label="미제출 자율 학습" />
      <q-tab name="doneTask" label="제출한 과제 목록" />
    </q-tabs>

    <q-separator />

    <q-tab-panels v-model="tab">
      <q-tab-panel name="todoTask">
        <q-list bordered class="rounded-borders" v-for="item in list.notDone" :key="item.pk">
          <task-item :item = item />
        </q-list>
        <the-pagination
          v-if="number.notDone"
          :limit="number.notDone"
          @change-page="changePage" />
      </q-tab-panel>

      <q-tab-panel name="myCheckedTask">
        <q-list bordered class="rounded-borders" v-for="item in list.studentTask" :key="item.pk">
          <task-item :item = item />
        </q-list>
        <the-pagination
          v-if="number.studentTask"
          :limit="number.studentTask"
          @change-page="changePage" />
      </q-tab-panel>

      <q-tab-panel name="myTask">
        <q-list bordered class="rounded-borders" v-for="item in list.studentTask" :key="item.pk">
          <task-item :item = item />
        </q-list>
        <the-pagination
          v-if="number.studentTask"
          :limit="number.studentTask"
          @change-page="changePage" />
      </q-tab-panel>

      <q-tab-panel name="doneTask">
        <q-list bordered class="rounded-borders" v-for="item in list.done" :key="item.pk">
          <task-item :item = item />
        </q-list>
        <the-pagination
          v-if="number.done"
          :limit="number.done"
          @change-page="changePage" />
      </q-tab-panel>
    </q-tab-panels>
  </q-card>
</template>

<script>
import {ref, reactive, computed} from 'vue'
import {useStore} from 'vuex'
import TaskItem from '@/components/TaskItem.vue'
import ThePagination from '@/components/ThePagination.vue'
export default {
  name: 'StudentTaskTab',
  components: {
    TaskItem,
    ThePagination,
  },
  setup() {
    const store = useStore()
    let tab = ref('todoTask')
    const list = reactive({
      notDone: computed(() => store.getters.getStudentNotDone),
      studentTask: computed(() => store.getters.getStudentSelfTask),
      done: computed(() => store.getters.getStudentDone),
    })
    const number = reactive({
      notDone: computed(() => store.getters.cntStudentNotDone),
      studentCheckedTask: computed(() => store.getters.cntStudentSelfTask),
      studentTask: computed(() => store.getters.cntStudentSelfTask),
      done: computed(() => store.getters.cntStudentDone),
    })
    return {
      tab,
      list,
      number
    }
  }
}
</script>