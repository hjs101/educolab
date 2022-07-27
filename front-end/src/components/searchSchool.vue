<template>
  <Fragment>
    <q-input color="teal" label="학교" disable/>
    <q-btn label="학교 검색" color="primary" @click="prompt = true" />
    
    <q-dialog v-model="prompt" persistent>
      <q-card style="min-width: 350px">
        <q-card-section>
          <div class="text-h6">학교 검색</div>
        </q-card-section>

        <q-card-section class="q-pt-none">
          <q-input dense v-model="address" autofocus @keyup.enter="prompt = false" />
          <q-btn label="검색" color="primary" @click="findSchool" />
              <div>
                <!-- v-for -->
                <q-card class="my-card">
                  <q-card-section>
                    <b>학교 이름</b>
                    <br>
                    <span>학교 주소</span>
                  </q-card-section>
                </q-card>
              </div>
        </q-card-section>

        <q-card-actions align="right" class="text-primary">
          <q-btn flat label="취소" v-close-popup />
          <!-- 추가할 때는 emit 해주기 -->
          <q-btn flat label="추가" v-close-popup />
        </q-card-actions>
      </q-card>
    </q-dialog>
  </Fragment>
</template>

<script>
import {ref} from '@vue/reactivity'
export default {
  name: 'searchSchool',
  setup() {
    let prompt = ref(false)
    let school = ref(0)
    let schoolAddress = ref('')
    let schoolName = ref('')
    const findSchool = () => {
      // 백에 입력 값 보내기
    }
    return {
      prompt,
      school,
      findSchool,
      schoolAddress,
      schoolName
    }
  },
}
</script>