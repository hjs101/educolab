<template>
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 5d02b22 (네브바, 컴포넌트 구성)
=======
>>>>>>> e6b54fb (asdu)
  <div class="row">
    <div class="col-2">1</div>
    <div class="col-8">퀴즈 메인 페이지</div>
    <div class="col-2">2</div>
<<<<<<< HEAD
<<<<<<< HEAD
=======
  <div>
    <h1>퀴즈 메인 페이지</h1>
  <router-view />
>>>>>>> e66f000 (navbar 생성)
=======
>>>>>>> 5d02b22 (네브바, 컴포넌트 구성)
=======
>>>>>>> e6b54fb (asdu)
=======
  <div>

    <!-- <q-form @submit="test">
      <label for="title">테스트: </label>
      <input type="text" id="title" v-model="title">
      <button type="submit">테스트</button>
    </q-form> -->

  <router-view />
>>>>>>> 2553da4 (공지사항  삭제)
=======
  <div>
    <h1>퀴즈 메인페이지</h1>
    <router-link :to="{name:'QuizCreate'}">
      <button>퀴즈 등록</button>
    </router-link>

>>>>>>> 4918ec5 (퀴즈 CRUD 폼 작성)
  </div>
</template>

<script>
<<<<<<< HEAD
export default {
  name: 'testList',
  // data() {
  //   return {
  //     title : '',
  //   }
  // },
  // methods: {
  //   test() {
  //     console.log(this.title)
  //   }
  // }
}
</script>
=======

export default({
  setup() {
    
  },
})
</script>

<style scoped>

</style>
>>>>>>> 4918ec5 (퀴즈 CRUD 폼 작성)
