<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e66f000 (navbar 생성)
// import { AppFullscreen } from 'quasar'
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
<<<<<<< HEAD
<<<<<<< HEAD
  // 회원 관리
  {
    path: '/',
    name: 'login',
    component: () => import ('@/views/LoginView')
  },  
<<<<<<< HEAD

  // 메인페이지 
  {
    path: '/educolab',
    name: 'educolab',
    component: () => import('@/views/MainPageView')
  },
=======
>>>>>>> 92fa455 (라우터 버그 수정)
  // 공지사항
  {
    path: '/notice',
    name: 'Notice',
    component: () => import('@/views/NoticeView')
  },
  
  // 공지사항 작성
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
=======
=======

>>>>>>> 5d02b22 (네브바, 컴포넌트 구성)
  // 공지사항
  {
    path: '/notice',
    name: 'notice',
<<<<<<< HEAD
    component: () => import('@/views/NoticeView')
>>>>>>> e66f000 (navbar 생성)
  },

  // 과제(교사)
  {
<<<<<<< HEAD
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
  {
    path: '/notice/create',
    name: 'NoticeForm',
=======
    component: () => import('@/views/NoticeView'),
  },
  
  // 공지사항 작성
  {
    path: '/notice/create',
    name: 'noticeForm',
>>>>>>> 5d02b22 (네브바, 컴포넌트 구성)
    component: () => import('@/views/NoticeFormView')
  },

  // 과제(교사)
  {
    path: '/teacher/task',
    name: 'TeacherTask',
=======
    path: '/teacher/task',
    name: 'teacherTask',
>>>>>>> e66f000 (navbar 생성)
    component: () => import('@/views/TeacherTaskView')
  },

  // 퀴즈(교사)
  {
    path: '/quiz',
<<<<<<< HEAD
    name: 'Quiz',
=======
    name: 'quiz',
>>>>>>> e66f000 (navbar 생성)
    component: () => import('@/views/QuizView')
  },

  // 설문조사(교사)
  {
    path: '/search',
<<<<<<< HEAD
    name: 'Search',
=======
    name: 'search',
>>>>>>> e66f000 (navbar 생성)
    component: () => import('@/views/SearchView')
  },

  // 마이페이지(교사)
  {
    path: '/teacher',
<<<<<<< HEAD
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
=======
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  // 회원 관리
  {
    path: '/login',
    name: 'login',
    component: () => import ('@/views/LoginView')
  },
  {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
>>>>>>> 1f63946 (vue 환경셋팅)
  }
=======
=======
=======
    path: '/signup/student',
    name: 'signupStudent',
    component: () => import ('@/views/SignupView')
  },
  {
>>>>>>> 147871f (Feat : 회원가입 틀 제작 후 이름까지 완료 (그 이후 부분은 미완성))
    path: '/signup/teacher',
    name: 'signupTeacher',
    component: () => import ('@/views/SignupView')
  },
  {
<<<<<<< HEAD
>>>>>>> 860f864 (Refactor : 로그인, 회원가입 동의 페이지 코드 수정 & 404 페이지 만듦)
=======
    path: '/signup/*',
    redirect: {name: 'NotFound'}
  },
=======
    path: '/signup/:userType',
    name: 'signup',
    component: () => import ('@/views/SignupView')
  },
>>>>>>> 03de9fd (Feat: 회원가입 학교 검색, 이름, 전화번호, 생년월일, 학년/반/번호)
  // signup 뒤에 student, teacher 아닌 것이 있으면 404 에러
  {
>>>>>>> 147871f (Feat : 회원가입 틀 제작 후 이름까지 완료 (그 이후 부분은 미완성))
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

>>>>>>> 23e74e9 (Feat : 로그인 화면 제작 완료 & 기능 구현 미완료 & 약관 동의 화면 구현)
=======
    name: 'teacherPage',
    component: () => import('@/views/TeacherPageView')
  }

>>>>>>> e66f000 (navbar 생성)
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
