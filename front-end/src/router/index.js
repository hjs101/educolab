// import { AppFullscreen } from 'quasar'
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  // 검색 공지사항
  {
    path: '/search',
    name: 'searchNotice',
    component: () => import ('@/components/SearchNotice')
  },
  // 메인페이지 
  {
    path: '/educolab',
    name: 'educolab',
    component: () => import('@/views/MainPageView')
  },
  // 아이디 & 비밀번호 찾기
  {
    path: '/find/:info',
    name: 'findInfo',
    component: () => import('@/views/FindView')
  },
  // 비밀번호 & 회원정보 변경
  {
    path: '/change/:userData',
    name: 'changeInfo',
    component: () => import('@/views/FindView')
  },
  // 회원정보 조회
  {
    path: '/myinfo',
    name: 'ReadMyInfo',
    component: () => import('@/views/FindView')
  },
  // 회원가입
  {
    path: '/signup/:userType',
    name: 'signup',
    component: () => import ('@/views/SignupView')
  },
  // 회원가입 동의 페이지
  {
    path: '/signup',
    name: 'agree',
    component: () => import ('@/views/SignupAgreeView')
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

  // 과제(학생)
  {
    path: '/student/task',
    name: 'StudentTaskListView',
    component: () => import('@/views/StudentTaskListView')
  },
  // 과제 상세 
  {
    path: '/:userType/task/detail/:taskPk',
    name: 'TaskDetailView',
    component: () => import('@/views/TaskDetailView')
  },
  // 과제 생성
  {
    path: '/:userType/task/create',
    name: 'TaskCreateView',
    component: () => import('@/views/TaskCreateOrUpdateView')
  },
  // 과제 수정
  {
    path: '/:userType/task/update/:taskPk',
    name: 'TaskUpdateView',
    component: () => import('@/views/TaskCreateOrUpdateView')
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
  },
  // 404 에러
  {
    path: '/404',
    name: 'notFound',
    component: () => import ('@/views/NotFoundView')
  },
  // 로그인
  {
    path: '/',
    name: 'login',
    component: () => import ('@/views/LoginView')
  },
  // 존재하지 않는 페이지
  {
    path: '/:anything',
    redirect: '/404'
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
