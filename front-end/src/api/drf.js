// const BASE_URL = 'https://i7c102.p.ssafy.io/api'
const BASE_URL = 'http://127.0.0.1:8000/api'
const ACCOUNTS = BASE_URL + '/accounts/'
const NOTICE = BASE_URL + '/notice/'
const HOMEWORK = BASE_URL + '/homework/'

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
>>>>>>> 9c886eb (Feat : 이메일 인증 부분 수정 & 아이디/비밀번호 찾기 기능 완료 & 비밀번호 변경 기능 진행 중)
=======
    // changeInfo: () => ACCOUNTS + 
>>>>>>> fa227ef (Feat & Fix : 과제 생성/수정 기능 완료, 나머지 기능 진행 중, 회원 관리 부분 컴포넌트화 및 버그 수정 중)
  },
  notice: {
    noticeList: () => NOTICE + 'main/',
    noticeDetail: () => NOTICE + 'detail/',
    noticeCreate: () => NOTICE + 'create/',
    noticeUpdate: () => NOTICE + 'update/'
  },
  task: {
    list: () => HOMEWORK + 'main/',
    create: () => HOMEWORK + 'create/',
    detail: () => HOMEWORK + 'detail/',
    check: () => HOMEWORK + 'check/',
    submit: () => HOMEWORK + 'submit/',
  },
  file: {
    path: () => BASE_URL,
  }
}