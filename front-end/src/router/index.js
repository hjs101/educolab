// import { AppFullscreen } from 'quasar'
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  // Main
  {
    path: '/',
    name: 'TheNavbar',
    component: () => import('@/views/TheNavbar')
  },

  // 공지사항
  {
    path: '/notice',
    name: 'notice',
    component: () => import('@/views/NoticeView')
  },

  // 공지사항 작성
  {
    path: '/notice/create',
    name: 'noticeForm',
    component: () => import('@/views/NoticeFormView')
  },
  // 과제(교사)
  {
    path: '/teacher/task',
    name: 'teacherTask',
    component: () => import('@/views/TeacherTaskView')
  },

  // 퀴즈(교사)
  {
    path: '/quiz',
    name: 'quiz',
    component: () => import('@/views/QuizView')
  },

  // 설문조사(교사)
  {
    path: '/search',
    name: 'search',
    component: () => import('@/views/SearchView')
  },

  // 마이페이지(교사)
  {
    path: '/teacher',
    name: 'teacherPage',
    component: () => import('@/views/TeacherPageView')
  }

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
