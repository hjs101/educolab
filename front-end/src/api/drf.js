const BASE_URL = 'http://localhost:8000/'
const ACCOUNTS = BASE_URL + 'accounts/'
const NOTICE = BASE_URL + 'notice/'

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
    sendEmail: () => ACCOUNTS + 'send_signup_email/',
>>>>>>> 80ba160 ( Feat : 백과의 통신 (학교 검색과 회원가입은 미완료))
=======
    sendEmail: () => ACCOUNTS + 'sendemail/',
>>>>>>> 6e582c6 (develop 브랜치 푸시)
=======
    signup: () => ACCOUNTS + 'registration',
    schoolInfo: () => ACCOUNTS + 'schoolinfo/',
    checkUsername: () => ACCOUNTS + 'check_username/',
    sendEmail: () => ACCOUNTS + 'send_signup_email/',
>>>>>>> e6b54fb (asdu)
  },
  notice: {
    noticeList: () => NOTICE
  }
}