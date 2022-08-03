<template>
  <div>
    <input type="text" v-model="searchTitle">
    <button @click="onSearch(searchTitle)">검색</button>
  </div>
</template>

<script>
// import { mapActions, mapGetters } from 'vuex'
export default {
  name : "SearchNotice",
  data() {
    return {
      searchTitle : '',
    }
  },
  // computed: {
  //   ...mapGetters(['notice2'])
  // },
  // methods: {
  //   ...mapActions(['noticeList']),
  //   onSearch(searchTitle) {
  //     if (searchTitle !== '') {
  //       for (var i=0; i < this.notice2.length; i++) {
  //         if (searchTitle in notice2[i]) {
  //           this.searchNotice.push(notice)
  //         }
  //       }
  //     }
  //   }
  // }
}
</script>

<style>

</style>