<template>
<!-- 비밀번호 입력 전까지 뜨지 않게 -->
  <main class="q-mx">
    <h3>CHANGE {{type.title}}</h3>
    <!-- form 부분 -->
    <q-form
      v-if="correct.state"
      class="q-gutter row">
      <section class="input col-8 offset-2 col-md-3 offset-md-4">
        <!-- 회원정보 변경 -->
        <change-user-info v-if="type.isTypeInfo"/>
        <!-- 비밀번호 변경 -->
        <login-info v-if="!type.isTypeInfo" :changeMode="true"/>
        <!-- 비밀번호 입력 팝업 -->
      </section>
    </q-form>
    <my-page-pop-up
      v-if="change.mode"
      :title="change.title"
      :changeMode="true"
      @reverse="render"
    />
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
    const change = reactive({
      prompt: true,
      title: route.params.userData === 'info'?'회원정보 수정':'비밀번호 변경',
      mode: computed(() => change.prompt),
    })
    const correct = reactive({
      password: false,
      state: computed(() => correct.password)
    })
    const render = (res) => {
      if (res === false) {
        // 비밀번호 일치
        correct.password = true
      }
    }
    return {
      type,
      change,
      correct,
      render
    }
  },
}
</script>