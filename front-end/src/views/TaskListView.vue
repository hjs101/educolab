<template>
  <main class="baseStyle">
    <h4 class="text-center">과제</h4>
    <hr>
    <section class="q-pa-md">
      <article class="row items-baseline justify-evenly">
        <q-input label="과제 제목검색" v-model="query" class="col-8" />
        <router-link class="button" :to="{name: 'SearchTaskView', params:{userType,}, query:{query,}}" >
          <q-btn color="primary" label="검색" class="col-3 text-size q-mx-lg q-py-sm" />
        </router-link>
      </article>
      <article>
        <router-link
          :to="{name:'TaskCreateView', params:{userType,}}"
          class="button d-flex">
          <q-btn color="primary" label="과제 생성" class="q-my-lg text-size q-mx-lg" />
        </router-link>
        <student-task-tab v-if="!isTeacher"/>
        <teacher-task-tab v-else />
      </article>
    </section>
  </main>
</template>

<script>
import {useRoute, useRouter} from 'vue-router'
import {useStore} from 'vuex'
import { computed, onBeforeMount, onMounted, ref } from 'vue'
import StudentTaskTab from '@/components/StudentTaskTab.vue'
import TeacherTaskTab from '@/components/TeacherTaskTab.vue'
export default {
  name: 'StudentTaskListView',
  components: {
    StudentTaskTab,
    TeacherTaskTab,
  },
  setup () {
    const route = useRoute()
    const router = useRouter()
    const store = useStore()
    const {userType} = route.params
    const isTeacher = computed(() => userType === 'teacher')
    let search = ref(false)
    let query = ref(null)
    onBeforeMount(() => {
      if (!this.isLoggedIn) {
        router.push('/educolab/login')
      } else {
        store.dispatch('taskList')
      }
    })
    onMounted(() => {
    })
    return {
      userType,
      isTeacher,
      search,
      query,
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
</style>