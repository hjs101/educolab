// import { AppFullscreen } from 'quasar'
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  // 검색 공지사항
  {
    path: '/search',
    name: 'searchNotice',
    component: () => import ('@/components/SearchNotice')
  },
  // 회원 관리
  {
    path: '/',
    name: 'login',
    component: () => import ('@/views/LoginView')
  },  

  // 메인페이지 
  {
    path: '/educolab',
    name: 'educolab',
    component: () => import('@/views/MainPageView')
  },
  // 공지사항
  {
    path: '/notice',
    name: 'Notice',
    component: () => import('@/views/NoticeView')
  },
  
  // 공지사항 상세 페이지
  {
    path: '/notice/detail/:noticePk',
    name: 'NoticeDetail',
    component: () => import('@/views/NoticeDetailView')
  },

  {
    path: '/signup/:userType',
    name: 'signup',
    component: () => import ('@/views/SignupView')
  },
  // signup 뒤에 student, teacher 아닌 것이 있으면 404 에러
  {
    path: '/signup',
    name: 'agree',
    component: () => import ('@/views/SignupAgreeView')
  },
  {
    path: '/nonlogin',
    redirect: {name: 'login'}
  },
  // 404 에러
  {
    path: '/404',
    name: 'notFound',
    component: () => import ('@/views/NotFoundView')
  },
  // {
  //   path: '*',
  //   redirect: '/404'
  // }

  // 공지사항 작성
  {
    path: '/notice/create/:noticePk?',
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
