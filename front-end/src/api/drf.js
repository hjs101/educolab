const BASE_URL = 'http://localhost:8000/'
const ACCOUNTS = BASE_URL + 'accounts/'
const NOTICE = BASE_URL + 'notice/'

export default {
  accounts: {
    login: () => ACCOUNTS + 'login/',
    logout: () => ACCOUNTS + 'logout/',
    signup: () => ACCOUNTS + 'signup/',
    schoolInfo: () => ACCOUNTS + 'schoolinfo/',
    checkUsername: () => ACCOUNTS + 'checkusername/',
    sendEmail: () => ACCOUNTS + 'sendemail',
  },
  notice: {
    noticeList: () => NOTICE
  }

}