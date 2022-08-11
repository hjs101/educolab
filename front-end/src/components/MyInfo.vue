<template>
  <q-card class="my-card">
    <h5 class="text-center">내 정보</h5>
    <q-card-section horizontal>
      <label for="profil">
        <q-icon
          v-if="!profil"
          name="mdi-account"
          size="100px"
          color="grey-13"
          class="cursor-pointer" />
        <q-img
          v-else
          :src="profil"
          size="100px"
          class="cursor-pointer"
        />
      </label>
      <input
        type="file"
        class="hidden"
        id="profil"
        @update:model-value="val => { files = val }"
        @input="changeProfil"/>
      <q-icon
        v-if="!info.userflag"
        name="mdi-plus-circle-outline"
        size="50px"
        color="grey-13"
        @click="myTitle('배지')"
        class="cursor-pointer" />
      <q-card-section>
        아이디 {{info.username}} | 생년월일 {{birthday}}
        <br>
        학교 {{school}}
        <span v-if="!info.userflag || info.homeroom_teacher_flag">
          {{info.grade}}학년  {{info.class_field}}반 |
        </span>
        <span v-if="!info.userflag">
          <q-btn color="black" class="text-bold" flat @click="myTitle('칭호')">
            {{info.wear_title.title}}
          </q-btn>
          | 상점/벌점 +{{info.plus_point}} ({{info.acc_point}}) /-{{info.minus_point}}
        </span>
        <br>
        이메일과 전화번호는 데이터 값에 포함되지만 출력하지 않음
      </q-card-section>
    </q-card-section>

    <q-separator />

    <q-card-actions>
      <q-btn color="primary" flat @click="confirmPassword('info')">
        정보 수정
      </q-btn>
      <q-btn color="primary" flat @click="confirmPassword('password')">
        비밀번호 변경
      </q-btn>
    </q-card-actions>
    <!-- 비밀번호 입력 창 -->
    <my-page-pop-up
      v-if="change.mode"
      :title="change.title"
      :path="change.path"
      :changeMode="true"
      @reverse="change.prompt = false"
    />
    <!-- 업적/칭호 적용 창 -->
    <my-page-pop-up
      v-if="apply.mode && !info.userflag"
      :title="title"
      :changeMode="false"
      :items="info.own_title"
      @reverse="applyTitle"
    />
  </q-card>
</template>

<script>
import {useStore} from 'vuex'
import { computed, reactive, ref } from 'vue'
import dayjs from 'dayjs'
import axios from 'axios'
import drf from '@/api/drf.js'
import MyPagePopUp from '@/components/MyPagePopUp.vue'
export default {
  name: 'MyInfo',
  components: {
    MyPagePopUp,
  },
  props: {
    info: Object,
  },
  setup(props) {
    const store = useStore()
    const school = store.getters.currentUser.schoolname
    let title = ref(props.info.wear_title?.title)
    const date = dayjs(props.info.birthday)
    const birthday = `${date.get('y')}년 ${date.get('M')+1}월 ${date.get('D')}일생`
    let profil = ref(props.info.profil)
    let files = null
    const change = reactive({
      prompt: false,
      title: null,
      path: null,
      mode: computed(() => change.prompt),
    })
    const apply = reactive({
      prompt: false,
      title: null,
      mode: computed(() => apply.prompt),
    })
    const confirmPassword = (path) => {
      change.path = '/change/' + path
      change.title = path === 'info'?'회원정보 수정':'비밀번호 변경'
      change.prompt = true
    }
    const myTitle = (title) => {
      apply.title = '보유 ' + title + ' 목록'
      apply.prompt = true
    }
    const applyTitle = (val, pk, name) => {
      if (val && name !== title.value ) {
        axios({
          url: drf.myPage.changeTitle(),
          method: 'put',
          headers: store.getters.authHeader,
          data: {pk,}
        })
          .then(() => {
            title.value = name
          })
      }
    }
    const changeProfil = (event) => {
      // 자세한 건 수정 필요
      let form = new FormData()
      form.append('files', event.target.value)
      axios({
        url: drf.myPage.changeProfil(),
        method: 'put',
        headers: {
          ...store.getters.authHeader,
          'Content-Type': 'multipart/form-data'
          },
        data: form
      })
        .then(() => {
          // 프로필 적용
        })
    }
    return {
      school,
      change,
      apply,
      title,
      birthday,
      files,
      profil,
      confirmPassword,
      myTitle,
      applyTitle,
      changeProfil
    }
  },
}
</script>