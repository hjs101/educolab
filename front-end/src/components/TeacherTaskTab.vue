<template>
  <q-card>
    <q-tabs
      v-model="tab"
      dense
      class="text-grey q-pt-sm"
      active-color="primary"
      indicator-color="primary"
      align="justify"
      narrow-indicator
    >
      <q-tab class="text-size" name="notCheck">채점 가능한 과제 목록</q-tab>
      <q-tab class="text-size" name="studentTask">학생이 신청한 과제 목록</q-tab>
      <q-tab class="text-size" name="notDone">제출 중인 과제 목록</q-tab>
      <q-tab class="text-size" name="done">채점한 과제 목록</q-tab>
    </q-tabs>

    <q-separator />

    <q-tab-panels v-model="tab">
      <q-tab-panel name="notCheck">
        <div
          bordered
          class="rounded-borders">
          <task-list-table
            :list="totalList.notCheck"
            :page="page.notCheck"
            :teacher="1"
            :submit="false"
          />
        </div>
        <the-pagination
          v-if="number.notCheck"
          :limit="number.notCheck"
          target="notCheck"
          @change-page="changePage"
        />
      </q-tab-panel>

      <q-tab-panel name="studentTask">
        <div
          bordered
          class="rounded-borders">
          <task-list-table
            :list="totalList.studentTask"
            :page="page.studentTask"
            :teacher="0"
            :submit="false"
          />
        </div>
        <the-pagination
          v-if="number.studentTask"
          :limit="number.studentTask"
          target="studentTask"
          @change-page="changePage"
        />
      </q-tab-panel>

      <q-tab-panel name="notDone">
        <div
          bordered
          class="rounded-borders">
          <task-list-table
            :list="totalList.notDone"
            :page="page.notDone"
            :teacher="1"
            :submit="true"
          />
        </div>
        <the-pagination
          v-if="number.notDone"
          :limit="number.notDone"
          target="notDone"
          @change-page="changePage" />
      </q-tab-panel>

      <q-tab-panel name="done">
        <div
          bordered
          class="rounded-borders">
          <task-list-table
            :list="totalList.done"
            :page="page.done"
            :teacher="1"
          />
        </div>
        <the-pagination
          v-if="number.done"
          :limit="number.done"
          target="done"
          @change-page="changePage"
        />
      </q-tab-panel>
    </q-tab-panels>
  </q-card>
</template>

<script>
import {computed, reactive, ref} from 'vue'
import {useStore} from 'vuex'
import TaskListTable from '@/components/TaskListTable.vue'
import ThePagination from '@/components/ThePagination.vue'
export default {
  name: 'TeacherTaskTab',
  components: {
    TaskListTable,
    ThePagination
  },
  emits: [
    'change-page',
  ],
  setup() {
    let tab = ref('notCheck')
    const store = useStore()
    const totalList = reactive({
      notCheck: computed(() => store.getters.getTeacherNotCheck),
      studentTask: computed(() => store.getters.getTeacherStudentTask),
      notDone: computed(() => store.getters.getTeacherNotDone),
      done: computed(() => store.getters.getTeacherDone),
    })
    const page = reactive({
      notCheck: 1,
      studentTask: 1,
      notDone: 1,
      done: 1,
    })
    const number = reactive({
      notCheck: computed(() => store.getters.cntTeacherNotCheck),
      studentTask: computed(() => store.getters.cntTeacherStudentTask),
      notDone: computed(() => store.getters.cntTeacherNotDone),
      done: computed(() => store.getters.cntTeacherDone),
    })
    const changePage = (value, target) => {
      page[target] = value
    }
    return {
      tab,
      totalList,
      page,
      number,
      changePage,
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