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
      <q-tab name="toScoreTask" label="채점 가능한 과제 목록" />
      <q-tab name="studentTask" label="학생이 신청한 과제 목록" />
      <q-tab name="toSubmitTask" label="제출 중인 과제 목록" />
      <q-tab name="doneTask" label="채점한 과제 목록" />
    </q-tabs>

    <q-separator />

    <q-tab-panels v-model="tab">
      <q-tab-panel name="toScoreTask">
        <q-list bordered class="rounded-borders" v-for="item in list.notCheck" :key="item.pk">
          <task-item :item = item :teacher="1"/>
        </q-list>
        <the-pagination v-if="number.notCheck" :limit="number.notCheck" />
      </q-tab-panel>

      <q-tab-panel name="studentTask">
        <q-list bordered class="rounded-borders" v-for="item in list.studentTask" :key="item.pk">
          <task-item :item = item :teacher="0"/>
        </q-list>
        <the-pagination v-if="number.studentTask" :limit="number.studentTask" />
      </q-tab-panel>

      <q-tab-panel name="toSubmitTask">
        <q-list bordered class="rounded-borders" v-for="item in list.notDone" :key="item.pk">
          <task-item :item = item :teacher="1" />
        </q-list>
        <the-pagination
          v-if="number.notDone"
          :limit="number.notDone"
          @change-page="changePage" />
      </q-tab-panel>

      <q-tab-panel name="doneTask">
        <q-list bordered class="rounded-borders" v-for="item in list.done" :key="item.pk">
          <task-item :item = item :teacher="1" />
        </q-list>
        <the-pagination v-if="number.done" :limit="number.done" />
      </q-tab-panel>
    </q-tab-panels>
  </q-card>
</template>

<script>
import {computed, reactive, ref} from 'vue'
import {useStore} from 'vuex'
import TaskItem from '@/components/TaskItem.vue'
import ThePagination from '@/components/ThePagination.vue'
export default {
  name: 'TeacherTaskTab',
  components: {
    TaskItem,
    ThePagination,
  },
  setup() {
    let tab = ref('toScoreTask')
    const store = useStore()
    const list = reactive({
      notCheck: computed(() => store.getters.getTeacherNotcheck),
      studentTask: computed(() => store.getters.getTeacherStudentTask),
      notDone: computed(() => store.getters.getTeacherNotDone),
      done: computed(() => store.getters.getTeacherDone),
    })
    const number = reactive({
      notCheck: computed(() => store.getters.cntTeacherNotcheck),
      studentTask: computed(() => store.getters.cntTeacherStudentTask),
      notDone: computed(() => store.getters.cntTeacherNotDone),
      done: computed(() => store.getters.cntTeacherDone),
    })
    let page = ref('1')
    const changePage = (number) => {
      page.value = number
    }
    return {
      tab,
      list,
      number,
      changePage
    }
  }
}
</script>