<template>
  <q-card @click="toDetail">
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
</template>

<style>
  .black {
    color: black;
  }
</style>

<script>
import { computed } from '@vue/runtime-core'
import {useRoute, useRouter} from 'vue-router'
export default {
  name: 'TaskItem',
  props: {
    item: Object,
    teacher: Number,
    submit: Boolean,
  },
  setup(props) {
    const route = useRoute()
    const router = useRouter()
    const {userType} = route.params
    const taskType = computed(() => props.teacher? 'lecture':'self')
    const toDetail = () => {
      if (userType === 'student' && !props.teacher && !props.submit) {
        router.push({name: 'TaskUpdateView',
        params: {
          userType: userType, taskPk: props.item.id
        }})
      } else {
        router.push({name: 'TaskDetailView',
        params: {
          userType: userType, taskType:taskType.value ,taskPk: props.item.id
        }})
      }
    }
    return {
      userType,
      taskType,
      toDetail
    }
  }
}
</script>