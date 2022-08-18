<template>
  <q-input
    color="teal"
    label="이름"
    v-model="name"
    maxlength="20"
    style="ime-mode:active"
    @change="sendData"
    clearable
    :dense="false"
    lazy-rules
    :rules="[ val => val && val.length > 0 || '이름을 입력해주세요',
    val => val.length > 1 || '이름은 두 글자 이상이어야 합니다']"
  />
</template>

<script>
  import {ref} from '@vue/reactivity'
  import {useStore} from 'vuex'

  export default {
    name:'userName',
    setup() {
      const store = useStore()
      let name= ref('')
      const sendData = () => {
        store.dispatch('changeData', {name: name.value})
      }
      return {
        sendData,
        name
      }
    },
  }
</script>
