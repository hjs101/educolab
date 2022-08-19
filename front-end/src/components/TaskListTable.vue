<template>
  <q-markup-table class="q-ma-md">
    <thead>
      <tr class="text-center text-size">
        <th class="text-size">번호</th>
        <th class="text-size">제목</th>
        <!-- 학생이 만든 문제만 작성자 표시 -->
        <th class="text-size" v-if="!teacher && isTeacher">작성자</th>
        <!-- 학생이 만든 문제에서는 과목과 대상 표시 X -->
        <th class="text-size" v-if="!isTeacher && teacher">과목</th>
        <th class="text-size" v-if="isTeacher && teacher">대상</th>
        <th class="text-size">제출 기한</th>
      </tr>
    </thead>
    <tbody>
      <tr
        v-for="(item, index) in data.list.slice((data.page-1)*10, data.page*10)"
        :key="item.id"
        class="text-center">
        <td class="text-size">{{ index+1+((data.page-1)*10) }}</td> 
        <td class="cursor-pointer text-left text-size" @click="toDetail(item.id)">{{ item.title }}</td>
        <td class="text-size" v-if="!search && !isTeacher && teacher">{{ item.subject }}</td>
        <td class="text-size" v-if="isTeacher">
          <span v-if="!search">
            {{item.grade || item.student?.grade}}학년 {{item.class_field || item.student?.class_field}}반
          </span>
          <span v-if="!teacher">
            {{item.student?.name || name}}
          </span>
          </td>
        <td class="text-size">{{ item.deadline }}</td>
      </tr>
    </tbody>
  </q-markup-table>
</template>

<script>
import { computed, reactive } from '@vue/runtime-core'
import {useRoute, useRouter} from 'vue-router'
import {useStore} from 'vuex'
export default {
  name: 'TaskListTable',
  props: {
    list: Array,
    page: Number,
    teacher: Number,
    submit: Boolean,
    search: Boolean,
  },
  setup(props) {
    const route = useRoute()
    const router = useRouter()
    const store = useStore()
    const {userType} = route.params
    const name = computed(() => store.getters.currentUser.name)
    const isTeacher = computed(() => userType === 'teacher')
    const taskType = computed(() => props.teacher? 'lecture':'self')
    const data = reactive({
      list: computed(() => props.list),
      page: computed(() => props.page)
    })
    const toDetail = (pk) => {
      if (userType === 'student' && !props.teacher && !props.submit) {
        router.push({name: 'TaskUpdateView',
        params: {
          userType: userType, taskPk: pk
        }})
      } else {
        router.push({name: 'TaskDetailView',
        params: {
          userType: userType, taskType:taskType.value ,taskPk: pk
        }})
      }
    }
    return {
      userType,
      taskType,
      toDetail,
      isTeacher,
      data,
      name
    }
  }
}
</script>

<style scoped>
  .text-size{font-size: 1rem;}
  .searchWrap{border-radius:5px; text-align:center; padding:20px 0; margin-bottom:10px;}
  .tbList th{border-top:1px solid #888;}
	.tbList th, .tbList td{border-bottom:1px solid #eee; padding:5px 0;}
	.tbList td.txt_left{text-align:left;}
  .btn{margin-bottom:40px;}
</style>