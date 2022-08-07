<template>
  <main class="q-mx">
    <h3 v-if="type.type">FIND {{type.title}}</h3>
    <!-- form 부분 -->
    <q-form
      class="q-gutter row">
      <section class="input col-8 offset-2 col-md-3 offset-md-4">
      <!-- 여기에 이름, 이메일 입력 창 -->
        <article v-if="type.type">
          <find-id />
          <send-pw-email v-if="!type.isTypeId" />
        </article>
        <change-user-info />
      </section>
    </q-form>
    <!-- 여기에 회원가입 로그인 비밀번호 찾기 -->
    <button-group v-if="type.type" :currentUrl="type.currentUrl"/>
  </main>

</template>

<style scoped>
  .input {
    width: 500px;
  }
  .buttonGroup {
    margin-top: 100px;
  }
</style>

<script>
import { reactive } from '@vue/reactivity'
import {computed, onBeforeMount} from 'vue'
import {useRoute} from 'vue-router'
import ButtonGroup from '@/components/ButtonGroup.vue'
import SendPwEmail from '@/components/SendPwEmail.vue'
import FindId from '@/components/FindId.vue'
import ChangeUserInfo from '@/components/ChangeUserInfo.vue'

export default {
  name: 'FindView',
  components: {
    ButtonGroup,
    SendPwEmail,
    FindId,
    ChangeUserInfo,
  },
  setup () {
    const route = useRoute()
    // const router = useRouter()
    const type = reactive({
      type : computed(() => route.params.info),
      changeType: computed(() => route.params.userData),
      isTypeId: computed(() => type.type === 'id'),
      title : computed(() => type.isTypeId? 'ID':'PW'),
      currentUrl: computed(() => type.isTypeId? 'findId':'findPw'),
      })
    onBeforeMount (() => {
      console.log(type.type)
      console.log(type.changeType)
      // if (!type.isTypeId && type.type !== 'password' && !type.changeType) {
      //   router.push('/404')
      // }
    })
    return {
      type,
    }
  },
}
</script>