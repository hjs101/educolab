<template>
  <div>
    <div class="test">
      <!-- 첫번째 라인 -->
      <button class="test" @click='sendMessage(send_test)'>학생 입장용 테스트 메시지 전송</button>

      <div class="test hor">
        <div class="test">방 번호 : {{all.RoomNumber}}</div>
        <div class="test">
          <div class="test">---퀴즈 대기중---</div>
          <div class="test hor">
            <div class="test">---입장한 사람수--- {{ans_list.length}}</div>
            <button @click='quiz_start()' >퀴즈 시작</button>
          </div>
        </div>
      </div>
      <!-- 두번째 라인 -->
      <div class="test hor">
        <div class="test" v-for="item in ans_list" :key="item">{{item}}</div>
      </div>
    </div>
    <router-link to="/quiz"><button class="test" @click='quiz_end()'>소켓 종료 & 목록으로</button></router-link>
  </div>
</template>

<script>
import { mapGetters, mapMutations, mapActions } from "vuex";

export default {
  name: "QuizWait",
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
      },
    }
  },

  created() {
    // this.RoomNumber = Math.floor(Math.random()*90000000)+10000000
    // 테스트용
    this.all.RoomNumber = 12341234
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
    },
    quiz_start(){
      this.cnt_flag(false)
      this.sendMessage(this.send_sig)
      this.$router.push({name:'QuizProb', params:{probNum:1}})
    },
  },

  mounted() {
  this.getQuizDetail(this.$route.params.quizPk)
  },
}

</script>

<style>

  .test{
    border:2px solid black;
    }

  .hor{
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
  }
</style>