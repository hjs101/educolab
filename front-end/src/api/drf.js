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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
// const BASE_URL = 'https://i7c102.p.ssafy.io/api'
const BASE_URL = 'http://127.0.0.1:8000/api'
const PROFIL = 'http://127.0.0.1:8000'
// const PROFIL = 'https://i7c102.p.ssafy.io'
const ACCOUNTS = BASE_URL + '/accounts/'
const NOTICE = BASE_URL + '/notice/'
const HOMEWORK = BASE_URL + '/homework/'
=======
const BASE_URL = 'http://localhost:8000/'
=======
const BASE_URL = 'http://localhost:8000/api/'
>>>>>>> fc0382e (api url 수정)
const ACCOUNTS = BASE_URL + 'accounts/'
const NOTICE = BASE_URL + 'notice/'
const SURVEY = BASE_URL + 'survey/'
<<<<<<< HEAD

>>>>>>> 452a9d1 (설문조사  등록)
=======
const QUIZ = BASE_URL + 'quiz/'
>>>>>>> 4918ec5 (퀴즈 CRUD 폼 작성)
=======
const BASE_URL = 'https://i7c102.p.ssafy.io/api'
=======
// const BASE_URL = 'https://i7c102.p.ssafy.io/api'
const BASE_URL = 'http://127.0.0.1:8000/api'
>>>>>>> 1b417af (Feat : 학생 마이페이지 정보 조회, 포인트 내역 구현 중)
=======
// const BASE_URL = 'https://i7c102.p.ssafy.io/api'
const BASE_URL = 'http://127.0.0.1:8000/api'
>>>>>>> 38a5ff1 (공지사항  수정 해결)
=======
const BASE_URL = 'https://i7c102.p.ssafy.io/api'
// const BASE_URL = 'http://127.0.0.1:8000/api'
>>>>>>> 71858f1 (설문조사 sass)
const ACCOUNTS = BASE_URL + '/accounts/'
const NOTICE = BASE_URL + '/notice/'
const SURVEY = BASE_URL + '/survey/'
const QUIZ = BASE_URL + '/quiz/'
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9bb5647 (메인 페이지 css)
=======
const MY_PAGE = BASE_URL + '/mypage/'
>>>>>>> 1b417af (Feat : 학생 마이페이지 정보 조회, 포인트 내역 구현 중)
=======
=======
>>>>>>> 13e9331 (프로젝트  최신 버전)
const FILE = 'http://127.0.0.1:8000'
// const FILE = 'https://i7c102.p.ssafy.io'
=======
// const FILE = 'http://127.0.0.1:8000'
const FILE = 'https://i7c102.p.ssafy.io'
>>>>>>> 519727a (Fix: front_user 브랜치와 병합)
=======
// const FILE = 'http://127.0.0.1:8000'
const FILE = 'https://i7c102.p.ssafy.io'
>>>>>>> 9b08e30 (설문조사  주관식 답변  sass)
const BASE_URL = FILE + '/api/'
const ACCOUNTS = BASE_URL + 'accounts/'
const NOTICE = BASE_URL + 'notice/'
const SURVEY = BASE_URL + 'survey/'
const QUIZ = BASE_URL + 'quiz/'
const MY_PAGE = BASE_URL + 'mypage/'
const HOMEWORK = BASE_URL + 'homework/'
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 11b73f2 (Feat : 마이페이지 프로필 수정, 삭제 기능 구현 완료)
=======
const MainPage = BASE_URL + '/mainpage/'
>>>>>>> e824b6b (메인페이지 화면 구성)
=======
>>>>>>> 519727a (Fix: front_user 브랜치와 병합)
=======
const MainPage = BASE_URL + 'mainpage/'
>>>>>>> 13e9331 (프로젝트  최신 버전)

export default {
  accounts: {
    login: () => ACCOUNTS + 'login/',
    logout: () => ACCOUNTS + 'logout/',
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    signup: () => ACCOUNTS + 'registration/',
=======
    signup: () => ACCOUNTS + 'registration',
>>>>>>> 4628d97 ( Style : 디자인 수정)
    schoolInfo: () => ACCOUNTS + 'schoolinfo/',
    checkUsername: () => ACCOUNTS + 'check_username/',
    sendEmail: () => ACCOUNTS + 'send_signup_email/',
=======
    logout: () => ACCOUNTS + 'signup/',
>>>>>>> 2091835 (Feat: merge 전 수정 사항 반영)
=======
    signup: () => ACCOUNTS + 'signup/',
>>>>>>> c942112 (로그인 프론트와 백 연결)
=======
    signup: () => ACCOUNTS + 'signup/',
    schoolInfo: () => ACCOUNTS + 'schoolinfo/',
    checkUsername: () => ACCOUNTS + 'checkusername/',
<<<<<<< HEAD
    sendEmail: () => ACCOUNTS + 'sendemail',
>>>>>>> acd4b8a ( Feat : 아이디 중복 확인, 학교 검색, 이메일 인증 백과 통신 기능 추가)
=======
    signup: () => ACCOUNTS + 'registration/',
    schoolInfo: () => ACCOUNTS + 'schoolinfo/',
    checkUsername: () => ACCOUNTS + 'check_username/',
    findUsername: () => ACCOUNTS + 'find_username/',
    sendEmail: () => ACCOUNTS + 'send_signup_email/',
<<<<<<< HEAD
>>>>>>> 80ba160 ( Feat : 백과의 통신 (학교 검색과 회원가입은 미완료))
=======
    sendEmail: () => ACCOUNTS + 'sendemail/',
>>>>>>> 6e582c6 (develop 브랜치 푸시)
=======
    signup: () => ACCOUNTS + 'registration',
=======
    signup: () => ACCOUNTS + 'registration/',
>>>>>>> d7d3605 (feat : 비밀번호 변경 기능 구현)
    schoolInfo: () => ACCOUNTS + 'schoolinfo/',
    checkUsername: () => ACCOUNTS + 'check_username/',
    sendEmail: () => ACCOUNTS + 'send_signup_email/',
>>>>>>> e6b54fb (asdu)
=======
    sendPwEmail: () => ACCOUNTS + 'send_pw_email/',
<<<<<<< HEAD
>>>>>>> c780a28 (Feat : 아이디 찾기 기능 완료 & 비밀번호 찾기 진행 중)
=======
    changePw: () => ACCOUNTS + 'change_pw/',
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9c886eb (Feat : 이메일 인증 부분 수정 & 아이디/비밀번호 찾기 기능 완료 & 비밀번호 변경 기능 진행 중)
=======
    // changeInfo: () => ACCOUNTS + 
>>>>>>> fa227ef (Feat & Fix : 과제 생성/수정 기능 완료, 나머지 기능 진행 중, 회원 관리 부분 컴포넌트화 및 버그 수정 중)
=======
const BASE_URL = "http://3.36.69.192:8000/";
=======
const BASE_URL = "https://i7c102.p.ssafy.io/api/";
>>>>>>> c091697 (Test : 자동배포 테스트 마지막)
const ACCOUNTS = BASE_URL + "accounts/";
const NOTICE = BASE_URL + "notice/";

export default {
  accounts: {
    login: () => ACCOUNTS + "login/",
    logout: () => ACCOUNTS + "logout/",
    signup: () => ACCOUNTS + "registration/",
    schoolInfo: () => ACCOUNTS + "schoolinfo/",
    checkUsername: () => ACCOUNTS + "check_username/",
    findUsername: () => ACCOUNTS + "find_username/",
    sendEmail: () => ACCOUNTS + "send_signup_email/",
    sendPwEmail: () => ACCOUNTS + "send_pw_email/",
    changePw: () => ACCOUNTS + "change_pw/",
>>>>>>> 7dba180 (Test : 배포테스트)
  },

=======
  },
>>>>>>> 13e9331 (프로젝트  최신 버전)
  notice: {
<<<<<<< HEAD
    noticeList: () => NOTICE + 'main/',
    noticeDetail: () => NOTICE + 'detail/',
    noticeCreate: () => NOTICE + 'create/',
    noticeUpdate: () => NOTICE + 'update/'
  },
<<<<<<< HEAD
<<<<<<< HEAD
=======

  survey: {
    surveyList: () => SURVEY + 'main/',    
    surveyCreate: () => SURVEY + 'create/',
    surveyDetail: () => SURVEY + 'detail/',
    surveyUpdate: () => SURVEY + 'update/',
    surveyStat : () => SURVEY + 'stat/',
    surveyQuestion : () => SURVEY + 'stat/detail/'
  },

  quiz: {
    quizList: () => QUIZ + 'main/',
    quizCreate: () => QUIZ + 'create/',
    quizDetail: () => QUIZ + 'detail/',
  },

<<<<<<< HEAD
>>>>>>> 519727a (Fix: front_user 브랜치와 병합)
=======
  mainpage: {
    mainItem: () => MainPage
  },
>>>>>>> 13e9331 (프로젝트  최신 버전)
  task: {
    list: () => HOMEWORK + 'main/',
    create: () => HOMEWORK + 'create/',
    detail: () => HOMEWORK + 'detail/',
    check: () => HOMEWORK + 'check/',
    checkDone: () => HOMEWORK + 'check/done/',
    submit: () => HOMEWORK + 'submit/',
  },
  file: {
<<<<<<< HEAD
<<<<<<< HEAD
    path: () => BASE_URL,
=======

  survey: {
<<<<<<< HEAD
    surveyList: () => SURVEY + 'main/'    
>>>>>>> 452a9d1 (설문조사  등록)
=======
    surveyList: () => SURVEY + 'main/',    
<<<<<<< HEAD
    surveyCreate: () => SURVEY + 'create/'
>>>>>>> c450ef8 (설문조사  등록 구현)
=======
    surveyCreate: () => SURVEY + 'create/',
    surveyDetail: () => SURVEY + 'detail/',
<<<<<<< HEAD
>>>>>>> 3d91e39 (설문조사  등록 구현)
=======
    surveyUpdate: () => SURVEY + 'update/',
<<<<<<< HEAD
>>>>>>> 4cea92e (설문조사  수정 구현)
=======
    surveyStat : () => SURVEY + 'stat/',
    surveyQuestion : () => SURVEY + 'stat/detail/'
<<<<<<< HEAD
>>>>>>> 3d3b676 (설문조사  통계 조회)
=======
  },

  quiz: {
    quizList: () => QUIZ + 'main/',
    quizCreate: () => QUIZ + 'create/',
    quizDetail: () => QUIZ + 'detail/',
<<<<<<< HEAD
    quizUpdate: () => QUIZ + '',
<<<<<<< HEAD
>>>>>>> 4918ec5 (퀴즈 CRUD 폼 작성)
  }
=======
=======
>>>>>>> a482350 (퀴즈 수정  구현)
  },
>>>>>>> 9bb5647 (메인 페이지 css)
}
=======
const BASE_URL = "http://3.36.69.192:8000/";
=======
const BASE_URL = "http://127.0.0.1:8000/";
>>>>>>> 6339470 (Test : 자동배포 테스트)
=======
const BASE_URL = "http://3.36.69.192:8000/";
>>>>>>> b94cff3 (Test : 자동배포테스트)
=======
const BASE_URL = "https://i7c102.p.ssafy.io/api/";
>>>>>>> 0e0ba57 (Fix : 제발)
const ACCOUNTS = BASE_URL + "accounts/";
const NOTICE = BASE_URL + "notice/";

export default {
  accounts: {
    login: () => ACCOUNTS + "login/",
    logout: () => ACCOUNTS + "logout/",
    signup: () => ACCOUNTS + "registration/",
    schoolInfo: () => ACCOUNTS + "schoolinfo/",
    checkUsername: () => ACCOUNTS + "check_username/",
    findUsername: () => ACCOUNTS + "find_username/",
    sendEmail: () => ACCOUNTS + "send_signup_email/",
    sendPwEmail: () => ACCOUNTS + "send_pw_email/",
    changePw: () => ACCOUNTS + "change_pw/",
  },
  notice: {
<<<<<<< HEAD
=======
>>>>>>> 7dba180 (Test : 배포테스트)
    noticeList: () => NOTICE + "main/",
    noticeDetail: () => NOTICE + "detail/",
    noticeCreate: () => NOTICE + "create/",
    noticeUpdate: () => NOTICE + "update/",
  },
};
<<<<<<< HEAD
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
=======
>>>>>>> 7dba180 (Test : 배포테스트)
=======
    noticeList: () => NOTICE + 'main/',
    noticeDetail: () => NOTICE + 'detail/',
    noticeCreate: () => NOTICE + 'create/',
    noticeUpdate: () => NOTICE + 'update/'
  },

  survey: {
    surveyList: () => SURVEY + 'main/',    
    surveyCreate: () => SURVEY + 'create/',
    surveyDetail: () => SURVEY + 'detail/',
    surveyUpdate: () => SURVEY + 'update/',
    surveyStat : () => SURVEY + 'stat/',
    surveyQuestion : () => SURVEY + 'stat/detail/'

  },

  quiz: {
    quizList: () => QUIZ + 'main/',
    quizCreate: () => QUIZ + 'create/',
    quizDetail: () => QUIZ + 'detail/',
  },
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
}
>>>>>>> 11618aa (Fix : 병합해결)
=======
=======
  task: {
    list: () => HOMEWORK + 'main/',
    create: () => HOMEWORK + 'create/',
    detail: () => HOMEWORK + 'detail/',
    check: () => HOMEWORK + 'check/',
    checkDone: () => HOMEWORK + 'check/done/',
    submit: () => HOMEWORK + 'submit/',
  },
  file: {
=======
>>>>>>> 519727a (Fix: front_user 브랜치와 병합)
=======
>>>>>>> 13e9331 (프로젝트  최신 버전)
    path: () => FILE,
    change: () => '/api/media/accounts/profils/',
    default: () => '/api/media/accounts/profils/profile1.jpg'
  },
>>>>>>> f7e1d76 (Feat : 학생 마이페이지 구현 완료 & 프로필/뱃지/칭호 변경 및 상벌점 부여 기능 진행 중)
  myPage: {
    main: () => MY_PAGE + 'main/',
    point: () => MY_PAGE + 'grant/',
    changeProfil: () => MY_PAGE + 'profil/',
    changeTitle: () => MY_PAGE + 'title/',
  },
<<<<<<< HEAD
<<<<<<< HEAD
}
<<<<<<< HEAD
>>>>>>> 1b417af (Feat : 학생 마이페이지 정보 조회, 포인트 내역 구현 중)
=======
}
>>>>>>> f7e1d76 (Feat : 학생 마이페이지 구현 완료 & 프로필/뱃지/칭호 변경 및 상벌점 부여 기능 진행 중)
=======

  mainpage: {
    mainItem: () => MainPage
  }
}
>>>>>>> e824b6b (메인페이지 화면 구성)
=======
}
>>>>>>> 519727a (Fix: front_user 브랜치와 병합)
=======
}
>>>>>>> 13e9331 (프로젝트  최신 버전)
