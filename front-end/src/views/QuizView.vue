<template>
  <div>

    <!-- <q-form @submit="test">
      <label for="title">테스트: </label>
      <input type="text" id="title" v-model="title">
      <button type="submit">테스트</button>
    </q-form> -->

  <router-view />
  </div>
</template>

<script>
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