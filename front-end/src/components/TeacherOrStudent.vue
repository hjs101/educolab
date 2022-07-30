<template>
  <div>
    <!-- 과목 (교사) -->
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 89ccfeb ( Feat: 회원 가입 기능 완료 (백 통신해서 디버깅 해야 함))
    <q-select v-if="userType === 'teacher'"
      color="teal"
      v-model="subject"
      label="과목"
      :options="subjectOptions"
      :value="subject.value"
    />
<<<<<<< HEAD
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
=======
>>>>>>> 03de9fd (Feat: 회원가입 학교 검색, 이름, 전화번호, 생년월일, 학년/반/번호)
    <q-select v-if="userType === 'teacher'" v-model="userData.subject" :options="subjectOptions" label="과목" />
=======
>>>>>>> 89ccfeb ( Feat: 회원 가입 기능 완료 (백 통신해서 디버깅 해야 함))
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
<<<<<<< HEAD
        :rules="[ val => val && val.length > 0 || '반을 입력해주세요']"
>>>>>>> 147871f (Feat : 회원가입 틀 제작 후 이름까지 완료 (그 이후 부분은 미완성))
=======
        :rules="[ val => val && val.length > 0 || '반을 입력해주세요', val => val > 0 || '적절하지 않은 값입니다']"
      />
<<<<<<< HEAD
      <q-input
        v-model="userData.classNumber"
        color="teal"
        label="번호"
        type="number"
        min="1"
        lazy-rules
        :rules="[ val => val && val.length > 0 || '번호를 입력해주세요', val => val > 0 || '적절하지 않은 값입니다']"
>>>>>>> 03de9fd (Feat: 회원가입 학교 검색, 이름, 전화번호, 생년월일, 학년/반/번호)
      />
=======
>>>>>>> bb316aa ( Feat : 회원가입 시 입력받은 정보를 취합하는 중)
    </div>
  </div>
</template>

<script>
<<<<<<< HEAD
<<<<<<< HEAD
import {ref} from '@vue/reactivity'
import {useStore} from 'vuex'
import {watch} from 'vue'
=======
import {reactive} from '@vue/reactivity'
>>>>>>> 147871f (Feat : 회원가입 틀 제작 후 이름까지 완료 (그 이후 부분은 미완성))
=======
import {ref} from '@vue/reactivity'
import {useStore} from 'vuex'
import {watch} from 'vue'
>>>>>>> 89ccfeb ( Feat: 회원 가입 기능 완료 (백 통신해서 디버깅 해야 함))
export default {
  name: 'TeacherOrStudent',
  props: {
    userType: String,
  },
  setup() {
<<<<<<< HEAD
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
=======
    const store = useStore()
>>>>>>> 89ccfeb ( Feat: 회원 가입 기능 완료 (백 통신해서 디버깅 해야 함))
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
<<<<<<< HEAD
      userData
>>>>>>> 147871f (Feat : 회원가입 틀 제작 후 이름까지 완료 (그 이후 부분은 미완성))
=======
      sendData,
      subject,
      grade,
      classField
>>>>>>> 89ccfeb ( Feat: 회원 가입 기능 완료 (백 통신해서 디버깅 해야 함))
    }
  }
}
</script>