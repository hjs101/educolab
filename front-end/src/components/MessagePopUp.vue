<template>
<<<<<<< HEAD
  <q-dialog persistant v-model="prompt">
<<<<<<< HEAD
=======
  <q-dialog persistant v-model="popUp.flag">
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
      <q-card style="min-width: 350px">
        <q-card-section v-if="title">
          <div class="text-h6">{{title}}</div>
        </q-card-section>
        <q-card-section>
          <div class="text-h6 center">{{message}}</div>
        </q-card-section >
        <q-card-actions align="center">
<<<<<<< HEAD
          <q-btn color="primary" v-if="!button" label="확인" @click="move" v-close-popup/>
          <button-group v-else :currentUrl="currentUrl"/>
          <q-btn color="primary" v-if="cancel" label="취소" @click="doNothing" v-close-popup/>
=======
          <q-btn color="primary" label="확인" @click="move" v-close-popup/>
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
        </q-card-actions>
      </q-card>
    </q-dialog>
=======
    <q-card style="min-width: 350px">
      <q-card-section v-if="title">
        <div class="text-h6">{{title}}</div>
      </q-card-section>
      <q-card-section>
        <div class="text-h6 center">{{message}}</div>
      </q-card-section >
      <q-card-actions align="center">
        <q-btn color="primary" v-if="!button" label="확인" @click="move" v-close-popup/>
        <button-group v-else :currentUrl="currentUrl"/>
        <q-btn color="primary" flat v-if="cancel" label="취소" @click="doNothing" v-close-popup/>
      </q-card-actions>
    </q-card>
  </q-dialog>
>>>>>>> f7e1d76 (Feat : 학생 마이페이지 구현 완료 & 프로필/뱃지/칭호 변경 및 상벌점 부여 기능 진행 중)
</template>

<script>
<<<<<<< HEAD
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
        // 새로고침
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
=======
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
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
    }
  }
}
</script>