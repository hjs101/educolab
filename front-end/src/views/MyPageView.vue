<template>
  <div
    v-if="data.computedMy"
    oncontextmenu="return false"
    onselectstart="return false">
    <h1>{{userType}} 마이 페이지</h1>
    <h3> 안녕하세요 {{data.my.userinfo.name}}님</h3>
    <my-info :info="data.my.userinfo" :profilImg="data.my.userinfo.profil" />
    <point-list v-if="!isTeacher" :point="data.my.point_log"/>
    <grant-point v-else />
  </div>
</template>

<script>
import { computed, onBeforeMount, reactive} from 'vue'
import {useRoute} from 'vue-router'
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
        store.dispatch('changeInfo', res.data.userinfo)
      })
    }
    onBeforeMount(() => {
      pageMain()
    })
    return {
      userType,
      isTeacher,
      data
    }
  },
}
</script>