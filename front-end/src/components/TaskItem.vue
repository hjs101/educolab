<template>
  <router-link div class="button black" :to="{name: 'TaskDetailView', params: {
    userType: userType, taskType,taskPk: item.pk
  }}">
    <q-card>
      <q-card-section >
        {{item.pk}}
        <div class="text-h6">{{item.title}}</div>
        <div class="text-subtitle2">~ {{item.deadline}}</div>
        <!-- <div class="text-subtitle2">{{item.teacher}}</div> -->
      </q-card-section>
      <q-card-section>
        {{item.grade}}학년 {{item.class_field}}반
        <!-- 학생 출제 과제라면 이름-->
      </q-card-section>
    </q-card>
  </router-link>
</template>

<style>
  .black {
    color: black;
  }
</style>

<script>
import {useRoute} from 'vue-router'
export default {
  name: 'TaskItem',
  props: {
    item: Object,
  },
  setup() {
    const route = useRoute()
    const {userType} = route.params
    return {
      userType
    }
  }
}
</script>