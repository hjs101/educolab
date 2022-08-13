<template>
  <div>
    <q-card class="my-card bg-yellow-13">
  
      <q-card-section class="row justify-between items-center card-bt">
        <div class="text-h6">공지사항</div>
        <div @click="goNotice" class="text-subtitle2 cursor-pointer">더보기 ></div>
      </q-card-section>
  
      <q-markup-table>
        <tbody v-for="mainNotice in mainNotice" :key="mainNotice" 
        class="row items-center card-pad">
          <tr>
            <td v-if="mainNotice.classification === '변경'" class="text-size text-pink-13">{{ mainNotice.classification }}</td>
            <td v-else-if="mainNotice.classification === '공지'" class="text-size text-indigo-13">{{ mainNotice.classification }}</td>
            <td v-else-if="mainNotice.classification === '행사'" class="text-size text-green-13">{{ mainNotice.classification }}</td>
            <td class="text-size">{{ mainNotice.title }}</td>
          </tr>
        </tbody>
      </q-markup-table>
    </q-card>
  </div>
</template>

<script>
export default {
  name: 'MainNotice',
  props: {
    mainNotice: Object,
  },
  methods: {
    goNotice() {
      this.$router.push({name:'Notice'})
    }
  }
}
</script>

<style scoped>
  .my-card {
    width: 400px;
  }
  .card-bt {
    border-bottom: 1px solid #FFC000;
  }
  .text-size {
    font-size: 1.1rem;
  }
  .clsif-border {
    border-radius: 30px;
  }
</style>