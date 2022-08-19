<template>
  <div>
    <td class="cursor-pointer text-left text-size">{{ item.title }}</td>
    <td class="text-size" v-if="isTeacher">
      {{item.grade || item.student?.grade}}학년 {{item.class_field || item.student?.class_field}}반
      <span v-if="!teacher">
        {{item.student.name}}
      </span>
      </td>
    <td class="text-size" v-if="!over">{{ item.deadline }}</td>
  </div>
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
    page: Number,
    teacher: Number,
    submit: Boolean,
    over: Boolean,
  },
  setup(props) {
    const route = useRoute()
    const router = useRouter()
    const {userType} = route.params
    const isTeacher = computed(() => userType === 'teacher')
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
      toDetail,
      isTeacher
    }
  }
}
</script>