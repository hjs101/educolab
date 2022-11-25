<template>
  <q-dialog persistant v-model="prompt" no-esc-dismiss class="content-center">
    <q-card style="min-width: 350px">
      <q-card-section v-if="title">
        <div class="text-h6 text-center">{{title}}</div>
      </q-card-section>
      <q-card-section>
        <div class="text-h6 text-center">{{message}}</div>
      </q-card-section >
      <q-card-actions class="row justify-center align-center">
        <q-btn color="primary" v-if="!button" label="확인" @click="move" v-close-popup/>
        <button-group v-else :currentUrl="currentUrl"/>
        <q-btn color="primary" flat v-if="cancel" label="취소" @click="doNothing" v-close-popup/>
      </q-card-actions>
    </q-card>
  </q-dialog>
</template>

<script>
import { ref } from '@vue/reactivity'
import { useRouter, useRoute} from 'vue-router'
import ButtonGroup from '@/components/ButtonGroup.vue'
export default {
  name: 'MessagePopUp',
  components: {
    ButtonGroup,
  },
  props: {
    title: String,
    path: String,
    button: Boolean,
    message: String,
    cancel: Boolean,
    reload: Boolean,
  },
  setup(props, {emit}) {
    const router = useRouter()
    const route = useRoute()
    let currentUrl = route.params.info === 'id'? 'findId':'findPw'
    let prompt = ref(true)
    const doNothing = () => {
      prompt = false
      emit('reverse', false)
    }
    const move = () => {
      if (props.path) {
        router.push(props.path)
        if (props.reload) {
          router.go(1)
        }
      }
      prompt = false
      emit('reverse', true)
    }
    return {
      move,
      prompt,
      currentUrl,
      doNothing
    }
  }
}
</script>