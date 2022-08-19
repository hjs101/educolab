import drf from "@/api/drf.js"
import router from "@/router"
// import router from "@/router"
import axios from "axios"

export const quiz = {
  state() {
    return {
      quiz: {},
<<<<<<< HEAD
<<<<<<< HEAD
      quizDetail : {},
      quizData: [{}, {}],
      online:{
        username:'',
        socket:null,
        RoomNumber:0,
        quizPK:0,
        ans_list:[],
        cnt_flag:true,
        ans_good_num:0,
        ranking_list:[],
        quizDetail_len:0,
      }
    }
=======
      quizDetail: {},
=======
      quizDetail: [],
>>>>>>> 2f26b40 (퀴즈 수정 버그 4)
      quizData: [{}],
      online: {
        username: "",
        socket: null,
        RoomNumber: 0,
        quizPK: 0,
        ans_list: [],
        cnt_flag: true,
        ans_good_num: 0,
        ranking_list: [],
        quizDetail_len: 0,
      },
    };
>>>>>>> 2b10460 (프론트 버그 수정)
  },

  getters: {
<<<<<<< HEAD
    quiz : state => state.quiz,
    quizDetail : state => state.quizDetail,
    quizData : state => state.quizData,
<<<<<<< HEAD
<<<<<<< HEAD
    quizLength: state => Math.ceil(state.quiz.length/10),
=======
    socket: state=>state.online.socket,
    ans_list: state=>state.online.ans_list,
    RoomNumber: state=>state.online.RoomNumber,
    ans_good_num: state=>state.online.ans_good_num,
    quizDetail_len: state=>state.online.quizDetail_len,
    username: state=>state.online.username,
    ranking_list:state=>state.online.ranking_list,
>>>>>>> 7ae675e (Feat : 웹 퀴즈 기능 완료)
=======
    quizLength : state => Math.ceil(state.quiz/10),
>>>>>>> db26c2a (Style & Fix : 스타일 및 오류 수정)
=======
    quiz: (state) => state.quiz,
    quizDetail: (state) => state.quizDetail,
    quizData: (state) => state.quizData,
    quizLength: (state) => Math.ceil(state.quiz.length / 10),
    quizItemLength : state => state.quizDetail.length,
    socket: (state) => state.online.socket,
    ans_list: (state) => state.online.ans_list,
    RoomNumber: (state) => state.online.RoomNumber,
    ans_good_num: (state) => state.online.ans_good_num,
    quizDetail_len: (state) => state.online.quizDetail_len,
    username: (state) => state.online.username,
    ranking_list: (state) => state.online.ranking_list,
<<<<<<< HEAD
    quiz_length: (state) => state.quiz_length
>>>>>>> f247ee0 (퀴즈 수정페이지 버그 수정)
=======
>>>>>>> 1f2b28d (퀴즈 버그 수정3)
  },

  mutations: {
<<<<<<< HEAD
    SURVEY_LIST : (state, quiz) => state.quiz = quiz,
    QUIZ_DETAIL : (state, quizDetail) => state.quizDetail = quizDetail,
    QUIZ_DETAIL_LEN : (state, quizDetail) => state.online.quizDetail_len = quizDetail.length,
    QUIZ_DATA : (state, data) => state.quizData[data.question_number-1] = data,
    RANK_SCORE: (state)=>{
      let temp=[]
      console.log(state.online.ranking_list)
      for(let i of state.online.ranking_list){
        console.log(i)
        if(temp.length===0){
          temp.push(i.score)
        }
        else if(temp[0]!==i.score){
            temp.push(i.score)
=======
    SURVEY_LIST: (state, quiz) => (state.quiz = quiz),
    QUIZ_DETAIL: (state, quizDetail) => state.quizDetail = quizDetail,
    QUIZ_DETAIL_LEN: (state, quizDetail) =>
      (state.online.quizDetail_len = quizDetail.length),
    QUIZ_DATA: (state, data) =>
      (state.quizData[data.question_number - 1] = data),

    QUIZ_TOTAL_DATA : (state, data) => state.quizData = data, 

    RANK_SCORE: (state) => {
      let temp = [];
      for (let i of state.online.ranking_list) {
        if (temp.length === 0) {
          temp.push(i.score);
        } else if (temp[0] !== i.score) {
          temp.push(i.score);
>>>>>>> 2f26b40 (퀴즈 수정 버그 4)
        }
      }
<<<<<<< HEAD
      console.log(temp)
=======
>>>>>>> c2bb4de (공지사항 파일 버그 수정)
      return temp;
    },
<<<<<<< HEAD
    SOCKET_COUNT_FLAG : (state,flag)=>{
      state.online_cnt_flag=flag
=======
    // 일단 대기
    QUIZ_LEN: (state, length) => state.length = length,

    SOCKET_COUNT_FLAG: (state, flag) => {
      state.online_cnt_flag = flag;
>>>>>>> f247ee0 (퀴즈 수정페이지 버그 수정)
    },
<<<<<<< HEAD
    ANS_GOOD_NUM:(state,data)=>state.online.ans_good_num=data,
    RANKING_LIST:(state,data)=>state.online.ranking_list=data,
    SOCKET_ON : (state, data) =>{
      console.log("Starting connection to WebSocket Server")
      state.online.socket=new WebSocket(data.url)
      state.online.RoomNumber=data.RoomNumber
      state.online.quizPK=data.quizPK
      state.online.username=data.username
      state.online.ans_list=[]
      
      state.online.socket.addEventListener("message", (event) => {
        state.online.result = JSON.parse(event.data)//['message'] //test용
        // console.log("받기")
        console.log(state.online.result)
        // console.log(state.online.result.split('/'))
        if (state.online.cnt_flag===true && state.online.result['message']==="등록 성공"){
            state.online.ans_list.unshift(state.online.result['nickname'])
        }
      })
      state.online.socket.onclose = function(event) {
          console.log(event)
          console.error('Chat socket closed unexpectedly')
      }
      state.online.socket.addEventListener("open", (event) => {
        console.log(event)
        console.log("Successfully connected to the echo websocket server...")
        state.online.socket.send(JSON.stringify({
          message: '방 생성',
          id:state.online.username, //수정해야함
          room_num: state.online.RoomNumber,
          quiz_num: state.online.quizPK
        }));
      })
    },
    SOCKET_SEND :(state, data)=>{
      // console.log("보내기")
      // console.log(data)
=======
    ANS_GOOD_NUM: (state, data) => (state.online.ans_good_num = data),
    RANKING_LIST: (state, data) => (state.online.ranking_list = data),
    SOCKET_ON: (state, data) => {
      state.online.socket = new WebSocket(data.url);
      state.online.RoomNumber = data.RoomNumber;
      state.online.quizPK = data.quizPK;
      state.online.username = data.username;
      state.online.ans_list = [];

      state.online.socket.addEventListener("message", (event) => {
        state.online.result = JSON.parse(event.data);  //test용
        if (
          state.online.cnt_flag === true &&
          state.online.result["message"] === "등록 성공"
        ) {
          state.online.ans_list.unshift(state.online.result["nickname"]);
        }
      });

      state.online.socket.addEventListener("open", () => {
        state.online.socket.send(
          JSON.stringify({
            message: "방 생성",
            id: state.online.username, //수정해야함
            room_num: state.online.RoomNumber,
            quiz_num: state.online.quizPK,
          })
        );
      });
    },
    SOCKET_SEND: (state, data) => {
>>>>>>> c2bb4de (공지사항 파일 버그 수정)
      if(state.online.socket!==null){
        state.online.socket.send(JSON.stringify(data));
      }
    },
    SOCKET_CLOSE :(state)=>{
      if (state.online.socket!==null){
        state.online.socket.close()
        state.online.socket=null;
      }
    }
  },

  actions: {
    // 퀴즈 조회
    quizList( { getters, commit }) {
      axios({
        url: drf.quiz.quizList(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SURVEY_LIST', res.data)
        })
    },

    // 퀴즈 상세
    getQuizDetail({ getters, commit }, quizPk) {
      axios({
        url: drf.quiz.quizDetail(),
        method: 'get',
        headers: getters.authHeader,
        params: {
<<<<<<< HEAD
          quiz_num : quizPk
=======
          quiz_num: quizPk,
        },
<<<<<<< HEAD
      }).then((res) => {
        for (var i = 1; i < res.data.length; i++) {
          const bogi = res.data[i].multiple_bogi.split("/");
          res.data[i].multiple_bogi = bogi;
>>>>>>> 2b10460 (프론트 버그 수정)
        }
      })
        .then(res => {
          console.log(res.data)
          for (var i=1; i < res.data.length; i++) {
            const bogi = res.data[i].multiple_bogi.split('/')
            res.data[i].multiple_bogi = bogi
          }
          commit('QUIZ_DETAIL', res.data)
          commit('QUIZ_DETAIL_LEN', res.data)
        })
=======
      })
        .then((res) => {
          for (var i = 1; i < res.data.length; i++) {
            if (res.data[i].multiple_bogi) {
              const bogi = res.data[i].multiple_bogi.split('/');
              res.data[i].multiple_bogi = bogi;
            }
          }
          commit("QUIZ_DETAIL", res.data);
          commit("QUIZ_DETAIL_LEN", res.data);
      });
>>>>>>> 93e53ce (퀴즈 버그 수정....)
    },

<<<<<<< HEAD
    // 퀴즈 번호, 보기, 답 가져오기 
    onQuiz( { commit }, data) {
      console.log(data)
      commit('QUIZ_DATA', data)
    },

    createQuiz( { getters }, credentials) {
      credentials.question = getters.quizData
      console.log(credentials)
=======
    // 퀴즈 번호, 보기, 답 가져오기
    onQuiz({ commit }, data) {
      commit('QUIZ_DATA', data);
    },

    createQuiz({ getters }, credentials) {
      credentials.question = getters.quizData;
>>>>>>> e9e9cab (퀴즈 버그 수정)
      axios({
        url: drf.quiz.quizCreate(),
        method: 'post',
        headers: getters.authHeader,
<<<<<<< HEAD
        data : credentials
      })
        .then(router.push({ name: 'Quiz'}))
=======
        data: credentials,
      })
        .then(router.push({ name: "Quiz" }));
>>>>>>> e9e9cab (퀴즈 버그 수정)
    },

    deleteQuiz({ getters }, quizPk) {
      axios({
        url: drf.quiz.quizDetail(),
        method: 'delete',
        headers: getters.authHeader,
        params: {
          quiz_num : quizPk
        }
      })
        .then(alert('퀴즈가 삭제되었습니다.')),
        router.push({ name: 'Quiz'})
        .catch(err => {
          console.log(err)
        })
    },

    updateQuiz({ getters }, credentials) {
      credentials.question = getters.quizData
      axios({
        url: drf.quiz.quizDetail(),
        method: 'put',
        headers: getters.authHeader,
<<<<<<< HEAD
        data : credentials,
      })
        .then(res => {
          console.log(res)
          router.push({ name : 'Quiz' })
        })
=======
        data: credentials,
      })
        .then(
        router.push({ name: "Quiz" })
        )
>>>>>>> e9e9cab (퀴즈 버그 수정)
    },

    quizTotalData({ commit }, data) {
      commit('QUIZ_TOTAL_DATA', data)
    },
    ////////////////////////////////
<<<<<<< HEAD
    ansgoodQuiz({getters,commit}, data) {
      console.log(data)
=======
    ansgoodQuiz({ getters, commit }, data) {
<<<<<<< HEAD
      // console.log(data);
>>>>>>> 93e53ce (퀴즈 버그 수정....)
=======
>>>>>>> c2bb4de (공지사항 파일 버그 수정)
      axios({
        url: drf.quiz.quizScore(),
        method: 'get',
        headers: getters.authHeader,
        params: {
          quiz_question_id : data.probPk,
          room_num: data.room_num
        }
      })
        .then(res=>{
          commit('ANS_GOOD_NUM', res.data.ans_cnt)
        })
    },
    rankQuiz({getters,commit},roomNum) {
      axios({
        url: drf.quiz.quizRank(),
        method: 'get',
        headers: getters.authHeader,
        params: {
<<<<<<< HEAD
          room_num: roomNum
        }
      })
        .then(res=>{
          // console.log(res.data)
          commit('RANKING_LIST', res.data.ranks) //임시'
        })
        // .then(res=>{
        //   let result=commit('RANK_SCORE')
        //   console.log(result)
        //   console.log(res)
        // })
        // .then(res=>{
        //   let result=commit('RANK_SCORE')
        //   console.log(result)
        //   console.log(res)
        // })
=======
          room_num: roomNum,
        },
      }).then((res) => {
        commit("RANKING_LIST", res.data.ranks); //임시'
      });
>>>>>>> c2bb4de (공지사항 파일 버그 수정)
    },
    ///////////////////////////
  }
}