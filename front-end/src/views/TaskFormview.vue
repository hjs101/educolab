<template>
<<<<<<< HEAD
  <main>
<<<<<<< HEAD
=======
  <main class="baseStyle">
<<<<<<< HEAD
>>>>>>> 0a91d41 (Feat : 비밀번호 확인, 회원정보 변경 기능 구현 완료, 약간의 스타일 적용)
    <h1>{{userType}} 과제 {{type}} 페이지 {{taskPk}}</h1>
    <section class="q-pa-md" style="max-width: 400px">
      <q-form
=======
    <h1>{{userType}} 과제 작성, 수정 페이지 {{taskPk}}</h1>
    <section class="q-pa-md" style="max-width: 400px">
      <q-form
        @submit="onSubmit"
>>>>>>> 0e01249 (Feat : 객관식 문항 /로 구분해 저장 기능 완료)
        @reset="onReset"
        class="q-gutter-md"
      >
        <q-input
          outlined
          v-model="task.title"
          label="제목"
          required
        />

        <q-input
          outlined
          type="textarea"
          label="내용"
          v-model="task.content"
        />
<<<<<<< HEAD

        <!-- 교사에게만 보임 -->
        <div v-if="isTeacher">
=======
    <h4>과제 {{type}}</h4>
    <q-form
      @reset="onReset">
      <div class="row">
        <span class="q-py-md q-mr-lg text-size" style="width:70px; text-align:center">제목</span>
        <q-input class="text-size" outlined v-model="task.title" label="title" style="width: 700px;" required/>
      </div>
      <hr>
      <div class="row">
        <span class="q-py-md q-mr-lg text-size" style="width:70px; text-align:center">내용</span>
        <div style="width:700px">
          <q-editor
            class="text-size"
            style="min-height:500px; max-height:100%;"
            v-model="task.content"
            label="content"
            :definitions="{
              bold: {label: 'Bold', icon: null, tip: 'My bold tooltip'}
            }"
            required/>
        </div>
      </div>
      <hr>
      <!-- 교사에게만 보임 -->
      <div v-if="isTeacher">
        <div class="row">
          <span class="q-py-md q-mr-lg text-size" style="width:70px; text-align:center">과목 </span>
>>>>>>> db26c2a (Style & Fix : 스타일 및 오류 수정)
          <q-select
            class="text-size"
            style="width: 300px;"
            outlined
<<<<<<< HEAD
            v-model="task.subject"
            label="과목"
            :options="subjectOptions"
          />
=======
        <q-select
          outlined
          v-model="task.subject"
          label="과목"
          :options="subjectOptions"
        />

        <!-- 교사에게만 보임 -->
        <div v-if="isTeacher">
>>>>>>> 0e01249 (Feat : 객관식 문항 /로 구분해 저장 기능 완료)
=======
            v-model="task.subject" label="과목" :options="subjectOptions" required/>
        </div>
        <hr>
        <div class="row">
          <span class="q-py-md q-mr-lg text-size" style="width:70px; text-align:center">학년</span>
>>>>>>> db26c2a (Style & Fix : 스타일 및 오류 수정)
          <q-input
            outlined
            style="width: 300px;"
            type="number"
            :min="1"
            :max="3"
<<<<<<< HEAD
            label="학년"
<<<<<<< HEAD
            v-model="task.grade"
=======
            v-model="task.targetGrade"
>>>>>>> 0e01249 (Feat : 객관식 문항 /로 구분해 저장 기능 완료)
            lazy-rules
            :rules="[
            val => val === '' || val === null || val > 0 && val < 4 || '값이 올바르지 않습니다'
          ]"
=======
            v-model="task.grade"
            required
>>>>>>> db26c2a (Style & Fix : 스타일 및 오류 수정)
          />
          <span class="q-py-md q-mr-lg text-size" style="width:70px; text-align:center">반</span>
          <q-input
            outlined
            style="width: 300px;"
            type="number"
            :min="1"
<<<<<<< HEAD
            :max="20"
<<<<<<< HEAD
            v-model="task.class_field"
=======
            v-model="task.targetClass"
>>>>>>> 0e01249 (Feat : 객관식 문항 /로 구분해 저장 기능 완료)
            lazy-rules
            :rules="[
            val => val === '' || val === null || val > 0 && val < 21 || '값이 올바르지 않습니다'
            ]"
=======
            :max="10"
            v-model="task.class_field"
            required
>>>>>>> db26c2a (Style & Fix : 스타일 및 오류 수정)
          />
<<<<<<< HEAD
        </div>
        <hr>
      </div>
      <div class="row">
        <span class="q-py-md q-ml-sm q-mr-lg text-size" style="width: 70px; text-align:center">제출기한</span>
        <q-input
          outlined
          stack-label
          type="date"
          v-model="task.deadline"
        />
<<<<<<< HEAD
        <q-input
=======
          <q-input
            outlined
            stack-label
            type="date"
            label="제출기한"
            v-model="task.deadline"
          />
        </div>
        <q-input
>>>>>>> 0e01249 (Feat : 객관식 문항 /로 구분해 저장 기능 완료)
          label="첨부파일"
          stack-label
          outlined
          @update:model-value="val => { task.files = val }"
          multiple
          type="file"
        />
        <div>
<<<<<<< HEAD
          <q-btn label="초기화" type="reset" color="primary" flat class="q-ml-sm" />
          <q-btn :label="type" color="primary" @click="onSubmit(false)" />
          <q-btn v-if="!isTeacher" label="제출" color="primary" @click="onSubmit(true)"/>
          <router-link class="button" :to="{name:'TaskListView', params: {userType,}}">
            <q-btn label="목록" color="primary"/>
          </router-link>
=======
          <q-btn label="등록" type="submit" color="primary"/>
          <q-btn label="초기화" type="reset" color="primary" flat class="q-ml-sm" />
>>>>>>> 0e01249 (Feat : 객관식 문항 /로 구분해 저장 기능 완료)
        </div>
      </q-form>
    </section>
=======
      </div>
      <hr>
      <div class="row items-center">
        <span class="q-py-md q-ml-sm q-mr-lg text-size" style="width: 70px; text-align:center">첨부파일</span>
        <input class="text-size" type="file" @change="onFileSelected" multiple>
      </div>
      <hr>
      <div class="row justify-center q-mt-xl q-gutter-md">
        <q-btn label="초기화" type="reset" color="primary" flat class="q-ml-sm" />
        <q-btn :label="type" color="primary" @click="onSubmit(false)"  class="text-size q-px-xl q-py-md" />
        <q-btn v-if="!isTeacher" label="제출" color="primary" @click="onSubmit(true)"  class="text-size q-px-xl q-py-md"/>
        <router-link class="button" :to="{name:'TaskListView', params: {userType,}}">
          <q-btn label="목록" color="primary"  class="text-size q-px-xl q-py-md" />
        </router-link>
      </div>
    </q-form>
>>>>>>> db26c2a (Style & Fix : 스타일 및 오류 수정)
  </main>
</template>

<script>
<<<<<<< HEAD
import { reactive, computed, onBeforeMount} from 'vue'
<<<<<<< HEAD
=======
import { ref, reactive, computed } from 'vue'
>>>>>>> 0e01249 (Feat : 객관식 문항 /로 구분해 저장 기능 완료)
import { useRoute } from 'vue-router'
=======
import { useRoute, useRouter } from 'vue-router'
>>>>>>> c8c893f (Feat: 로그인 여부 & 사용자 여부에 따른 접근 제한)
import {useStore} from 'vuex'
export default {
  name: 'TaskFormView',
  setup () {
    const route = useRoute()
    const store = useStore()
<<<<<<< HEAD
<<<<<<< HEAD
=======
    const router = useRouter()
>>>>>>> c8c893f (Feat: 로그인 여부 & 사용자 여부에 따른 접근 제한)
    let {userType, taskPk} = route.params
    onBeforeMount(() => {
      if (!this.isLoggedIn) {
      router.push('/educolab/login')
    } else if (taskPk) {
        store.dispatch('initTask')
        store.dispatch('taskDetail', {pk: taskPk, teacher_flag: userType === 'teacher'? 1:0})
    }
    })
    const subjectOptions = store.getters.getSubject
    let isTeacher = computed(() => userType === 'teacher')
    let type = computed(() => taskPk? '수정':'등록')
    const storeTask = computed(() => store.getters.getTask)
    const computedTask = reactive({
      subject: computed(() => storeTask.value.homework?.subject),
      title: computed(() => storeTask.value.homework?.title || storeTask.value.title),
      content: computed(() => storeTask.value.homework?.content || storeTask.value.content),
      grade: computed(() => storeTask.value.homework?.grade),
      class_field: computed(() => storeTask.value.homework?.class_field),
      files: computed(() => storeTask.value.homework?.files || storeTask.value['student_file']),
      deadline: computed(() => storeTask.value.homework?.deadline || storeTask.value.deadline),
    })
    const task = reactive({
      teacher_flag: isTeacher.value? 1:0,
      subject: taskPk? computedTask.subject: '',
      title: taskPk? computedTask.title: '',
      content: taskPk? computedTask.content : '',
      grade: taskPk? computedTask.grade : '',
      class_field: taskPk? computedTask.class_field : '',
      files: taskPk? computedTask.files : '',
      deadline: taskPk? computedTask.deadline : '',
    })
    const onSubmit = (arg) => {
      let form = new FormData()
      for (let key in task) {
        if (key === 'files' && task[key]) {
          for (let i=0; i < task.files.length; i++) {
            form.append(key, task[key][i])
          }
        } else {
          form.append(key, task[key])
        }
      }
      if (arg) {
        form.append('submit_pk', storeTask.value['my_submit'][0].id)
        store.dispatch('submitTask', form)
      } else if (taskPk) {
        form.append('pk', taskPk)
        store.dispatch('taskUpdate', form)
        console.log('update')
      } else {
        store.dispatch('createTask', form)
        console.log('create')
      }
    }
    const onReset = (event) => {
      event.preventDefault()
      if (taskPk) {
        for (let key in task) {
          if (key === 'teacher') {
              task[key] = store.getters.currentUser.username
            } else if (key === 'subject') {
              task[key] = store.getters.currentUser.subject
            } else {
            task[key] = storeTask.value[key]
          }
        }
      } else {
        for (let key in task) {
          task[key] = ''
        }
      }
    }
    return {
      task,
      storeTask,
      userType,
      taskPk,
      type,
      isTeacher,
      onSubmit,
      onReset,
      subjectOptions,
      computedTask
    }
  }
}
</script>
=======
    const subjectOptions = store.getters.getSubject
    let userType = route.params.userType
    let isTeacher = computed(() => userType === 'teacher')
    let taskPk = route.params.taskPk
    const task = reactive({
      teacher: store.getters.currentUser.username,
      subject: store.getters.currentUser.subject,
      title: null,
      content: null,
      grade: null,
      class_field: null,
      files: null,
      deadline: null,
    })
    const accept = ref(false)
    const onSubmit = (event) => {
      event.preventDefault()
      store.dispatch('createTask', task)
    }
    const onReset = (event) => {
      event.preventDefault()
      for (let key in task) {
        task[key] = null
      }
    }

<<<<<<< HEAD
    return {
      task,
      accept,
      userType,
      taskPk,
      isTeacher,
      onSubmit,
      onReset,
      subjectOptions
    }
  }
}
</script>

import {reactive} from 'vue'
setup() {
  credential
}
>>>>>>> 0e01249 (Feat : 객관식 문항 /로 구분해 저장 기능 완료)
=======
<style scoped>
  p {
    margin: 0;
  }
  .text-size {
    font-size: 1rem;
  }
</style>
>>>>>>> db26c2a (Style & Fix : 스타일 및 오류 수정)
