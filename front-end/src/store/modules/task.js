import drf from "@/api/drf.js"
import router from "@/router"
import axios from "axios"

export const task = {
  state() {
    return {
      teacher: {
        allDone: [],
        notCheck: [],
        notDone: [],
        studentTask: [],
      },
      student: {
        notDone: [],
        done: [],
        selfTask: [],
        checkedSelfTask: [],
      },
      task: {},
      taskEdit: {},
    }
  },
  
  getters: {
    getTeacherDone: state => state.teacher.allDone,
    cntTeacherDone: (state, getters) => Math.ceil(getters.getTeacherDone.length/10),
    getTeacherNotCheck: state => state.teacher.notCheck,
    cntTeacherNotCheck: (state, getters) => Math.ceil(getters.getTeacherNotCheck.length/10),
    getTeacherNotDone: state => state.teacher.notDone,
    cntTeacherNotDone: (state, getters) => Math.ceil(getters.getTeacherNotDone.length/10),
    getTeacherStudentTask: state => state.teacher.studentTask,
    cntTeacherStudentTask: (state, getters) => Math.ceil(getters.getTeacherStudentTask.length/10),
    getStudentNotDone: state => state.student.notDone,
    cntStudentNotDone: (state, getters)=> Math.ceil(getters.getStudentNotDone.length/10),
    getStudentDone: state => state.student.done,
    cntStudentDone: (state, getters) => Math.ceil(getters.getStudentDone.length/10),
    getStudentSelfTask: state => state.student.selfTask,
    cntStudentSelfTask: (state, getters) => Math.ceil(getters.getStudentSelfTask.length/10),
    getCheckedSelfTask: state => state.student.checkedSelfTask,
    cntCheckedSelfTask: (state, getters) => Math.ceil(getters.getCheckedSelfTask.length/10),
    getTask: state => state.task,
    getEditTask: state => state.taskEdit,
    getTeacherAll: (state, getters) => [
    ...getters.getTeacherDone, ...getters.getTeacherNotCheck, ...getters.getTeacherNotDone, ...getters.getTeacherStudentTask
    ],
    cntTeacherAll: (state, getters) => Math.ceil(getters.getTeacherAll.length/10),
    getStudentAll: (state, getters) => [
    ...getters.getStudentNotDone, ...getters.getStudentDone, ...getters.getStudentSelfTask, ...getters.getCheckedSelfTask
    ],
    cntStudentAll: (state, getters) => Math.ceil(getters.getStudentAll.length/10),
  },

  mutations: {
    SET_TEACHER_TASK: (state, data) => {
      let teacherKey = null
      for (let key in data) {
        if (key === 'not_done') {
          teacherKey = 'notDone'
        } else if (key === 'done_notcheck') {
          teacherKey = 'notCheck'
        } else if ( key === 'all_done') {
          teacherKey = 'allDone'
        } else {
          teacherKey = 'studentTask'
        }
        state.teacher[teacherKey] = data[key]
      }
    },
    SET_STUDENT_TASK: (state, data) => {
      let studentKey = null
      for (let key in data) {
        if (key === 'notdone') {
          studentKey = 'notDone'
        } else if (key === 'done') {
          studentKey = 'done'
        } else if (key === 'my_homework') {
          studentKey = 'selfTask'
        } else {
          studentKey = 'checkedSelfTask'
        }
        state.student[studentKey] = data[key]
      }
    },
    TASK_DETAIL: (state, data) => state.task = data,
    TASK_EDIT: (state, data) => state.taskEdit = data,
    },

  actions: {
    taskList({ getters, commit }) {
      axios({
        url: drf.task.list(),
        method : 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          if (getters.currentUser.userflag) {
            commit('SET_TEACHER_TASK', res.data)
          } else {
            commit('SET_STUDENT_TASK', res.data)
          }
        })
        .catch(err => {
          // 페이지를 불러올 수 없습니다
          console.log(err.data)
        })
    },
    createTask({ commit, getters}, data) {
      console.log(data)
      axios({
        url: drf.task.create(),
        method : 'post',
        headers: {
          ...getters.authHeader,
        'Content-Type': 'multipart/form-data'},
        data,
      })
        .then(res => {
          if (data.get('teacher_flag') === '1') {
            commit('TASK_EDIT', {})
            router.push({name: 'TaskDetailView', params: {
              userType: getters.currentUser.userflag? 'teacher': 'student',
              taskType: 'lecture',
              taskPk: res.data.pk
            }}) 
          } else {
            commit('TASK_EDIT', {})
            router.push({name: 'TaskListView', params: {
              userType: getters.currentUser.userflag? 'teacher': 'student',
          }})
        }})
        .catch(err => {
          // 페이지를 불러올 수 없습니다
          console.log(err.data)
        })
    },
    taskDetail({ getters, commit }, params) {
      axios({
        url: drf.task.detail(),
        method: 'get',
        headers: getters.authHeader,
        params,
      })
        .then(res => {
          console.log(res.data)
          commit('TASK_DETAIL', res.data)
        })
        .catch(err => {
          console.log(err)
        })
    },
    editTask({ getters, commit }, params) {
      axios({
        url: drf.task.detail(),
        method: 'get',
        headers: getters.authHeader,
        params,
      })
        .then(res => {
          console.log(res.data)
          commit('TASK_EDIT', res.data)
        })
        .catch(err => {
          console.log(err)
        })
    },
    taskUpdate({getters, commit }, data) {
      axios({
        url: drf.task.detail(),
        method: 'put',
        headers: {
          ...getters.authHeader,
        'Content-Type': 'multipart/form-data'},
        data,
      })
      .then(()=> {
        if (getters.currentUser.userflag) {
          commit('TASK_EDIT', {})
          router.push({name: 'TaskDetailView', params: {
            userType: getters.currentUser.userflag? 'teacher': 'student',
            taskType: 'lecture',
            taskPk: data.get('pk')
          }}) 
        } else {
          commit('TASK_EDIT', {})
          router.push({name: 'TaskListView', params: {
            userType: 'student',
        }})
      }})
      .catch(err => {
        console.log(err)
      })
    },
    taskDelete({getters}, data) {
      console.log(data)
      axios({
        url: drf.task.detail(),
        method: 'delete',
        headers: getters.authHeader,
        data,
      })
        .then(() => {
          router.push({name: 'TaskListView', params: {
            userType: data.teacher? 'teacher':'student'
          }})
          router.go(0)
        })
        // .catch(err => {
        // })
    },
    submitTask({commit, getters}, data) {
      axios({
        url: drf.task.submit(),
        method: 'post',
        headers: {
          ...getters.authHeader,
        'Content-Type': 'multipart/form-data'},
        data,
      })
        .then(((res) => {
          commit('TASK_EDIT', {})
          console.log(res.data.message)
          router.push({name: 'TaskListView'})
        }))
      },
    }
  }
