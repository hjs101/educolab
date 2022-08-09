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
        checkedSelfTask: [],
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
    getCheckedSelfTask: state => state.student.checkedSelfTask,
    cntCheckedSelfTask: (state, getters) => Math.ceil(getters.getCheckedSelfTask.length/10),
    getTask: state => state.task,
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
            taskType: data.get('teacher')? 'lecture':'self',
            taskPk: res.data.pk
          }})
        })
        .catch(err => {
          // 페이지를 불러올 수 없습니다
          console.log(err.data)
        })
    },
    taskDetail({ getters, commit }, params) {
      console.log(params)
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
    taskUpdate({ getters }, data) {
      axios({
        url: drf.task.detail(),
        method: 'put',
        headers: {
          ...getters.authHeader,
        'Content-Type': 'multipart/form-data'},
        data,
      })
      .then(()=> {
        // 새로고침 -> currentUser가 날아가면서 오류 생김
        router.push({name: 'TaskDetailView', params: {
          userType: data['teacher_flag']? 'teacher': 'student',
          taskPk: data.get('pk'),
          taskType: data.get('teacher')? 'lecture':'self',
        }})
      })
      .catch(err => {
        console.log(err)
      })
    },
    taskDelete({ getters}, data) {
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
    submitTask({getters}, data) {
      axios({
        url: drf.task.submit(),
        method: 'post',
        headers: {
          ...getters.authHeader,
        'Content-Type': 'multipart/form-data'},
        data,
      })
    }
  }
}
