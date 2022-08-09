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
      <q-tab name="notCheck" label="채점 가능한 과제 목록" />
      <q-tab name="studentTask" label="학생이 신청한 과제 목록" />
      <q-tab name="notDone" label="제출 중인 과제 목록" />
      <q-tab name="done" label="채점한 과제 목록" />
    </q-tabs>

    <q-separator />

    <q-tab-panels v-model="tab">
      <q-tab-panel name="notCheck">
        <div v-for="num in number.notCheck" :key="num">
          <div v-if="num === page.notCheck">
            <q-list bordered class="rounded-borders" v-for="item in totalList.notCheck.slice((num-1)*10, num*10)" :key="item.pk">
              <task-item :item = item :teacher="1"/>
            </q-list>
          </div>
        </div>
        <the-pagination
          v-if="number.notCheck"
          :limit="number.notCheck"
          target="notCheck"
          @change-page="changePage"
        />
      </q-tab-panel>

      <q-tab-panel name="studentTask">
        <div v-for="num in number.studentTask" :key="num">
          <div v-if="num === page.studentTask">
            <q-list bordered class="rounded-borders" v-for="item in totalList.studentTask.slice((num-1)*10, num*10)" :key="item.pk">
              <task-item :item = item :teacher="0"/>
            </q-list>
          </div>
        </div>
        <the-pagination
          v-if="number.studentTask"
          :limit="number.studentTask"
          target="notCheck"
          @change-page="changePage"
        />
      </q-tab-panel>

      <q-tab-panel name="notDone">
        <div v-for="num in number.notDone" :key="num">
          <div v-if="num === page.notDone">
            <q-list bordered class="rounded-borders" v-for="item in totalList.notDone.slice((num-1)*10, num*10)" :key="item.pk">
              <task-item :item = item :teacher="1" />
            </q-list>
          </div>
        </div>
        <the-pagination
          v-if="number.notDone"
          :limit="number.notDone"
          target="notDone"
          @change-page="changePage" />
      </q-tab-panel>

      <q-tab-panel name="done">
        <div v-for="num in number.done" :key="num">
          <div v-if="num === page.done">
            <q-list bordered class="rounded-borders" v-for="item in totalList.done.slice((num-1)*10, num*10)" :key="item.pk">
              <task-item :item = item :teacher="1" />
            </q-list>
          </div>
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
import TaskItem from '@/components/TaskItem.vue'
import ThePagination from '@/components/ThePagination.vue'
export default {
  name: 'TeacherTaskTab',
  components: {
    TaskItem,
    ThePagination,
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
      changePage
    }
  }
}
</script>