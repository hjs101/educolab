import drf from "@/api/drf.js"
import router from "@/router"
// import router from "@/router"
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
      },
      task: {},
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
    getTask: state => state.task,
    getTeacherAll: state => state.teacher.allDone + state.teacher.notCheck + state.teacher.notDone + state.teacher.studentTask,
    cntTeacherAll: (state, getters) => Math.ceil(getters.getTeacherAll.length/10), 
    getStudentAll: state => state.student.notDone + state.student.done + state.student.selfTask,
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
        } else if ( key === 'done') {
          studentKey = 'done'
        } else {
          studentKey = 'selfTask'
        }
        state.student[studentKey] = data[key]
      }
    },
    TASK_DETAIL: (state, data) => state.task = data,
    UPDATE_TASK: (state, data) => state.task = data,
    DELETE_TASK: (state) => state.task = [],
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
    createTask({ getters}, data) {
      axios({
        url: drf.task.create(),
        method : 'post',
        headers: {
          ...getters.authHeader,
        'Content-Type': 'multipart/form-data'},
        data,
      })
        .then(res => {
          router.push({name: 'TaskDetailView', params: {
            userType: getters.currentUser.userflag? 'teacher': 'student',
            taskPk: res.data.pk
          }})
        })
        .catch(err => {
          // 페이지를 불러올 수 없습니다
          console.log(err.data)
        })
    },
    taskDetail({ getters, commit }, taskPk) {
      axios({
        url: drf.task.detail(),
        method: 'get',
        headers: getters.authHeader,
        params: {
          pk : taskPk,
          teacher: 1
        }
      })
        .then(res => {
          console.log(res.data)
          commit('TASK_DETAIL', res.data)
        })
        .catch(err => {
          console.log(err)
        })
    },
    taskUpdate({ getters, commit }, data) {
      axios({
        url: drf.task.detail(),
        method: 'put',
        headers: getters.authHeader,
        data: data
      })
        .then(res => {
          console.log(res.data)
          commit('UPDATE_TASK', res.data)
        })
        .catch(err => {
          console.log(err)
        })
    },
    taskDelete({ getters, commit }) {
      axios({
        url: drf.task.detail(),
        method: 'delete',
        headers: getters.authHeader,
        data: task,
      })
        .then(res => {
          console.log(res.data)
          commit('DELETE_TASK')
        })
        .catch(err => {
          console.log(err)
        })
    },
    submitTask({getters}, data) {
      axios({
        url: drf.task.submit(),
        method: 'post',
        headers: getters.authHeader,
        data,
      })
    }
  }
}
