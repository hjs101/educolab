<template>
  <div class="back" >
    <div class="base">
      <div style="padding:5px 0">
        <span style="color:#FEC002;" class="logo">edu  </span>
        <span style="color:#00D300;" class="logo">colab</span>
      </div>
      <div class="hor" style="justify-content:center;align-items:center;">
        <div class="align" style="flex-direction:column; margin:20px 40px">
          <span style="font-size:25px;">퀴즈 방 번호</span>
          <span class="line">{{all.RoomNumber}}</span> 
        </div>
        <div class="align" style="padding:0 20px; flex-direction:column">
          <span class="person_num ">{{ans_list.length}}</span>
          <q-btn class="btn_next" @click='quiz_start()' square color="amber-5" glossy text-color="black" label="퀴즈 시작" />
        </div>
      </div>
      <!-- <button class="test" @click='sendMessage(send_test)'>학생 입장용 테스트 메시지 전송</button> -->
      <div class="back0">
        <div class="hor" style="position:absolute">
          <div class="element" v-for="item in ans_list" :key="item">{{item}}</div>
        </div>
      </div>
    </div>
    <div class="blank">
      <q-btn class="glossy btn_list" rounded color="green-9" @click='quiz_end()' label="퀴즈 목록" />
    </div>
  </div>
</template>

<script>
import { mapGetters, mapMutations, mapActions } from "vuex";

export default {
  name: "QuizWait",
  beforeRouteUpdate(to,from,next){
    this.closeSocket()
    next()
  },
  beforeRouteLeave(to,from,next){
    if(to.fullPath.includes(from.fullPath.split('/wait')[0]+'/prob/1')===false){
      this.sendMessage({
        message:"퀴즈 종료", 
        room_num:this.all.RoomNumber, 
        id:this.all.username})
      this.closeSocket()
    }
    next()
  },
  computed: { 
    ...mapGetters(['socket','ans_list','getUsername','quizDetail']),
  },
  data() {
    return {
      all:{
        username:"teacher01",
        quizPK: 0,
        RoomNumber:12341234,
        url:'',
      },
      send_test:{
        message:'학생 입장',
        id :'stu01',
        room_num : 0,
      },
      send_sig:{
        message:'퀴즈 시작',
        probPk:[],
      },
    }
  },

  created() {
    this.all.RoomNumber = Math.floor(Math.random()*90000000)+10000000
    // console.log(this.send_test)
    this.all.quizPK=this.$route.params.quizPk
    this.send_test.room_num=this.all.RoomNumber ///이거 테스트용임 지워도 됨
    this.all.username=this.getUsername
    this.all.url= "wss://i7c102.p.ssafy.io/api/ws/chat/"+this.all.RoomNumber+'/'
    this.cnt_flag(true)
    this.socket_on(this.all)

    ////////////테스트용
    this.send_test.room_num=this.all.RoomNumber
    },
  methods: {
    ...mapMutations({socket_on:"SOCKET_ON", sendMessage:"SOCKET_SEND", closeSocket:"SOCKET_CLOSE", cnt_flag:"SOCKET_COUNT_FLAG"}),
    ...mapActions(['getQuizDetail']),

    quiz_end(){
      this.sendMessage({
        message:"퀴즈 종료", 
        room_num:this.all.RoomNumber, 
        id:this.all.username})
      this.closeSocket()
      this.$router.push({name:'Quiz'})
    },
    quiz_start(){
      this.cnt_flag(false)
      this.send_sig.probPk=this.quizDetail[1].id
      this.sendMessage(this.send_sig)
      this.$router.push({name:'QuizProb', params:{probNum:1}})
    },
  },

  mounted() {
  this.getQuizDetail(this.$route.params.quizPk)
  },
}

</script>

<style scoped>
  a{
    text-decoration:none;
  }
  .logo{
    font-weight:bold;
    font-size:20px;
  }
  .align{
    align-items:center;
    text-align:center;
    justify-content:center;    
    display:flex;
    font-weight:bolder;
  }
  .line{
    border-top: 3px solid #FF9966;
    border-bottom: 3px solid #FF9966;
    padding: 5px 0;
    margin-top: 5px;
    font-size:100px;
    line-height:100px;
  }
  .back{
    background-color: #70AD47;
    width: 100vw;
    height: 100vh;
    display:table-cell;
    vertical-align:middle;
  }
  .base{
    display:flex;
    flex-direction:column;
    background-color: white;
    width:75%;
    height:75%;
    margin:0 auto;
    border:10px solid #497A28;
    border-radius:20pt;
    text-align:center;
  }
  .btn_next{
    color: black;
    border-radius: 10px;
    font-weight:bold;
    font-size: 20px;
    height:40%;
    margin-top:20px;
  }

  .btn_list{
    font-size:25px;
    width:300px;
    height:50px;
    display:block;
    margin:auto;
    border: 1px solid black;
    line-height:50px;
  }
  /* .btn_list{
    background-color:#497A28;
    color:white;
    font-size:15px;
    width:200px;
    height:50px;
    display:block;
    margin:auto;
    border: 1px solid black;

  } */
  .blank{
    width:100vw;
    height:12.5vh;
    display:table-cell;
    vertical-align:middle;
  }
  .test{
    border:2px solid black;
    }

  .hor{
    display: flex;
    flex-wrap: wrap;
  }
  .person_num{
    height:140px;
    width:140px;
    line-height:120px;
    font-size:50px;
    border-radius:50%;
    border:10px solid #70AD47;

  }
  .back0{
    background-color: aliceblue;
    margin:20px;
    padding:10px; 
    border-radius:10px;
    flex:1;
    overflow:hidden;
    position:relative;
  }
  .element{
    font-size:20px;
    margin: 5px 5px;
    font-weight:bold;
    padding:3px 8px;
    border-radius:20px;
    border:3px solid skyblue;
  }
</style>
