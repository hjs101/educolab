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
      <q-tab class="text-size" name="notDone" label="제출 가능한 과제" />
      <q-tab name="studentTask" label="미제출 자율 학습" />
      <q-tab name="studentCheckedTask" label="제출한 자율 학습" />
      <q-tab name="done" label="기한이 지난 과제 목록" />
    </q-tabs>

    <q-separator />
    <q-tab-panels v-model="tab">
      <q-tab-panel name="notDone">
        <div
          bordered
          class="rounded-borders">
          <task-list-table
            :list="list.notDone"
            :page="page.notDone"
            :teacher="1"
            :submit="false"
          />
        </div>
        <the-pagination
          v-if="number.notDone"
          :limit="number.notDone"
          target="notDone"
          @change-page="changePage" />
      </q-tab-panel>

      <q-tab-panel name="studentTask">
        <div
          bordered
          class="rounded-borders">
          <task-list-table
            :list="list.studentTask"
            :page="page.studentTask"
            :teacher="0"
            :submit="false"
          />
        </div>
        <the-pagination
          v-if="number.studentTask"
          :limit="number.studentTask"
          target="notCheck"
          @change-page="changePage" />
      </q-tab-panel>

      <q-tab-panel name="studentCheckedTask">
        <div
          bordered
          class="rounded-borders">
          <task-list-table
            :list="list.studentCheckedTask"
            :page="page.studentCheckedTask"
            :teacher="0"
            :submit="true"
            :over="true"
          />
        </div>
        <the-pagination
          v-if="number.studentCheckedTask"
          :limit="number.studentCheckedTask"
          target="studentCheckedTask"
          @change-page="changePage" />
      </q-tab-panel>

      <q-tab-panel name="done">
        <div
          bordered
          class="rounded-borders">
          <task-list-table
            :list="list.done"
            :page="page.done"
            :teacher="1"
            :submit="true"
            :over="true"
          />
        </div>
        <the-pagination
          v-if="number.done"
          :limit="number.done"
          target="done"
          @change-page="changePage" />
      </q-tab-panel>
    </q-tab-panels>
  </q-card>
</template>

<script>
import {ref, reactive, computed} from 'vue'
import {useStore} from 'vuex'
import ThePagination from '@/components/ThePagination.vue'
import TaskListTable from '@/components/TaskListTable.vue'
export default {
  name: 'StudentTaskTab',
  components: {
    ThePagination,
    TaskListTable,
  },
  setup() {
    let tab = ref('notDone')
    const store = useStore()
    const list = reactive({
      notDone: computed(() => store.getters.getStudentNotDone),
      studentTask: computed(() => store.getters.getStudentSelfTask),
      studentCheckedTask: computed(() => store.getters.getCheckedSelfTask),
      done: computed(() => store.getters.getStudentDone),
    })
    const page = reactive({
      notDone: 1,
      studentTask: 1,
      studentCheckedTask: 1,
      done: 1,
    })
    const number = reactive({
      notDone: computed(() => store.getters.cntStudentNotDone),
      studentCheckedTask: computed(() => store.getters.cntCheckedSelfTask),
      studentTask: computed(() => store.getters.cntStudentSelfTask),
      done: computed(() => store.getters.cntStudentDone),
    })
    const changePage = (value, target) => {
      page[target] = value
    }
    return {
      tab,
      list,
      page,
      number,
      changePage
    }
  }
}
</script>

<style scoped>
  .text-size{font-size: 1rem;}
  .searchWrap{border-radius:5px; text-align:center; padding:20px 0; margin-bottom:10px;}
  .tbList th{border-top:1px solid #888;}
	.tbList th, .tbList td{border-bottom:1px solid #eee; padding:5px 0;}
	.tbList td.txt_left{text-align:left;}
  .btn{margin-bottom:40px;}
  .notice-small {
    display: none;
  }

  @media screen and (max-width: 950px) {
    .notice-full {
      display: none;
    }
    .notice-small {
      display: block;
    }
  }
</style>