<template>
  <div>
    <!-- 과목 (교사) -->
    <q-select v-if="userType === 'teacher'" v-model="userData.subject" :options="subjectOptions" label="과목" />
    <!-- 학년/반 (학생) -->
    <div v-else>
      <q-select v-model="userData.grade" :options="[1,2,3]" label="학년" />
      <q-input
        v-model="userData.classField"
        color="teal"
        label="반"
        type="number"
        :dense="false"
        min="1"
        lazy-rules
        :rules="[ val => val && val.length > 0 || '반을 입력해주세요', val => val > 0 || '적절하지 않은 값입니다']"
      />
    </div>
  </div>
</template>

<script>
import {reactive} from '@vue/reactivity'
export default {
  name: 'TeacherOrStudent',
  props: {
    userType: String,
  },
  setup() {
    const subjectOptions = [
    '국어', '수학', '사회', '과학', '보건', '기술가정', '기타'
    ]
    const userData = reactive({
      subject: null,
      grade: null,
      classField: null,
    })
    return {
      subjectOptions,
      userData
    }
  }
}
</script>