<template>
  <div>
    <!-- 과목 (교사) -->
    <q-select v-if="isTeacher"
      color="teal"
      v-model="subject"
      label="과목"
      :options="subjectOptions"
      :value="subject.value"
    />
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
      />
    </div>
  </div>
</template>

<script>
import {useStore} from 'vuex'
import {computed, ref, watch, reactive} from 'vue'
export default {
  name: 'TeacherOrStudent',
  props: {
    userType: String,
    data: Object,
    type: String,
    homeroomFlag: Number,
  },
  setup(props) {
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
    }
  }
}
</script>