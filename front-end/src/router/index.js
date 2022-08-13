<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e66f000 (navbar 생성)
=======
>>>>>>> e6b54fb (asdu)
=======
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
// import { AppFullscreen } from 'quasar'
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e6b54fb (asdu)
=======
=======
>>>>>>> 8e382a2 (Fix : 회원가입 오류 수정해 merge)
=======
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
  // 검색 공지사항
  {
    path: '/search',
    name: 'searchNotice',
    component: () => import ('@/components/SearchNotice')
  },
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3646f0b (공지사항 파일 업로드)
  // 회원 관리
  {
    path: '/',
    name: 'login',
    component: () => import ('@/views/LoginView')
  },  
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
  // Main
  {
    path: '/',
    name: 'TheNavbar',
    component: () => import('@/views/TheNavbar')
  },
>>>>>>> b22ae6e (공지사항 메인 페이지)
=======
>>>>>>> e6b54fb (asdu)

=======
  
>>>>>>> c780a28 (Feat : 아이디 찾기 기능 완료 & 비밀번호 찾기 진행 중)
=======
>>>>>>> 8e382a2 (Fix : 회원가입 오류 수정해 merge)
=======
>>>>>>> 452a9d1 (설문조사  등록)
=======
  // 로그인
  {
    path: '/educolab/login',
    name: 'login',
    component: () => import ('@/views/LoginView')
  },
>>>>>>> 9bb5647 (메인 페이지 css)
=======
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
  // 메인페이지 
  {
    path: '/educolab',
    name: 'educolab',
<<<<<<< HEAD
    component: () => import('@/components/MainPage')
  },
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 92fa455 (라우터 버그 수정)
=======

  // 메인페이지 
  {
    path: '/nav',
    name: 'nav',
    component: () => import('@/views/TheNavbar.vue')
  },
>>>>>>> 77a4159 (로그아웃 구현)
=======
>>>>>>> e6b54fb (asdu)
  // 공지사항
  {
    path: '/notice',
    name: 'Notice',
    component: () => import('@/views/NoticeView')
  },
<<<<<<< HEAD
  
  // 공지사항 상세 페이지
  {
    path: '/notice/detail/:noticePk',
    name: 'NoticeDetail',
    component: () => import('@/views/NoticeDetailView')
  },

=======
=======
>>>>>>> 9c886eb (Feat : 이메일 인증 부분 수정 & 아이디/비밀번호 찾기 기능 완료 & 비밀번호 변경 기능 진행 중)
=======
    component: () => import('@/views/MainPageView')
  },
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
=======
>>>>>>> bf6f861 (Feat : 교사 상/벌점 부여 기능 구현 완료)
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
  // 로그인
  {
<<<<<<< HEAD
<<<<<<< HEAD
    path: '/my-info',
    name: 'readMyInfo',
    component: () => import('@/views/FindView')
=======
    path: '/educolab/login',
    name: 'login',
    component: () => import ('@/views/LoginView')
  },
  // 메인페이지 
  {
    path: '/educolab',
    name: 'educolab',
    component: () => import('@/components/MainPage')
>>>>>>> bf6f861 (Feat : 교사 상/벌점 부여 기능 구현 완료)
  },
  // 회원가입
>>>>>>> c780a28 (Feat : 아이디 찾기 기능 완료 & 비밀번호 찾기 진행 중)
=======
    path: '/myinfo',
    name: 'ReadMyInfo',
    component: () => import('@/views/FindView')
  },
  // 회원가입
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
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
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======

>>>>>>> 5d02b22 (네브바, 컴포넌트 구성)
  // 공지사항
=======
  // 공지사항 (공통)
>>>>>>> 3d37e1b (공지사항 검색기능 구현)
  {
    path: '/notice',
    name: 'notice',
<<<<<<< HEAD
<<<<<<< HEAD
    component: () => import('@/views/NoticeView')
>>>>>>> e66f000 (navbar 생성)
  },

  // 과제(교사)
  {
<<<<<<< HEAD
=======
  },
  // 공지사항
  {
<<<<<<< HEAD
>>>>>>> e6b54fb (asdu)
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
=======
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
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)

  // 공지사항 작성
  {
    path: '/notice/create/:noticePk?',
<<<<<<< HEAD
    name: 'NoticeForm',
<<<<<<< HEAD
<<<<<<< HEAD
=======
    component: () => import('@/views/NoticeView'),
=======
    component: () => import('@/views/NoticeView')
>>>>>>> b22ae6e (공지사항 메인 페이지)
  },

  // 공지사항 작성
=======
    path: '/notice',
    name: 'Notice',
    component: () => import('@/views/NoticeView')
  },
>>>>>>> 9c886eb (Feat : 이메일 인증 부분 수정 & 아이디/비밀번호 찾기 기능 완료 & 비밀번호 변경 기능 진행 중)
  {
    path: '/notice/create',
    name: 'noticeForm',
>>>>>>> 5d02b22 (네브바, 컴포넌트 구성)
=======
>>>>>>> e6b54fb (asdu)
=======
    name: 'NoticeCreate',
<<<<<<< HEAD
>>>>>>> d127577 (기능별 메인 페이지 구성)
    component: () => import('@/views/NoticeFormView')
=======
    component: () => import('@/views/NoticeCreateView')
>>>>>>> 38a5ff1 (공지사항  수정 해결)
  },
<<<<<<< HEAD

  // 과제 메인
=======
  // 과제(교사)
>>>>>>> 3d91e39 (설문조사  등록 구현)
  {
<<<<<<< HEAD
    path: '/teacher/task',
    name: 'TeacherTask',
<<<<<<< HEAD
=======
    path: '/teacher/task',
    name: 'teacherTask',
>>>>>>> e66f000 (navbar 생성)
=======
>>>>>>> e6b54fb (asdu)
=======
    component: () => import('@/views/NoticeFormView')
  },

  // 과제(교사)
  {
    path: '/teacher/task',
    name: 'TeacherTask',
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
    component: () => import('@/views/TeacherTaskView')
  },

  // 과제(학생)
  {
    path: '/student/task',
    name: 'StudentTask',
    component: () => import('@/views/StudentTaskListView')
<<<<<<< HEAD
=======
    path: '/:userType/task',
    name: 'TaskListView',
    component: () => import('@/views/TaskListView')
>>>>>>> b5069a1 (Feat : 과제 목록 & 생성 & 상세 페이지 제작 진행 중)
  },
  // 과제 검색
  {
    path: '/:userType/task/search',
    name: 'SearchTaskView',
    component: () => import('@/views/SearchTaskView')
  },
  // 과제 상세 
  {
    path: '/:userType/task/detail/:taskType/:taskPk',
=======
  },
  // 과제 상세 
  {
    path: '/:userType/task/detail/:taskPk',
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
    name: 'TaskDetailView',
    component: () => import('@/views/TaskDetailView')
  },
  // 과제 생성
  {
    path: '/:userType/task/create',
    name: 'TaskCreateView',
<<<<<<< HEAD
    component: () => import('@/views/TaskFormview')
=======
    component: () => import('@/views/TaskCreateOrUpdateView')
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
  },
  // 과제 수정
  {
    path: '/:userType/task/update/:taskPk',
    name: 'TaskUpdateView',
<<<<<<< HEAD
    component: () => import('@/views/TaskFormview')
  },
<<<<<<< HEAD
  // 퀴즈(교사)
  {
    path: '/quiz',
<<<<<<< HEAD
<<<<<<< HEAD
    name: 'Quiz',
=======
    name: 'quiz',
>>>>>>> e66f000 (navbar 생성)
=======
    name: 'Quiz',
>>>>>>> e6b54fb (asdu)
=======
    component: () => import('@/views/TaskCreateOrUpdateView')
  },
  // 퀴즈(교사)
  {
    path: '/quiz',
    name: 'Quiz',
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
    component: () => import('@/views/QuizView')
  },

  // 설문조사(교사)
  {
    path: '/search',
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    name: 'Search',
=======
    name: 'search',
>>>>>>> e66f000 (navbar 생성)
=======
    name: 'Search',
>>>>>>> e6b54fb (asdu)
    component: () => import('@/views/SearchView')
=======

  // 설문조사(교사)
  {
    path: '/survey/',
    name: 'Survey',
    component: () => import('@/views/SurveyView')
  },

<<<<<<< HEAD
  // 설문조사 등록
  {
    path: '/survey/create',
    name: 'SurveyCreate',
    component: () => import('@/views/SurveyCreateView')
>>>>>>> 452a9d1 (설문조사  등록)
  },

=======
>>>>>>> 4cea92e (설문조사  수정 구현)
  // 설문조사 상세
  {
    path: '/survey/detail/:surveyPk',
    name: 'SurveyDetail',
    component: () => import('@/views/SurveyDetailView')
  },

  // 설문조사 등록
  {
    path: '/survey/create/:surveyPk?',
    name: 'SurveyCreate',
    component: () => import('@/views/SurveyCreateView')
  },

  // 설문조사 통계
  {
    path: '/survey/stat/:surveyPk',
    name: 'SurveyStat',
    component: () => import('@/views/SurveyStatView')
  },
  // 마이페이지
  {
<<<<<<< HEAD
    path: '/teacher',
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e6b54fb (asdu)
=======
    name: 'Search',
    component: () => import('@/views/SearchView')
  },

  // 마이페이지(교사)
  {
    path: '/teacher',
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
    name: 'TeacherPage',
    component: () => import('@/views/TeacherPageView')
=======
    path: '/:userType',
    name: 'MyPage',
    component: () => import('@/views/MyPageView')
>>>>>>> 1b417af (Feat : 학생 마이페이지 정보 조회, 포인트 내역 구현 중)
  },

  // 내 필기(학생)
  {
    path: '/student/writing',
    name: 'StudentWritingView.vue',
    component: () => import('@/views/StudentWritingView')
  },

  // 포인트 상점(학생)
  {
    path: '/student/point',
    name: 'StudentStoreView.vue',
    component: () => import('@/views/StudentStoreView')
  },
<<<<<<< HEAD
  
  // 마이 페이지(학생)
  {
    path: '/student',
    name: 'StudentPageView',
    component: () => import('@/views/StudentPageView')
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
  },
=======
>>>>>>> 1b417af (Feat : 학생 마이페이지 정보 조회, 포인트 내역 구현 중)
  // 404 에러
  {
    path: '/404',
    name: 'notFound',
    component: () => import ('@/views/NotFoundView')
  },
<<<<<<< HEAD
<<<<<<< HEAD
  // {
  //   path: '*',
  //   redirect: '/404'
  // }

>>>>>>> 23e74e9 (Feat : 로그인 화면 제작 완료 & 기능 구현 미완료 & 약관 동의 화면 구현)
=======
    name: 'teacherPage',
    component: () => import('@/views/TeacherPageView')
  },

<<<<<<< HEAD
>>>>>>> e66f000 (navbar 생성)
=======
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
>>>>>>> 3d37e1b (공지사항 검색기능 구현)
=======
  }
>>>>>>> e6b54fb (asdu)
=======
  },
  // 회원 관리
=======
  // 로그인
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
  {
    path: '/',
    name: 'login',
    component: () => import ('@/views/LoginView')
<<<<<<< HEAD
<<<<<<< HEAD
  },  
>>>>>>> c780a28 (Feat : 아이디 찾기 기능 완료 & 비밀번호 찾기 진행 중)
=======
  },
  // 404 에러
  {
    path: '/404',
    name: 'notFound',
    component: () => import ('@/views/NotFoundView')
  },
  // 로그아웃
  {
    path: '/logout',
    name: 'logout',
    meta: {
      reload:true,
    },
    redirect: '/'
  },
=======
>>>>>>> 9bb5647 (메인 페이지 css)

  // 퀴즈 메인 
  {
    path: '/quiz',
    name: 'Quiz',
    component: () => import('@/views/QuizView')
  },

  // 퀴즈 등록
  {
    path: '/quiz/create/:quizPk?',
    name: 'QuizCreate',
    component: () => import('@/views/QuizCreateView')
  },

  // 퀴즈 상세
  {
    path: '/quiz/detail/:quizPk',
    name: 'QuizDetail',
    component: () => import('@/views/QuizDetailView')
  },
<<<<<<< HEAD
=======
  // 로그아웃
  {
    path: '/logout',
    name: 'logout',
    // meta: {
    //   reload:true,
    // },
    redirect: '/educolab/login'
  },
>>>>>>> f7e1d76 (Feat : 학생 마이페이지 구현 완료 & 프로필/뱃지/칭호 변경 및 상벌점 부여 기능 진행 중)
  // 존재하지 않는 페이지
  {
    path: '/:pathMatch(.*)*',
    redirect: '/404'
  }
>>>>>>> 9c886eb (Feat : 이메일 인증 부분 수정 & 아이디/비밀번호 찾기 기능 완료 & 비밀번호 변경 기능 진행 중)
=======
  },
<<<<<<< HEAD
  // 존재하지 않는 페이지
  {
    path: '/:anything',
    redirect: '/404'
  },
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
=======
  // 로그인 페이지로 이동
  {
    path: '/',
    redirect: '/educolab/login'
  },
>>>>>>> bf6f861 (Feat : 교사 상/벌점 부여 기능 구현 완료)
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
