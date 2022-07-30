<template>
  <div>
    <!-- 과목 (교사) -->
    <q-select v-if="userType === 'teacher'"
      color="teal"
      v-model="subject"
      label="과목"
      :options="subjectOptions"
      :value="subject.value"
    />
    <!-- 학년/반 (학생) -->
    <div v-else>
      <q-select
        color="teal"
        v-model="grade"
        :options="[1,2,3]"
        label="학년"
        :value="grade"
      />
      <q-input
        v-model="classField"
        color="teal"
        label="반"
        type="number"
        :dense="false"
        min="1"
        @change="sendData({class_field:classField})"
        lazy-rules
        :rules="[ val => val && val.length > 0 || '반을 입력해주세요', val => val > 0 || '적절하지 않은 값입니다']"
      />
    </div>
  </div>
</template>

<script>
import {ref} from '@vue/reactivity'
import {useStore} from 'vuex'
import {watch} from 'vue'
export default {
  name: 'TeacherOrStudent',
  props: {
    userType: String,
  },
  setup() {
    const store = useStore()
    const subjectOptions = [
    '국어', '수학', '사회', '과학', '보건', '기술가정', '기타'
    ]
    let subject = ref('')
    let grade = ref('')
    let classField = ref('')
    watch(subject, () => {
      sendData({subject:subject.value})
    })
    watch(grade, () => {
      sendData({grade:grade.value})
    })
    const sendData = (data) => {
      store.dispatch('changeData', data)
    }
    return {
      subjectOptions,
      sendData,
      subject,
      grade,
      classField
    }
  }
}
</script>