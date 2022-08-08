<template>
  <router-link div class="button black" :to="{name: 'TaskDetailView', params: {
    userType: userType, taskType,taskPk: item.id
  }}">
    <q-card>
      <q-card-section >
        {{item.id}}
        <div class="text-h6">{{item.title}}</div>
        <div v-if="teacher" class="text-subtitle2">~ {{item.deadline}}</div>
      </q-card-section>
      <q-card-section>
        {{item.grade}}학년 {{item.class_field}}반
        <span v-if="!teacher"> {{item.student.name}}</span>
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
import { computed } from '@vue/runtime-core'
import {useRoute} from 'vue-router'
export default {
  name: 'TaskItem',
  props: {
    item: Object,
    teacher: Number,
  },
  setup(props) {
    const route = useRoute()
    const {userType} = route.params
    const taskType = computed(() => props.teacher?'lecture':'self')
    return {
      userType,
      taskType
    }
  }
}
</script>