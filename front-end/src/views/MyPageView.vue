<template>
  <div>
    <h1>{{userType}} 마이 페이지</h1>
    <my-info v-if="data" :info="data.userinfo" />
    <point-list v-if="data" :point="data.point_log"/>
  </div>
</template>

<script>
import { computed, onBeforeMount, ref } from 'vue'
import {useRoute} from 'vue-router'
import {useStore} from 'vuex'
import axios from 'axios'
import drf from '@/api/drf.js'
import MyInfo from '@/components/MyInfo.vue'
import PointList from '../components/PointList.vue'
export default {
  components: {
    MyInfo,
    PointList,
    },
  name: 'MyPageView',
  setup() {
    const route = useRoute()
    const store = useStore()
    const {userType} = route.params
    const isTeacher = computed(() => userType === 'teacher')
    let data = ref(null)
    const pageMain = () => {
      axios({
        url: drf.myPage.main(),
        method: 'get',
        headers: store.getters.authHeader,
      })
      .then((res) => {
        data.value = res.data
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