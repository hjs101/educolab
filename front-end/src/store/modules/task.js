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
      task: {
        
      },
    }
  },
  
  getters: {
    getTeacherDone: state => state.teacher.allDone,
    getTeacherNotCheck: state => state.teacher.notCheck,
    getTeacherNotDone: state => state.teacher.notDone,
    getTeacherStudentTask: state => state.teacher.studentTask,
    getStudentNotDone: state => state.student.notDone,
    getStudentDone: state => state.student.done,
    getStudentSelfTask: state => state.student.selfTask,
    getTask: state => state.task,
  },

  mutations: {
    SET_TEACHER_TASK: (state, data) => {
      console.log(1)
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
          homework_pk : taskPk,
          teacher: getters.currentUser.userflag
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
    submitTask({getters}) {
      axios({
        url: drf.task.submit(),
        method: 'post',
        headers: getters.authHeader,
        // data: ,
      })
    }
  }
}
