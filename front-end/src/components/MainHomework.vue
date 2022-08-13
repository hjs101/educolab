<template>
  <div>
    <q-card class="my-card bg-green-13">

      <q-card-section class="row my-card justify-between items-center card-bt">
        <div class="text-h6">제출 안한 과제</div>
        <div @click="goTask" class="text-subtitle2 cursor-pointer">더보기 ></div>
      </q-card-section>

      <q-markup-table>
        <q-card-section class="bg-green-13 text-size" v-if="!mainHomework[0]">제출 안한 과제가 없습니다.</q-card-section>
        <q-card-section v-for="mainHomework in mainHomework" :key="mainHomework" class="card-pad">
          <div class="row">
            <p>{{ mainHomework.title }}</p>
            <p>{{ mainHomework.title }}</p>
          </div>
        </q-card-section>
      </q-markup-table>
    </q-card>

  </div>
</template>

<script>
export default {
  name: 'MainHomework',
  props: {
    mainHomework: Object,
  },
  methods: {
    goTask() {
      this.$router.push({name:'StudentTask'})
    }
  }
}
</script>

<style scoped>
  .my-card {
    width: 400px;
  }
  .card-pad {
    padding: 5px 0px 0px 0px;
  }
  .card-bt{
    border-bottom: 1px solid #8BFF8B
  }
  .text-size {
    font-size: 1.1rem;
  }
</style>