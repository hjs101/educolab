<template>
  <div class="row justify-between">
    <q-input color="teal" label="학교" v-model="school.name" disable class="col-9"/>
    <q-btn label="학교 검색" color="teal" @click="prompt.prompt = true" />
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
          <q-btn flat label="취소" v-close-popup />
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
  props: {
    schoolname: String,
    type: String,
  },
  setup(props) {
    const store = useStore()
    const prompt = reactive({
      prompt: false,
      search: false,
      selected: null,
      searchResults: computed(() => prompt.search),
    })
    const school = reactive({
      name: props?.schoolname || null,
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

    const selectSchool = (name, code) => {
      prompt.selected = code
      school.selectedName = name
      school.code = code
    }
    const applySchool = () => {
      school.name = school.selectedName
      if (props.type !== 'change') {
        store.dispatch('changeData', {school:school.code})
      } else  {
        store.dispatch('changeInfo', {school:school.code})
      }
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