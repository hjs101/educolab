<template>
  <q-dialog persistant v-model="popUp.flag">
      <q-card style="min-width: 350px">
        <q-card-section v-if="title">
          <div class="text-h6">{{title}}</div>
        </q-card-section>
        <q-card-section>
          <div class="text-h6 center">{{message}}</div>
        </q-card-section >
        <q-card-actions align="center">
          <q-btn color="primary" label="확인" @click="move" v-close-popup/>
        </q-card-actions>
      </q-card>
    </q-dialog>
</template>

<script>
import { reactive } from '@vue/reactivity'
import { useRouter} from 'vue-router'
import { computed } from 'vue'
export default {
  name: 'MessagePopUp',
  props: {
    title: String,
    path: String,
    success: Boolean,
    message: String,
  },
  setup(props) {
    const router = useRouter()
    const popUp = reactive({
      prompt: true,
      flag: computed(() => popUp.prompt)
    })
    const move = () => {
      if (props.success && props.path) {
        router.push(props.path)
      }
      popUp.prompt = false
    }
    return {
      move,
      popUp,
    }
  }
}
</script>