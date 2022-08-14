<template>
  <main class="q-mx">
    <h3>CHANGE {{type.title}}</h3>
    <!-- form 부분 -->
    <q-form
      class="q-gutter row">
      <section class="input col-8 offset-2 col-md-3 offset-md-4">
        <!-- 회원정보 변경 -->
        <change-user-info v-if="type.isTypeInfo"/>
        <!-- 비밀번호 변경 -->
        <login-info v-if="!type.isTypeInfo" :changeMode="true"/>
        <!-- 비밀번호 입력 팝업 -->
        <my-page-pop-up
          v-if="change.mode"
          :title="change.title"
          :changeMode="true"
        />
      </section>
    </q-form>
  </main>

</template>

<script>
import {reactive, computed, onBeforeMount} from 'vue'
import {useRoute, useRouter} from 'vue-router'
import {useStore} from 'vuex'
import LoginInfo from '@/components/LoginInfo.vue'
import MyPagePopUp from '@/components/MyPagePopUp.vue'
import ChangeUserInfo from '@/components/ChangeUserInfo.vue'

export default {
  name: 'ChangeView',
  components: {
    LoginInfo,
    MyPagePopUp,
    ChangeUserInfo,
  },
  setup () {
    const route = useRoute()
    const router = useRouter()
    const store = useStore()
    const type = reactive({
      type: computed(() => route.params.userData),
      isTypeInfo: computed(() => type.type === 'info'),
      title : computed(() => type.isTypeInfo? 'INFO':'PW'),
    })
    const change = reactive({
      prompt: true,
      title: route.params.userData === 'info'?'회원정보 수정':'비밀번호 변경',
      mode: computed(() => change.prompt),
    })
    onBeforeMount (() => {
      if (!type.isTypeInfo){
        if (type.type !== 'password') {
          router.push('/404')
        }
      } else if (store.getters.isLoggedIn) {
          // 로그인됐을 경우
      } else {
        // 로그인되지 않았을 경우
      }
    })
    return {
      type,
      change,
    }
  },
}
</script>