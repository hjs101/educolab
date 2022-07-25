export default  {
  state: {
  },
  mutations: {
  },
  actions: {
    login () {
      // axios로 정보 보냄 // 아직 url 정해지지 않음
      // 성공 시 데이터 받고 main page로
      // (name, profil, email -> vuex -> navbar에서 사용할 것)
      // access, refresh -> local storage
      // userFlag -> main 페이지 결정
      /*
      성공 :
      'name' : name 
      'access': accessjwtToken
      'refresh' : refreshjwtToken,
      'userFlag': 'true(teacher) OR false(student)',
      'email' : email,
      'profil' : profilimg.png
      실패 : 상태코드
      */ 
      // 실패 시 상태 코드 -> '아이디나 비밀번호가 일치하지 않습니다'
      
      // axios.post('')
      //   .then(res => console.log(res))
      //   .catch(err => console.log(err))
      console.log('로그인 기능 함수 완성 필요')
    }
  }
}