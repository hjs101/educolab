<template>
  <q-dialog persistant v-model="prompt">
    <q-card style="min-width: 350px">
      <q-card-section>
        <div class="text-h6">{{title}}</div>
      </q-card-section>

      <q-card-section v-if="changeMode">
        <div class="text-h6 center">비밀번호 입력이 필요합니다</div>
        <q-input label="password"/>
      </q-card-section >
      
      <q-card-section v-else>
        <q-card v-for="item in items" :key="item.id" @click="selectAlias(item.id, item.title)">
          <q-card-section>
            <!-- 이미지 -->
            <!-- 칭호명 -->
            <p>{{item.title}}</p>
          </q-card-section>
        </q-card>
      </q-card-section>
      
      <q-card-actions align="center">
        <q-btn color="primary"
          :label="changeMode?'확인': '적용'"
          @click="move"
          v-close-popup/>
        <q-btn color="primary" label="취소" flat @click="doNothing" v-close-popup/>
      </q-card-actions>
    </q-card>
  </q-dialog>
</template>

<script>
import { reactive, ref } from '@vue/reactivity'
import { useRouter} from 'vue-router'
export default {
  name: 'PasswordInput',
  props: {
    title: String,
    path: String,
    changeMode: Boolean,
    items: Array,
  },
  setup(props, {emit}) {
    const router = useRouter()
    let prompt = ref(true)
    const doNothing = () => {
      prompt = false
      emit('reverse', false)
    }
    const alias = reactive({
      name: null,
      id: null,
    })
    const selectAlias = (id, name) => {
      alias.id = id
      alias.name = name
    }
    const move = () => {
      // 비밀번호 맞는지 확인 필요
      if (props.changeMode) {
        router.push(props.path)
        router.go(1)
      } else {
        emit('reverse', true, alias.id, alias.name)
      }
      prompt = false
    }
    return {
      move,
      prompt,
      alias,
      selectAlias,
      doNothing
    }
  }
}
</script>