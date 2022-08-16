<template>
  <q-form class="q-py-lg" 
    @submit="grantPoint"
    @reset="initForm"
    >
    <q-card  class="q-pa-xl">
      <q-card-section>
        <div class="text-h6 text-center">상/벌점</div>
      </q-card-section>
      <q-card-section>
        <q-form
          @submit="searchStudent"
          class="row q-ma-lg justify-between align-center"
          >
          <span class="text-size q-mr-sm q-py-lg">학생명</span>
          <q-input
            class="col-8 q-mr-lg"
            v-model="searchKey"
            lazy-rules
            :rules="[ val => val && val.length > 0 || '학생명을 입력해주세요',
            val => val.length >= 2 || '정확한 검색을 위해 두 글자 이상 입력해주세요']"
          />
          <q-btn class="col-2 text-size" color="primary" type="submit">학생 검색</q-btn>
          <div v-if="students.result">
            <q-btn
              flat
              class="q-my-sm text-size q-mx-lg"
              v-for="student in students.list"
              :key="student.username"
              :text-color="students.selected === student.username? 'blue':'black'"
              @click="grant.student = student.username">
              {{student.name}} ({{student.grade}}학년 {{student.class_field}}반)
            </q-btn>
          </div>
        </q-form>
          <div class="q-ma-lg">
            <span class="q-py-lg q-mr-lg text-size" style="width:70px; text-align:center">유형</span>
            <q-radio
              class="q-mr-lg text-size"
              dense
              v-model="grant.pointflag"
              :val="true">
            상점
            </q-radio>
            <q-radio
              class="text-size"
              dense
              v-model="grant.pointflag"
              :val="false">
            벌점
            </q-radio>
          </div>
          <div class="row q-ma-lg">
            <span class="q-py-lg q-mr-lg text-size">점수</span>
            <q-input
              v-model="grant.log.point"
              class="col-8"
              type="number"
              :min="limit.min"
              :max="limit.max"
              lazy-rules
              required
              :rules="[ val => val && val.length > 0 || '점수를 입력해주세요',
              () => limit.selectedType !== null || '유형을 선택해주세요',
              val => val >= limit.min && val <= limit.max || '적절하지 않은 값입니다']"
            />
          </div>
          <div class="row align-center q-mx-lg">
            <span class="q-py-lg q-mr-lg text-size">사유</span>
            <q-input
              class="col-8"
              v-model="grant.log.content"
              required
              lazy-rules
              :rules="[ val => val && val.length > 0 || '샤유를 입력해주세요']"
            />
          </div>
      </q-card-section>
      <q-card-actions class="row justify-center">
        <q-btn  class="q-my-lg text-size q-mx-lg" label="초기화" flat type="reset"/>
        <q-btn  class="q-my-lg text-size q-mx-lg" label="점수 부여" color="primary" type="submit"/>
      </q-card-actions>
    </q-card>
    <message-pop-up
      v-if="confirm.isTrue"
      :message="confirm.message"
      :reload="true"
      @reverse="confirm.prompt = false"
    />
  </q-form>
</template>

<script>
import {computed, ref, reactive} from 'vue'
import {useStore} from 'vuex'
import axios from 'axios'
import drf from '@/api/drf.js'
import MessagePopUp from './MessagePopUp.vue'
export default {
  components: { MessagePopUp },
  name: 'GrantPoint',
  setup() {
    const store = useStore()
    const grant = reactive({
      student: null,
      pointflag: null,
      log: {
        point: null,
        content: null
      }
    })
    const limit = reactive({
      min : computed(() => grant.pointflag? 1 : -10),
      max : computed(() => grant.pointflag? 10 : -1),
      selectedType: computed(() => grant.pointflag)
    })
    const students = reactive({
      list: null,
      result: computed(() => students.list),
      selected: computed(() => grant.student)
    })
    const confirm = reactive({
      prompt: false,
      message: null,
      isTrue: computed(() => confirm.prompt)  
    })
    let searchKey = ref(null)
    const searchStudent = () => {
      if (searchKey.value.length >= 2 ) {
        axios({
          url: drf.myPage.point(),
          method: 'get',
          headers: store.getters.authHeader,
          params: {
            search_key: searchKey.value,
          }
        })
        .then((res) => {
          students.list = res.data
        })
      }
    }
    const initForm = () => {
      students.list = null
      searchKey.value = null
      grant.student = null
      grant.pointflag = null
      grant.log.point = null
      grant.log.content = null
    }
    const grantPoint = () => {
      if (grant.log.point > limit.max || grant.log.point < limit.min) {
        confirm.message = '적절한 점수가 아닙니다'
        confirm.prompt = true
      } else if (grant.student && grant.pointflag !== null && grant.log.point && grant.log.content)  {
        grant.log.point = grant.log.point * 1
        axios({
            url: drf.myPage.point(),
            method: 'put',
            headers: store.getters.authHeader,
            data: grant,
        })
        .then(() => {
          confirm.message = '적용되었습니다'
          initForm()
        })
        .catch(() => {
          confirm.message = '오류가 발생했습니다'
        })
        .finally(() => {
          confirm.prompt = true
        })
      } else {
        confirm.message = '빈 항목이 있습니다'
        confirm.prompt = true
      }
    }
    return {
      limit,
      grant,
      students,
      confirm,
      searchKey,
      searchStudent,
      grantPoint,
      initForm
    }
  },
}
</script>


<style scoped>
  p {
    margin: 0;
  }
  .text-size {
    font-size: 1rem;
  }
</style>