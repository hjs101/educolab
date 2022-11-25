<template>
  <div>
    <!-- 과목 (교사) -->
<<<<<<< HEAD
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
=======
    {{userType}}
    <q-select v-if="userType === 'teacher'" v-model="userData.subject" :options="subjectOptions" label="과목" />
    <!-- 학년/반 (학생) -->
    <div v-else>
      <q-select v-model="userData.grade" :options="[1,2,3]" label="학년" />
      <q-input
        v-model="userData.classField"
        color="teal"
        label="반"
        type="number"
        min="1"
        lazy-rules
        :rules="[ val => val && val.length > 0 || '반을 입력해주세요']"
>>>>>>> 147871f (Feat : 회원가입 틀 제작 후 이름까지 완료 (그 이후 부분은 미완성))
      />
    </div>
  </div>
</template>

<script>
<<<<<<< HEAD
import {ref} from '@vue/reactivity'
import {useStore} from 'vuex'
import {watch} from 'vue'
=======
import {reactive} from '@vue/reactivity'
>>>>>>> 147871f (Feat : 회원가입 틀 제작 후 이름까지 완료 (그 이후 부분은 미완성))
export default {
  name: 'TeacherOrStudent',
  props: {
    userType: String,
  },
  setup() {
<<<<<<< HEAD
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
=======
    const subjectOptions = [
    '국어', '수학', '사회', '과학', '보건', '기술가정', '기타'
    ]
    const userData = reactive({
      subject: '',
      grade: '',
      classField: ''
    })
    return {
      subjectOptions,
      userData
>>>>>>> 147871f (Feat : 회원가입 틀 제작 후 이름까지 완료 (그 이후 부분은 미완성))
    }
  }
}
</script>