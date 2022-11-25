<template>
<<<<<<< HEAD
  <div>
    <q-input color="teal" label="학교" v-model="school.name" disable/>
    <q-btn label="학교 검색" color="primary" @click="prompt.prompt = true"/>
    <!-- 학교 검색 팝업 -->
    <q-dialog v-model="prompt.prompt" persistent>
      <q-card style="min-width: 350px">
        <q-card-section>
          <div class="text-h6 center">학교 검색</div>
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
                <q-card v-for="schoolInfo in school.list" :key="schoolInfo.code">
                  <q-card-section :class="{active: prompt.selected === schoolInfo.code}" @click="selectSchool(schoolInfo.name,schoolInfo.code)">
                    <b>{{schoolInfo.name}}</b>
                    <br>
                    <span>{{schoolInfo.address}}</span>
                  </q-card-section>
                </q-card>
              </q-scroll-area>

            </div>
        </q-card-section>

        <q-card-actions align="right" class="text-primary" v-if="prompt.search">
          <q-btn flat label="취소" @click="school.name = null" v-close-popup />
          <q-btn label="추가" @click="applySchool" v-close-popup />
        </q-card-actions>
      </q-card>
    </q-dialog>
  </div>
</template>

<style>
  .active {
    color: blue;
    font-weight: bold;
  }
</style>

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
      selected: null,
      searchResults: computed(() => prompt.search),
      // isSelected: computed(() => prompt.selected === code)
    })
    const school = reactive({
      name: null,
      code: null,
      selectedName: null,
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
      prompt.selected = code
      school.selectedName = name
      school.code = code
    }
    const applySchool = () => {
      school.name = school.selectedName
      store.dispatch('changeData', {school:school.code})
    }
=======
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
>>>>>>> 147871f (Feat : 회원가입 틀 제작 후 이름까지 완료 (그 이후 부분은 미완성))
    return {
      prompt,
      school,
      findSchool,
<<<<<<< HEAD
      selectSchool,
      applySchool
=======
      schoolAddress,
      schoolName
>>>>>>> 147871f (Feat : 회원가입 틀 제작 후 이름까지 완료 (그 이후 부분은 미완성))
    }
  },
}
</script>