<template>
  <div>
    <div class="test">{{quizDetail[0].quiz_name}}</div>
    <div class="hor">
      <div class="test" v-for="item in ranking_list" v-bind:key="item">
        <div class="test">[{{item.title}}]{{item.name}}</div>
        <div class="test">{{item.score}}</div>
        <div class="test"></div>
      </div>
    </div>
    <button @click='quiz_end()'>퀴즈 종료/목록으로</button>
  </div>
</template>

<script>
import { mapGetters, mapMutations, mapActions } from "vuex";

export default {
  name: "QuizResult",
    data() {
        return {
            message:''
        }
    },
  created() {

    this.rankQuiz(this.RoomNumber)
    console.log(this.ranking_list)

  },
  computed: {
    ...mapGetters(['username','RoomNumber','ranking_list','quizDetail'])
  },
  methods: {
    ...mapActions(['rankQuiz']),
    ...mapMutations({socket_on:"SOCKET_ON", sendMessage:"SOCKET_SEND", closeSocket:"SOCKET_CLOSE", cnt_flag:"SOCKET_COUNT_FLAG"}),
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