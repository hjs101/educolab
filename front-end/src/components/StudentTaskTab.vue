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
      <q-tab name="notDone" label="제출 가능한 과제" />
      <q-tab name="studentTask" label="미제출 자율 학습" />
      <q-tab name="studentCheckedTask" label="제출한 자율 학습" />
      <q-tab name="done" label="기한이 지난 과제 목록" />
    </q-tabs>

    <q-separator />

    <q-tab-panels v-model="tab">
      <q-tab-panel name="notDone">
        <div v-for="num in number.notDone" :key="num">
          <div v-if="num === page.notDone">
            <q-list bordered class="rounded-borders" v-for="item in list.notDone.slice((num-1)*10, num*10)" :key="item.pk">
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

      <q-tab-panel name="studentTask">
        <div v-for="num in number.studentTask" :key="num">
          <div v-if="num === page.studentTask">
            <q-list bordered class="rounded-borders" v-for="item in list.studentTask.slice((num-1)*10, num*10)" :key="item.pk">
              <task-item :item = item :teacher="0" />
            </q-list>
          </div>
        </div>
        <the-pagination
          v-if="number.studentTask"
          :limit="number.studentTask"
          target="notCheck"
          @change-page="changePage" />
      </q-tab-panel>

      <q-tab-panel name="studentCheckedTask">
        <div v-for="num in number.studentCheckedTask" :key="num">
          <div v-if="num === page.studentCheckedTask">
            <q-list bordered class="rounded-borders" v-for="item in list.studentTask.slice((num-1)*10, num*10)" :key="item.pk">
              <task-item :item = item :teacher="0" />
            </q-list>
          </div>
        </div>
        <the-pagination
          v-if="number.studentCheckedTask"
          :limit="number.studentCheckedTask"
          target="studentCheckedTask"
          @change-page="changePage" />
      </q-tab-panel>

      <q-tab-panel name="done">
        <div v-for="num in number.done" :key="num">
          <div v-if="num === page.done">
            <q-list bordered class="rounded-borders" v-for="item in list.done.slice((num-1)*10, num*10)" :key="item.pk">
              <task-item :item = item :teacher="1" />
            </q-list>
          </div>
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
import TaskItem from '@/components/TaskItem.vue'
import ThePagination from '@/components/ThePagination.vue'
export default {
  name: 'StudentTaskTab',
  components: {
    TaskItem,
    ThePagination,
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