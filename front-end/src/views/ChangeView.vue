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
        <article v-if="!type.isTypeInfo">
          <login-info :changeMode="true"/>
          <q-btn label="비밀번호 변경" color="amber" @click="changePw"/>
          <message-pop-up
            v-if="password.popUpFlag"
            :message="password.message"
            path="/"
            :reload="true"
            :success="password.success"
          />
        </article>
        <!-- 비밀번호 입력 팝업 -->
        <my-page-pop-up
          :title="change.title"
          :changeMode="true"
          @reverse="change.prompt = false"
        />
      </section>
    </q-form>
  </main>

</template>

<script>
import {reactive, computed, onBeforeMount} from 'vue'
import {useRoute, useRouter} from 'vue-router'
import {useStore} from 'vuex'
import axios from 'axios'
import drf from '@/api/drf.js'
import LoginInfo from '@/components/LoginInfo.vue'
import MyPagePopUp from '@/components/MyPagePopUp.vue'
import MessagePopUp from '@/components/MessagePopUp.vue'
import ChangeUserInfo from '@/components/ChangeUserInfo.vue'

export default {
  name: 'ChangeView',
  components: {
    LoginInfo,
    MessagePopUp,
    MyPagePopUp,
    ChangeUserInfo,
  },
  setup () {
    const route = useRoute()
    const router = useRouter()
    const store = useStore()
    const info = computed(() => store.getters.getInfo)
    const type = reactive({
      type: computed(() => route.params.userData),
      isTypeInfo: computed(() => type.type === 'info'),
      title : computed(() => type.isTypeInfo? 'INFO':'PW'),
    })
    const change = reactive({
      prompt: false,
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
    const password = reactive({
      one: null,
      two: null,
      message: null,
      success: false,
      prompt: false,
      popUpFlag:computed(() => password.prompt),
      samePassword: computed(() => password.one === password.two)
    })
    const changePw = () => {
      axios({
        url: drf.accounts.changePw(),
        method: 'post',
        data: {
          ...info,
          password1:password.one,
          password2:password.two
        }
      })
      .then(({data}) => {
        console.log(data)
        password.message = data.message
      })
      .catch(({response}) => {
        password.message = response.data.message
      })
      .finally(() => {
        password.prompt = true
      })
    }
    return {
      type,
      change,
      password,
      changePw
    }
  },
}
</script>