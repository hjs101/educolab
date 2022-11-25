<template>
<<<<<<< HEAD
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
=======
  <div>
    <q-input color="teal" label="학교" v-model="school.name" @change="$emit(toSignup)" disable/>
    <q-btn label="학교 검색" color="primary" @click="prompt.prompt = true"/>
>>>>>>> 03de9fd (Feat: 회원가입 학교 검색, 이름, 전화번호, 생년월일, 학년/반/번호)
    
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

              <!-- 테스트용 -->
              <!-- <q-scroll-area style="height: 500px; max-width: 700px;" class="col-6 offset-3">
                <q-card class="my-card" v-for="schoolInfo in school.temp" :key="schoolInfo.id">
                  <q-card-section @click="selectSchool(schoolInfo.schoolname, schoolInfo.schoolCode)">
                    <span>{{schoolInfo.url}}</span>
                  </q-card-section>
                </q-card>
              </q-scroll-area> -->
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
import axios from 'axios'
// import {mdiMagnify} from '@quasar/extras/mdi-v6'
export default {
  name: 'searchSchool',
  setup(props, {emit}) {
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
      list: [{
        schoolname: '안녕중학교',
        schoolAddress: '광주광역시 이하 생략',
        schoolCode: 123
      },
      {
        schoolname: '정신이들어중학교',
        schoolAddress: '광주광역시 북구 이하 생략',
        schoolCode: 124
      },
      {
        schoolname: '정신이들어중학교',
        schoolAddress: '광주광역시 북구 이하 생략',
        schoolCode: 124
      },
      {
        schoolname: '정신이들어중학교',
        schoolAddress: '광주광역시 북구 이하 생략',
        schoolCode: 124
      },
      {
        schoolname: '정신이들어중학교',
        schoolAddress: '광주광역시 북구 이하 생략',
        schoolCode: 124
      },
      {
        schoolname: '정신이들어중학교',
        schoolAddress: '광주광역시 북구 이하 생략',
        schoolCode: 124
      },
      {
        schoolname: '정신이들어중학교',
        schoolAddress: '광주광역시 북구 이하 생략',
        schoolCode: 124
      },
      {
        schoolname: '정신이들어중학교',
        schoolAddress: '광주광역시 북구 이하 생략',
        schoolCode: 124
      },
      {
        schoolname: '정신이들어중학교',
        schoolAddress: '광주광역시 북구 이하 생략',
        schoolCode: 124
      },
      {
        schoolname: '정신이들어중학교',
        schoolAddress: '광주광역시 북구 이하 생략',
        schoolCode: 124
      },
      {
        schoolname: '정신이들어중학교',
        schoolAddress: '광주광역시 북구 이하 생략',
        schoolCode: 124
      },
      {
        schoolname: '정신이들어중학교',
        schoolAddress: '광주광역시 북구 이하 생략',
        schoolCode: 124
      },
      ],
      temp: [],
    })
    const findSchool = () => {
      prompt.search = true
      const url = "https://api.thecatapi.com/v1/images/search"
      // axios.post(URL+"", {schoolname:event.target.value})
      //   .then((res) => school.list = res.data)
      //   .catch((err) => console.log(err))
      axios.get(url)
        .then((res) => {
          school.temp = res.data
          console.log(school.temp)
          })
        .catch((err) => console.log(err))

      // 백에 입력 값 보내기
    }
<<<<<<< HEAD
>>>>>>> 147871f (Feat : 회원가입 틀 제작 후 이름까지 완료 (그 이후 부분은 미완성))
=======
    const selectSchool = (name, code) => {
      school.selectedName = name
      school.selectedCode = code
    }
    const applySchool = () => {
      school.name = school.selectedName
      school.code = school.selectedCode
    }
    const toSignup = () => {
      emit('to-signup', {school:school.code})
    }
>>>>>>> 03de9fd (Feat: 회원가입 학교 검색, 이름, 전화번호, 생년월일, 학년/반/번호)
    return {
      prompt,
      school,
      findSchool,
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
      applySchool,
      toSignup
>>>>>>> 03de9fd (Feat: 회원가입 학교 검색, 이름, 전화번호, 생년월일, 학년/반/번호)
    }
  },
}
</script>