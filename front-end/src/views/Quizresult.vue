<template>
  <div class="back">
    <div class="base">
      <div style="padding:5px 0">
        <span style="color:#FEC002;" class="logo">edu  </span>
        <span style="color:#00D300;" class="logo">colab</span>
      </div>
      <div class="line">{{quizDetail[0].quiz_name}}</div>
        <div class="hor">
          <!-- <div v-if="person_flag" class="cnt">아무도 없습니다.</div> -->
          <!-- <div v-if="ranking_list"> -->
          <div class="box1" v-for="item in ranking_list" v-bind:key="item">
            <div :class="{'score_bar s1':item.rank===1,'score_bar s2':item.rank===2,'score_bar s3':item.rank===3,'score_bar s4':item.rank===4,'score_bar s5':item.rank===5}">{{item.score}}</div>
            <div class="title_name">{{item.name}}</div>
            <div class="title_name">[{{item.title}}]</div>
          </div>
          <!-- </div> -->
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
  name: "QuizResult",
    data() {
      return {
        height0:"100%",
        height1:"80%",
        height2:"60%",
        height3:"40%",
        height4:"20%",
      }
    },
  beforeRouteLeave(to,from,next){
    this.closeSocket()
    next()
  },
  created() {
    this.rankQuiz(this.RoomNumber)
  },
  computed: {
    ...mapGetters(['username','RoomNumber','ranking_list','quizDetail'])
  },
  methods: {
    ...mapActions(['rankQuiz']),
    ...mapMutations({socket_on:"SOCKET_ON", sendMessage:"SOCKET_SEND", closeSocket:"SOCKET_CLOSE", cnt_flag:"SOCKET_COUNT_FLAG"}),
    quiz_end(){
      console.log(this.RoomNumber)
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
  .cnt{
    font-size:80px;
    display:flex;
    flex-direction:column;
    justify-content: center;
    /* padding:100px 0; */
    color:lightslategray;
    font-weight:bold
  }
  .score_bar{
    width:80%;
    margin: 20px;
    font-size:15px;
    font-weight:bold;
    display:flex;
    align-items:center;
    text-align:center;
    justify-content:center;
  }
  .s1{
    background-color: #FFAB91;
    height:v-bind(height0);
  }
  .s2{
    background-color: #FFE082;
    height:v-bind(height1);
  }
  .s3{
    background-color: #C5E1A5;
    height:v-bind(height2);
  }
  .s4{
    background-color: #B2EBF2;
    height:v-bind(height3);
  }
  .s5{
    background-color: #E1BEE7;
    height:v-bind(height4);
  }
  .title_name{
    font-size: 18px;
    font-weight: bold;
    word-break:break-all;
  }
  .logo{
    font-weight:bold;
    font-size:20px;
  }
  .box1{
    display:flex;
    flex-direction: column-reverse;
    width:15%;
    align-items:center;
    /* text-align:center; */
    /* justify-content:center;   */
  }
  .test{
    border:2px solid black;
    }

  .hor{
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    flex:1;
    width:100%;
    padding: 30px;
    justify-content: space-evenly ;
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
  .line{
    /* border-top: 3px solid #FF9966; */
    border-bottom: 3px solid #FF9966;
    padding: 30px 0;
    margin-top: 5px;
    font-size:50px;
    line-height:50px;
    font-weight:bold;
    word-break:break-all;
  }
</style>