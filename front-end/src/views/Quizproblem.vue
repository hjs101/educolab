<template>
  <div>
    <div class="test">
      <div>
        <div class=""></div> 
        <div class="title">{{title}}</div>
        <div class=""></div>
        <div v-if="result_flag" class="test">정답자:{{ans_good_num}}</div>
      </div>
      <button @click='quiz_start()'>다음 퀴즈</button>

      <div v-if="prob_flag" class="test">
        <div class="test hor">
          <div class="test">{{quizDetail[probNum].multiple_bogi[0]}}</div>
          <div class="test">{{quizDetail[probNum].multiple_bogi[1]}}</div>
        </div>
        <div class="test hor">
          <div class="test">{{quizDetail[probNum].multiple_bogi[2]}}</div>
          <div class="test">{{quizDetail[probNum].multiple_bogi[3]}}</div>
        </div>
      </div>
    </div> 
      
  </div>
</template>

<script>
import { mapGetters, mapMutations,mapActions} from "vuex";

export default {
  name: "QuizProb",
  mounted() {
      this.ansgoodData.room_num=this.RoomNumber
      this.quizTime.time_flag=false
      this.quizTime.timer= setInterval(()=>{
      if(this.quizTime.time_flag===false){
        this.quizTime.cnt++
        console.log(this.quizTime.cnt)
        if(this.quizTime.cnt===1){this.title="2"}
        if(this.quizTime.cnt===2){this.title="1"}
        if(this.quizTime.cnt===3){this.title=this.quizDetail[this.probNum].quiz_question}
        if(this.quizTime.cnt===4){
          this.prob_flag=true
        }
        if(this.quizTime.cnt===6){
          console.log(this.ansgoodData)
          this.ansgoodQuiz(this.ansgoodData)
          this.result_flag=true
          // this.quizTime.time_flag=true
        // }
        // if(this.quizTime.cnt===40){
          this.quizTime.time_flag=true
        }
      }
    }, 1000)
    },
  data() {
    return {
      prob_flag:false,
      result_flag:false,
      title: "3",
      quizPk : this.$route.params.quizPk,
      probNum : this.$route.params.probNum,
      send_sig:{
        message:'퀴즈 시작',
      },     
      quizTime:{
        timer: null,
        cnt:0,
        time_flag:false,
      },
      ansgoodData:{
        room_num: [],
        probPk:1
      }
    }
  },
  computed: { 
    ...mapGetters(['socket','quizDetail','RoomNumber','ans_good_num','quizDetail_len']),
  },
  methods: {
    ...mapActions(['ansgoodQuiz']),
    ...mapMutations({sendMessage:"SOCKET_SEND", cnt_flag:"SOCKET_COUNT_FLAG"}),
      testInfo(){
        this.$router.push({name:'QuizWait'})
      },
    quiz_start(){
      clearInterval(this.quizTime.timer)
      if(this.quizDetail_len===(Number(this.probNum)+1)){
        this.$router.push({name:'QuizResult'})
      }
      else{
        this.sendMessage(this.send_sig)
        this.prob_flag=false
        this.result_flag=false
        this.$router.push({name:'QuizProb', params:{probNum:Number(this.probNum)+1}})
      }
    },
  }
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