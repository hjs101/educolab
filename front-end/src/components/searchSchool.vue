<template>
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e6b54fb (asdu)
  <div>
    <q-input color="teal" label="학교" v-model="school.name" disable/>
    <q-btn label="학교 검색" color="primary" @click="prompt.prompt = true"/>
=======
  <div class="row justify-between">
    <q-input color="teal" label="학교" v-model="school.name" disable class="col-9"/>
    <q-btn label="학교 검색" color="teal" @click="prompt.prompt = true" class="col-2"/>
>>>>>>> bf45305 ( Fix : 버그 수정)
    <!-- 학교 검색 팝업 -->
    <q-dialog v-model="prompt.prompt" persistent>
      <q-card style="min-width: 350px">
        <q-card-section>
          <div class="text-h6 center">학교 검색</div>
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
      list: [],
=======
      list: [{
      //   code: 123,
      //   name: '아아아',
      //   address: '어쩌고',
      // },
      // {
      //   code: 124,
      //   name: '아아아',
      //   address: '어쩌고',
      // },
      // {
      //   code: 125,
      //   name: '아아아',
      //   address: '어쩌고',
      }],
>>>>>>> 6e582c6 (develop 브랜치 푸시)
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
=======
  <div>
    <q-input color="teal" label="학교" v-model="school.name" disable/>
    <q-btn label="학교 검색" color="primary" @click="prompt.prompt = true"/>
<<<<<<< HEAD
>>>>>>> 03de9fd (Feat: 회원가입 학교 검색, 이름, 전화번호, 생년월일, 학년/반/번호)
    
=======
    <!-- 학교 검색 팝업 -->
>>>>>>> bb316aa ( Feat : 회원가입 시 입력받은 정보를 취합하는 중)
    <q-dialog v-model="prompt.prompt" persistent>
      <q-card style="min-width: 350px">
        <q-card-section>
          <div class="text-h6">학교 검색</div>
=======
>>>>>>> 80ba160 ( Feat : 백과의 통신 (학교 검색과 회원가입은 미완료))
=======
>>>>>>> e6b54fb (asdu)
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
      searchResults: computed(() => school.list),
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
      axios.get(drf.accounts.schoolInfo(), 
      {params: {schoolname : event.target.value}})
        .then((res) => school.list = res.data)
        .catch((err) => console.log(err))
    }
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 147871f (Feat : 회원가입 틀 제작 후 이름까지 완료 (그 이후 부분은 미완성))
=======
=======

>>>>>>> 9d52baa ( Fix : 버그 수정 중)
=======

>>>>>>> e6b54fb (asdu)
    const selectSchool = (name, code) => {
      prompt.selected = code
      school.selectedName = name
      school.code = code
    }
    const applySchool = () => {
      school.name = school.selectedName
      store.dispatch('changeData', {school:school.code})
    }
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 03de9fd (Feat: 회원가입 학교 검색, 이름, 전화번호, 생년월일, 학년/반/번호)
=======

>>>>>>> 9d52baa ( Fix : 버그 수정 중)
=======

>>>>>>> e6b54fb (asdu)
    return {
      prompt,
      school,
      findSchool,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
      selectSchool,
      applySchool
=======
      schoolAddress,
      schoolName
>>>>>>> 147871f (Feat : 회원가입 틀 제작 후 이름까지 완료 (그 이후 부분은 미완성))
=======
      selectSchool,
<<<<<<< HEAD
      applySchool,
      toSignup
>>>>>>> 03de9fd (Feat: 회원가입 학교 검색, 이름, 전화번호, 생년월일, 학년/반/번호)
=======
      applySchool
>>>>>>> bb316aa ( Feat : 회원가입 시 입력받은 정보를 취합하는 중)
=======
      selectSchool,
      applySchool
>>>>>>> e6b54fb (asdu)
    }
  },
}
</script>