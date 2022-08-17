<template>
  <div>
    <!-- 과목 (교사) -->
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 89ccfeb ( Feat: 회원 가입 기능 완료 (백 통신해서 디버깅 해야 함))
=======
>>>>>>> e6b54fb (asdu)
=======
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
    <q-select v-if="userType === 'teacher'"
=======
    <q-select v-if="isTeacher"
>>>>>>> 086e088 (Feat : 회원정보 수정, 비밀번호 변경 페이지 구현 완료)
      color="teal"
      v-model="subject"
      label="과목"
      :options="subjectOptions"
      :value="subject.value"
    />
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e6b54fb (asdu)
=======
    <q-select v-if="userType === 'teacher'"
      color="teal"
      v-model="subject"
      label="담임여부"
      :options="['O', 'X']"
      :value="subject.value"
    />
    <!-- 담임여부 -->
=======
>>>>>>> bf6f861 (Feat : 교사 상/벌점 부여 기능 구현 완료)
=======
    <div v-if="isTeacher && changeType">
      교사 유형
      <q-radio
        dense
        v-model="homeroom.type"
        :val="true"
        label="담임"
        @click="sendData({homeroom_teacher_flag: 1})"/>
      <q-radio
        dense
        v-model="homeroom.type"
        :val="false"
        label="담임 아님"
        @click="sendData({homeroom_teacher_flag: 0})" />
    </div>
>>>>>>> 086e088 (Feat : 회원정보 수정, 비밀번호 변경 페이지 구현 완료)
    
>>>>>>> fa227ef (Feat & Fix : 과제 생성/수정 기능 완료, 나머지 기능 진행 중, 회원 관리 부분 컴포넌트화 및 버그 수정 중)
=======
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
    <!-- 학년/반 (학생) -->
    <div v-if="!isTeacher || homeroom.computedType">
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
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
      />
>>>>>>> e6b54fb (asdu)
=======
      />
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
    </div>
  </div>
</template>

<script>
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
import {ref} from '@vue/reactivity'
import {useStore} from 'vuex'
import {watch} from 'vue'
>>>>>>> e6b54fb (asdu)
=======
import {ref} from '@vue/reactivity'
import {useStore} from 'vuex'
import {watch} from 'vue'
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
=======
import {useStore} from 'vuex'
import {computed, ref, watch, reactive} from 'vue'
>>>>>>> 086e088 (Feat : 회원정보 수정, 비밀번호 변경 페이지 구현 완료)
export default {
  name: 'TeacherOrStudent',
  props: {
    userType: String,
    data: Object,
    type: String,
    homeroomFlag: Number,
  },
<<<<<<< HEAD
  setup() {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e6b54fb (asdu)
=======
  setup(props) {
>>>>>>> 086e088 (Feat : 회원정보 수정, 비밀번호 변경 페이지 구현 완료)
    const store = useStore()
    const subjectOptions = store.getters.getSubject
    const isTeacher = computed(() => props.userType === 'teacher')
    const changeType = computed(() => props.type === 'change')
    let subject = ref(props.data?.subject || '')
    let grade = ref(props.data?.grade || '')
    let classField = ref(props.data?.classField || '')
    let homeroom = reactive({
      type: changeType.value? props.homeroomFlag: null,
      computedType: computed(() => homeroom.type)
    })
    watch(subject, () => {
      sendData({subject:subject.value})
    })
    watch(grade, () => {
      sendData({grade:grade.value})
    })
    const sendData = (data) => {
      if (changeType.value) {
        store.dispatch('changeInfo', data)
      } else {
        store.dispatch('changeData', data)
      }
    }
    return {
      subjectOptions,
      sendData,
      isTeacher,
      homeroom,
      changeType,
      subject,
      grade,
      classField
<<<<<<< HEAD
=======
=======
    const store = useStore()
>>>>>>> 89ccfeb ( Feat: 회원 가입 기능 완료 (백 통신해서 디버깅 해야 함))
=======
    const store = useStore()
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
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
<<<<<<< HEAD
      userData
>>>>>>> 147871f (Feat : 회원가입 틀 제작 후 이름까지 완료 (그 이후 부분은 미완성))
=======
=======
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
      sendData,
      subject,
      grade,
      classField
<<<<<<< HEAD
>>>>>>> 89ccfeb ( Feat: 회원 가입 기능 완료 (백 통신해서 디버깅 해야 함))
=======
>>>>>>> e6b54fb (asdu)
=======
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
    }
  }
}
</script>