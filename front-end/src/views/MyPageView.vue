<template>
<<<<<<< HEAD
  <div
    v-if="data.computedMy"
    oncontextmenu="return false"
    onselectstart="return false">
<<<<<<< HEAD
    <h1>{{userType}} 마이 페이지</h1>
    <h3> 안녕하세요 {{data.my.userinfo.name}}님</h3>
=======
  <div v-if="data.computedMy" class="baseStyle">
    <h3>{{userType}} 마이 페이지</h3>
    <h5> 안녕하세요 {{data.my.userinfo.name}}님</h5>
>>>>>>> 0a91d41 (Feat : 비밀번호 확인, 회원정보 변경 기능 구현 완료, 약간의 스타일 적용)
=======
    <h4 class="text-center">마이페이지</h4>
    <hr>
    <h5 class="text-center"> 안녕하세요 {{data.my.userinfo.name}}님</h5>
>>>>>>> db26c2a (Style & Fix : 스타일 및 오류 수정)
    <my-info :info="data.my.userinfo" :profilImg="data.my.userinfo.profil" />
    <point-list v-if="!isTeacher" :point="data.my.point_log"/>
    <grant-point v-else />
  </div>
</template>

<script>
import { computed, onBeforeMount, reactive} from 'vue'
import {useRoute, useRouter} from 'vue-router'
import {useStore} from 'vuex'
import axios from 'axios'
import drf from '@/api/drf.js'
import MyInfo from '@/components/MyInfo.vue'
import PointList from '@/components/PointList.vue'
import GrantPoint from '@/components/GrantPoint.vue'
export default {
  components: {
    MyInfo,
    PointList,
    GrantPoint,
    },
  name: 'MyPageView',
  setup() {
    const route = useRoute()
    const router = useRouter()
    const store = useStore()
    const {userType} = route.params
    const isTeacher = computed(() => userType === 'teacher')
    const data = reactive({
      my: null,
      computedMy: computed(() => data.my)
    })
    const pageMain = () => {
      axios({
        url: drf.myPage.main(),
        method: 'get',
        headers: store.getters.authHeader,
      })
      .then((res) => {
        data.my = res.data
        console.log(res.data)
        store.dispatch('changeInfo', res.data.userinfo)
      })
    }
    onBeforeMount(() => {
      if (!store.getters.isLoggedIn) {
      router.push('/educolab/login')
      } else {
        pageMain()
      }
    })
    return {
      userType,
      isTeacher,
      data
    }
  },
}
</script>