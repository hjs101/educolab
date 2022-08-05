<template>
  <div>
    <h1>과제 상세 페이지 {{task.pk}}</h1>
    {{user.current}}
    <section>
      <header>{{task.title}} | {{task.createdAt}} | {{task.name}}</header>
      <article>
        {{task.deadline}}
        <br>
        {{task.content}}
      </article>
      <!-- 교사용 -->
      <article v-if="user.isTeacher">
        <q-list bordered class="rounded-borders" v-for="sample in samples" :key="sample.name">
          <task-target-student :sample="sample" />
        </q-list>
      </article>
      <!-- 학생용 -->
      <article v-if="!user.isTeacher">
        <q-input
          v-model="task.text"
          outlined
          label="내용"
          type="textarea"
        />
        <q-input
          @update:model-value="val => { files = val }"
          multiple
          type="file"
        />
        <!-- 학생에게만 보임 (생성, 수정 모두) -->
        <q-btn color="primary" label="과제 제출"/>
      </article>
      <div>
      <!-- 자신이 만든 페이지에서만 보임 -->
        <router-link class="button" :to="{name: 'TaskUpdateView', params: {
          userType: user.type, taskPk,
        }}">
          <q-btn color="primary" label="수정"/>
        </router-link>
        <q-btn color="primary" label="삭제" @click="confirm = true"/>
        <!-- 여기에 삭제 확인 메시지 -->
      </div>
      <router-link :to="user.path" class="button">
        <q-btn color="primary" label="목록"/>
      </router-link>
    </section>
  <router-view />
  </div>
</template>

<script>
import {computed, reactive, ref} from 'vue'
import {useStore} from 'vuex'
import {useRoute} from 'vue-router'
import TaskTargetStudent from '@/components/TaskTargetStudent.vue'
export default {
  name: 'TaskDetailView',
  components: {
    TaskTargetStudent
  },
  setup() {
    const route = useRoute()
    const store = useStore()
    let {taskPk} = ref(route.params)
    const user = reactive({
      type: route.params.userType,
      current: store.getters.currentUser.userflag,
      isTeacher: computed(() => user.type === 'teacher'),
      path: computed(() => user.isTeacher? '/teacher/task':'/student/task')
      })
    let files = ref(null)
    const samples =
      [{name : '학생 이름', submitAt:'제출 시간', content: '내용'},
      {name : '학생 이름2', submitAt:'제출 시간2', content: '내용2'},]
    let confirm = ref(false)
    return {
      taskPk,
      user,
      files,
      samples,
      confirm,
    }
  }
}
</script>