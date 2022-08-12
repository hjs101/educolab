<template>
  <q-card class="my-card">
    <h5 class="text-center">내 정보</h5>
    <q-card-section horizontal>
      <label for="profil">
        <!-- 프로필 이미지 있을 때 -->
        <img :src="profil" class="cursor-pointer size-100">
        <!-- <q-img
          :src="profil"
          size="100px"
          class="cursor-pointer"
        /> -->
      </label>
      <input
        type="file"
        class="hidden"
        id="profil"
        @update:model-value="val => { files = val }"
        @input="changeProfil"/>
      <!-- 배지가 없을 때만 뜸 -->
      <q-icon
        v-if="!info.userflag"
        name="mdi-plus-circle-outline"
        size="50px"
        color="grey-13"
        @click="myTitle(false)"
        class="cursor-pointer" />
      <!-- 배지가 있을 경우 -->
      <!-- <q-img

      /> -->
      <q-card-section>
        아이디 {{info.username}} | 생년월일 {{birthday}}
        <br>
        학교 {{school}}
        <span v-if="!info.userflag || info.homeroom_teacher_flag">
          {{info.grade}}학년  {{info.class_field}}반 |
        </span>
        <span v-if="!info.userflag">
          <q-btn color="black" class="text-bold" flat @click="myTitle(true)">
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
      <q-btn flat @click="deleteProfil">프로필 삭제</q-btn>
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
      :title="apply.title"
      :changeMode="false"
      :type="type"
      :items="info.own_title"
      @reverse="applyTitle"
    />
  </q-card>
</template>

<style scoped>
  .size-100 {
    width: 100px;
  }
</style>

<script>
import {useStore} from 'vuex'
import { computed, reactive, ref } from 'vue'
import dayjs from 'dayjs'
import axios from 'axios'
import drf from '@/api/drf.js'
import img from '@/assets/profile1.jpg'
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
    let profil = img
    // let profil = ref(drf.myPage.profil()+props.info.profil)
    let computedProfil = computed(() => profil.value)
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
    let type = ref(null)
    const myTitle = (title) => {
      type.value = title
      apply.title = title? '보유 업적 목록': '보유 배지 목록'
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
      apply.prompt = false
    }
    const changeProfil = () => {
      // 자세한 건 수정 필요
      let form = new FormData()
      form.append('files', [files])
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
    const deleteProfil = () => {
      // 기본 프로필 이미지 주소
      files = null
      // profil.value = drf.myPage.profil()+props.info.profil
    }
    return {
      school,
      change,
      apply,
      title,
      type,
      birthday,
      files,
      profil,
      computedProfil,
      confirmPassword,
      myTitle,
      applyTitle,
      changeProfil,
      deleteProfil
    }
  },
}
</script>