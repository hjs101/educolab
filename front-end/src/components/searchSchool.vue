<template>
  <div>
    <q-input color="teal" label="학교" v-model="school.name" disable/>
    <q-btn label="학교 검색" color="primary" @click="prompt.prompt = true"/>
    <!-- 학교 검색 팝업 -->
    <q-dialog v-model="prompt.prompt" persistent>
      <q-card style="min-width: 350px">
        <q-card-section>
          <div class="text-h6">학교 검색</div>
        </q-card-section>

        <q-card-section class="q-pt-none">
          <q-input minlength="2" dense autofocus @keyup.enter="findSchool">
            <template v-slot:append>
              <q-icon name="mdi-magnify" />
            </template>
          </q-input>
            <div v-if="prompt.searchResults">
              <!-- v-for -->
              <q-scroll-area style="height: 500px; max-width: 700px;" class="col-6 offset-3">
                <q-card class="my-card" v-for="schoolInfo in school.list" :key="schoolInfo.schoolCode">
                  <q-card-section @click="selectSchool(schoolInfo.schoolname, schoolInfo.schoolCode)">
                    <b>{{schoolInfo.schoolname}}</b>
                    <br>
                    <span>{{schoolInfo.schoolAddress}}</span>
                  </q-card-section>
                </q-card>
              </q-scroll-area>

            </div>
        </q-card-section>

        <q-card-actions align="right" class="text-primary">
          <q-btn flat label="취소" @click="school.name = null" v-close-popup />
          <!-- 추가할 때는 emit 해주기 -->
          <q-btn label="추가" @click="applySchool" v-close-popup />
        </q-card-actions>
      </q-card>
    </q-dialog>
  </div>
</template>

<script>
import {reactive} from '@vue/reactivity'
import {computed} from 'vue'
import {useStore} from 'vuex'
import axios from 'axios'
import drf from '@/api/drf.js'
export default {
  name: 'searchSchool',
  setup() {
    const store = useStore()
    const prompt = reactive({
      prompt: false,
      search: false,
      searchResults: computed(() => prompt.search)
    })
    const school = reactive({
      code: null,
      name: null,
      selectedName: null,
      selectedCode: null,
      list: [],
    })
    const findSchool = (event) => {
      prompt.search = true
      axios.get(drf.accounts.schoolInfo(), {schoolname:event.target.value})
        .then((res) => school.list = res.data)
        .catch((err) => console.log(err))
      // 백에 입력 값 보내기
    }
    const selectSchool = (name, code) => {
      school.selectedName = name
      school.selectedCode = code
    }
    const applySchool = () => {
      school.name = school.selectedName
      school.code = school.selectedCode
      store.commit('changeStudentDate', {school:school.code})
    }
    return {
      prompt,
      school,
      findSchool,
      selectSchool,
      applySchool
    }
  },
}
</script>