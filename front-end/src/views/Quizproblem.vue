<template>
  <div class="back">
    <div class="base">
      <!-- {{quizDetail[probNum].answer}} -->
      <div style="padding:5px 0">
        <span style="color:#FEC002;" class="logo">edu  </span>
        <span style="color:#00D300;" class="logo">colab</span>
      </div>
      <div class="align">
        <div class="problem">{{probNum}}. {{quizDetail[probNum].quiz_question}}</div> 
        <div v-if="prob_flag===false" class="cnt">{{cnt}}</div>
        <div style="display:flex; margin-top:20px;">
          <div v-if="result_flag" style="flex:1; font-size:30px; font-weight:bold; color:lightslategrey; margin-right:50px;"> 정답자 수 : {{ans_good_num}} </div>
          <q-btn  v-if="result_flag" class="btn_next" @click='quiz_start()' square color="amber-5" glossy text-color="black" label="다음 퀴즈" />
        </div>
        <!-- <div v-if="result_flag" class="test" style="position:absolute; height:40vh; width:75vw; top:500px; z-index:1;"></div> -->
        <!-- <div v-if="result_flag===false" class="test" style="position:absolute; height:50vh; width:75vw; top:450px; z-index:1;"></div> -->
        <div v-if="prob_flag" class="btns">
          <div class="hor2" style="margin-bottom:20px;">
            <q-btn v-if="result_flag===false || quizDetail[probNum].answer===1" align="left" class="btn btnp btn-fixed-width" rounded color="deep-orange-3" text-color="black" no-caps><p style="word-break:break-all;">{{quizDetail[probNum].multiple_bogi[0]}}</p></q-btn>
            <q-btn v-if="result_flag===true && quizDetail[probNum].answer!==1" align="left" class="btn btnp btn-fixed-width" rounded color="deep-orange-1" text-color="white" no-caps><p style="word-break:break-all;">{{quizDetail[probNum].multiple_bogi[0]}}</p></q-btn>
            <q-btn v-if="result_flag===false || quizDetail[probNum].answer===2"  align="left" class="btn btn-fixed-width" rounded color="light-green-3" text-color="black" no-caps><p style="word-break:break-all;">{{quizDetail[probNum].multiple_bogi[1]}}</p></q-btn>
            <q-btn v-if="result_flag===true && quizDetail[probNum].answer!==2"  align="left" class="btn btn-fixed-width" rounded color="light-green-1" text-color="white" no-caps><p style="word-break:break-all;">{{quizDetail[probNum].multiple_bogi[1]}}</p></q-btn>
          </div>
          <div class="hor2">
            <q-btn v-if="result_flag===false || quizDetail[probNum].answer===3"  align="left" class="btn btnp btn-fixed-width" rounded color="amber-3" text-color="black" no-caps><p style="word-break:break-all;">{{quizDetail[probNum].multiple_bogi[2]}}</p></q-btn>
            <q-btn v-if="result_flag===true && quizDetail[probNum].answer!==3"  align="left" class="btn btnp btn-fixed-width" rounded color="amber-1" text-color="white" no-caps><p style="word-break:break-all;">{{quizDetail[probNum].multiple_bogi[2]}}</p></q-btn>
            <q-btn v-if="result_flag===false || quizDetail[probNum].answer===4"  align="left" class="btn btn-fixed-width" rounded color="cyan-2" text-color="black" no-caps><p style="word-break:break-all;">{{quizDetail[probNum].multiple_bogi[3]}}</p></q-btn>
            <q-btn v-if="result_flag===true && quizDetail[probNum].answer!==4"  align="left" class="btn btn-fixed-width" rounded color="cyan-1" text-color="white" no-caps><p style="word-break:break-all;">{{quizDetail[probNum].multiple_bogi[3]}}</p></q-btn>
          </div>
        </div>
      </div>
    </div>
    <div class="blank">
      <q-btn class="glossy btn_list" rounded color="green-9" @click='quiz_end()' label="퀴즈 목록" />
    </div>
  </div>
</template>

<script>
import { mapGetters, mapMutations,mapActions} from "vuex";

export default {
  name: "QuizProb",
  mounted() {
      this.ansgoodData.room_num=this.RoomNumber
      this.ansgoodData.probPk=this.quizDetail[Number(this.probNum)].id
      this.quizTime.time_flag=false
      this.quizTime.timer= setInterval(()=>{
      if(this.quizTime.time_flag===false){
        this.quizTime.cnt++
        console.log(this.quizTime.cnt)
        if(this.quizTime.cnt===1){this.cnt="2"}
        if(this.quizTime.cnt===2){this.cnt="1"}
        if(this.quizTime.cnt===3){this.cnt="시작!"}
        if(this.quizTime.cnt===4){
          this.cnt=""
          this.prob_flag=true
        }
        if(this.quizTime.cnt===11){
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
      cnt: "3",
      quizPk : this.$route.params.quizPk,
      probNum : this.$route.params.probNum,
      send_sig:{
        message:'퀴즈 시작',
        probPk:[],
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
  beforeRouteLeave(to,from,next){
    if(to.fullPath.includes('/prob/')===false && to.fullPath.includes('/result')===false){
      this.sendMessage({
        message:"퀴즈 종료", 
        room_num:this.RoomNumber, 
        id:this.username})
      this.closeSocket()
    }
    clearInterval(this.quizTime.timer)
    next()
  },
  computed: { 
    ...mapGetters(['username','socket','quizDetail','RoomNumber','ans_good_num','quizDetail_len']),
  },
  methods: {
    ...mapActions(['ansgoodQuiz']),
    ...mapMutations({sendMessage:"SOCKET_SEND", cnt_flag:"SOCKET_COUNT_FLAG",closeSocket:"SOCKET_CLOSE"}),
      testInfo(){
        this.$router.push({name:'QuizWait'})
      },
    quiz_start(){
      clearInterval(this.quizTime.timer)
      if(this.quizDetail_len===(Number(this.probNum)+1)){
        this.sendMessage({message:'결과 보기'})
        this.$router.push({name:'QuizResult'})
      }
      else{
        this.send_sig.probPk=this.quizDetail[Number(this.probNum)+1].id
        // console.log(this.send_sig.)
        console.log(this.probNum)
        this.sendMessage(this.send_sig)
        this.prob_flag=false
        this.result_flag=false
        this.$router.push({name:'QuizProb', params:{probNum:Number(this.probNum)+1}})
      }
    },
    quiz_end(){
      this.sendMessage({
        message:"퀴즈 종료", 
        room_num:this.RoomNumber, 
        id:this.username})
      this.closeSocket()
      this.$router.push({name:'Quiz'})
    },
  }
}

</script>

<style scoped>
  a{
    text-decoration:none;
  }
  .btns{
    display:flex; 
    flex-direction:column; 
    flex:1; 
    width:100%; 
    padding:20px;
  }
  .test{
    border:2px solid black;
    }
  .align{
    display:flex;
    font-weight:bolder;
    /* display:flex; */
    flex:1;
    flex-direction:column;
    align-items:center;
    text-align:center;
    justify-content:center;
    /* font-weight:bolder; */
  }
  .hor2{
    display: flex;
    flex-wrap: wrap;
    flex:1;
    /* flex:1; */
    /* height:100% */
  }
  .btn_next{
    color: black;
    border-radius: 10px;
    font-weight:bold;
    font-size: 20px;
    height:30px;
  }
  .problem{
    width:100%;
    border-top: 30px solid #FF9966;
    border-bottom: 30px solid #FF9966;
    font-size:35px;
    padding: 30px 0;
  }
  .cnt{
    font-size:80px;
    padding:100px 0;
    color:lightslategray;
  }
  .btn{
    flex:1;
    border-radius:20px;
    font-size:30px;
  }
  .btnp{
    margin-right:20px;
    /* position:absolute;
    padding:20px;
    top:50%;
    left:0%;
    transform:translate(0,-50%);
    margin:0 */
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
  .btn_list{
    font-size:25px;
    width:300px;
    height:50px;
    display:block;
    margin:auto;
    border: 1px solid black;
    line-height:50px;
  }
  .blank{
    width:100vw;
    height:12.5vh;
    display:table-cell;
    vertical-align:middle;
  }
  .logo{
    font-weight:bold;
    font-size:20px;
  }
</style>
