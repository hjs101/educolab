<template>
  <q-card class="q-pa-md">
    <h5 class="text-center">내 정보</h5>
    <q-card-section horizontal>
      <!-- 프로필 -->
      <label for="profil">
        <img
          :src="profil.change"
          class="cursor-pointer"
          width="100">
      </label>
      <input
        type="file"
        class="hidden"
        id="profil"
        @input="changeProfil"
        accept="image/gif, image/jpeg, image/png"
      />
      <!-- 배지-->
      <div v-if="!info.userflag">
        <q-icon
          v-if="!info.wear_icon"
          name="mdi-plus-circle-outline"
          size="50px"
          color="grey-13"
          @click="myTitle(false)"
          class="cursor-pointer"
        />
        <img
          v-else
          :src="profil.change"
          class="cursor-pointer"
          width="50">
      </div>
      <q-card-section>
        아이디 {{info.username}} | 생년월일 {{birthday}}
        <br>
        학교 {{school}}
        <span v-if="!info.userflag || info.homeroom_teacher_flag">
          {{info.grade}}학년  {{info.class_field}}반 |
        </span>
        <span v-if="!info.userflag">
          <q-btn color="black" class="text-bold" flat @click="myTitle(true)">
            {{computedTitle}}
          </q-btn>
          | 현재(누적) 상점/벌점 +{{info.plus_point}} ({{info.acc_point}}) / {{info.minus_point}}
        </span>
        <br>
        이메일과 전화번호는 데이터 값에 포함되지만 출력하지 않음
      </q-card-section>
    </q-card-section>

    <q-separator />

    <q-card-actions>
      <q-btn flat @click="deleteProfil">프로필 삭제</q-btn>
      <q-btn color="primary" flat @click="toChangePage('info')">
        정보 수정
      </q-btn>
      <q-btn color="primary" flat @click="toChangePage('password')">
        비밀번호 변경
      </q-btn>
    </q-card-actions>
    <!-- 업적/칭호 적용 창 -->
    <my-page-pop-up
      v-if="apply.mode && !info.userflag"
      :title="apply.title"
      :changeMode="false"
      :type="type"
      :titles="info.own_title"
      :icons="info.own_icon"
      @reverse="applyTitle"
    />
  </q-card>
</template>

<script>
import {useStore} from 'vuex'
import { computed, reactive, ref } from 'vue'
import {useRouter} from 'vue-router'
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
    const router = useRouter()
    const school = store.getters.currentUser.schoolname
    let title = ref(props.info.wear_title?.title)
    let icon = ref(props.info.wear_icon?.title)
    let computedTitle = computed(() => title.value)
    const date = dayjs(props.info.birthday)
    const birthday = `${date.get('y')}년 ${date.get('M')+1}월 ${date.get('D')}일생`
    const profil = reactive({
      path: props.info.profil,
      change: computed(() => drf.file.path() + profil.path)
    })
    const badge = reactive({
      path: props.info.wear_icon,
      change: computed(() => drf.file.path() + badge.path)
    })
    let files = null
    const apply = reactive({
      prompt: false,
      title: null,
      mode: computed(() => apply.prompt),
    })
    let type = ref(null)
    const myTitle = (title) => {
      type.value = title
      apply.title = title? '보유 업적 목록': '보유 배지 목록'
      apply.prompt = true
    }
    const applyTitle = (val, type, pk, name) => {
      console.log(val, type, pk, name)
      if (val && name !== title.value ) {
        let url = null
        if (type.value) {
          url = drf.myPage.changeTitle()
        } else {
          url = drf.myPage.changeIcon()
        }
        console.log(url)
        axios({
          url,
          method: 'put',
          headers: store.getters.authHeader,
          data: {pk,}
        })
          .then((res) => {
            if (props.type) {
              title.value = name
            } else {
              icon.value = name
            }
          })
      }
      apply.prompt = false
    }
    const changeProfil = () => {
      // 자세한 건 수정 필요
      const photo = document.getElementById('profil')
      const form = new FormData()
      form.append('profil', photo.files[0])
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
          profil.path = drf.file.change() + photo.files[0].name
          console.log('적용되었습니다')
        })
    }
    const deleteProfil = () => {
      // 기본 프로필 이미지 주소
      axios({
        url: drf.myPage.changeProfil(),
        method: 'delete',
        headers: store.getters.authHeader,
      })
        .then(() => {
          // 프로필 적용
          profil.path = drf.file.default()
          console.log(profil.path)
          console.log('적용되었습니다')
        })
    }
    const toChangePage = (path) => {
      if (path === 'password') {
        store.dispatch('changePwInfo', {name: props.info.name, email: props.info.email, username: props.info.username})
        router.push('/change/password')
      } else {
        store.dispatch('changeInfo', props.info)
        router.push('/change/info')
      }
    }
    return {
      school,
      apply,
      title,
      icon,
      type,
      birthday,
      files,
      profil,
      badge,
      myTitle,
      applyTitle,
      changeProfil,
      deleteProfil,
      toChangePage,
      computedTitle
    }
  },
}
</script>