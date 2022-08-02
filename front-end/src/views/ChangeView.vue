<template>
  <div>
    <h3>CHANGE PASSWORD</h3>
    <q-form
      class="q-gutter row"
    >
      <div class="input col-8 offset-2 col-md-3 offset-md-4">
        <q-input
          color="teal"
          v-model="userInfo.name"
          label="새 비밀번호"
          lazy-rules
          :rules="[ val => val && val.length > 0 || '비밀번호를 입력해주세요']"
        />
        <q-input
        color="teal"
        v-model="userInfo.email"
        label="비밀번호 확인"
        lazy-rules
        :rules="[
          val => val !== null && val !== '' || '비밀번호를 입력해주세요',
        ]"
        />
      </div>
      <q-btn color="amber" label="CHANGE PW" v-if="type.isTypeId" class="col-8 offset-2 col-md-1 offset-md-1" @click="findId"/>
    </q-form>
  </div>
</template>

<script>
import {useStore} from 'vuex'
import {onBeforeMount} from 'vue'
import {useRouter} from 'vue-router'
export default {
  name: 'ChangeView',
  setup() {
    const store = useStore()
    const router = useRouter()
    onBeforeMount(() => {
      if (!store.getters.getPermission) {
        router.push('')
      }
    })
    return {

    }
  }
}
</script>