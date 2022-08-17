<template>
  <div>
    <q-card class="my-card bg-green-13">

      <q-card-section>
        <div class="row justify-between items-center" v-if="currentUser.userflag">
          <div class="text-h6">채점 안한 과제</div>
          <div @click="goTaskTeacher" class="text-subtitle2 cursor-pointer">더보기 ></div>
        </div>

        <div class="row justify-between items-center" v-else-if="!currentUser.userflag">
          <div class="text-h6">제출 안한 과제</div>
          <div @click="goTaskStudent" class="text-subtitle2 cursor-pointer">더보기 ></div>
        </div>
      </q-card-section>

      <q-markup-table style="height: 250px;">
        <tbody v-for="(mainHomework,index) in mainHomework" :key="index" class="card-pad">
          <tr>
            <td class="text-size">{{ index + 1}} . </td>
            <td class="text-size">{{ mainHomework.title}}</td>
            <td class="text-size">{{ mainHomework.deadline}}까지</td>
          </tr>
        </tbody>
      </q-markup-table>
    </q-card>

  </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'MainHomework',
  props: {
    mainHomework: Object,
  },
  computed: {
    ...mapGetters(['currentUser'])
  },
  methods: {
    goTaskTeacher() {
      this.$router.push({name:'TeacherTask'})
    },
    goTaskStudent() {
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
    font-size: 1rem;
  }
</style>