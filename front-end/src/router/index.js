// import { AppFullscreen } from 'quasar'
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  // 공지사항 (공통)
  {
    path: '/notice',
    name: 'Notice',
    component: () => import('@/views/NoticeView')
  },

  {
    path: '/notice/:contentId',
    name: 'NoticeDetailView',
    component: () => import('@/views/NoticeDetailView')
  },
  // 공지사항 작성
  {
    path: '/notice/create',
    name: 'NoticeForm',
    component: () => import('@/views/NoticeFormView')
  },

  // 과제(교사)
  {
    path: '/teacher/task',
    name: 'TeacherTask',
    component: () => import('@/views/TeacherTaskView')
  },

  // 퀴즈(교사)
  {
    path: '/quiz',
    name: 'Quiz',
    component: () => import('@/views/QuizView')
  },

  // 설문조사(교사)
  {
    path: '/search',
    name: 'Search',
    component: () => import('@/views/SearchView')
  },

  // 마이페이지(교사)
  {
    path: '/teacher',
    name: 'TeacherPage',
    component: () => import('@/views/TeacherPageView')
  },

  // 과제(학생)
  {
    path: '/student/task',
    name: 'StudentTaskListView',
    component: () => import('@/views/StudentTaskListView')
  },

  // 내 필기(학생)
  {
    path: '/student/writing',
    name: 'StudentWritingView.vue',
    component: () => import('@/views/StudentWritingView')
  },

  // 포인트 상점(학생)
  {
    path: '/student/store',
    name: 'StudentStoreView.vue',
    component: () => import('@/views/StudentStoreView')
  },

  // 마이 페이지(학생)
  {
    path: '/student',
    name: 'StudentPageView',
    component: () => import('@/views/StudentPageView')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
