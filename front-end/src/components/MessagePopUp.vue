<template>
  <q-dialog persistent>
      <q-card style="min-width: 350px">
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
import {useRouter} from 'vue-router'
export default {
  name: 'MessagePopUp',
  props: {
    message: String,
    path: String,
    success: Boolean,
  },
  setup(props) {
    const router = useRouter()
    const move = () => {
      router.push(props.path)
    }
    return {
      move
    }
  }
}
</script>