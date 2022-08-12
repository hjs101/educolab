<template>
  <q-dialog persistant v-model="prompt">
    <q-card style="min-width: 350px">
      <q-card-section>
        <div class="text-h6">{{title}}</div>
      </q-card-section>

      <q-card-section v-if="changeMode">
        <div class="text-h6 center">비밀번호 입력이 필요합니다</div>
        <q-input label="비밀번호"/>
      </q-card-section >
      <!-- 칭호 -->
      <q-card-section v-else-if="type">
        <q-card v-for="item in items" :key="item.id" @click="selectAlias(0,item.id, item.title)">
          <q-card-section :class="{active: item.id === alias.id}">
            <!-- 칭호명 -->
            <p>{{item.title}}</p>
          </q-card-section>
        </q-card>
      </q-card-section>
      <!-- 배지 -->
      <q-card-section v-else>
        <q-card v-for="item in items" :key="item.id" @click="selectAlias(1,item.id, item.title)">
          <q-card-section :class="{active: item.id === alias.id}">
            <!-- 이미지 -->
            <img :src="badge" >
            <!-- 배지명 -->
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
import badge from '@/assets/quiz.png'
export default {
  name: 'PasswordInput',
  props: {
    title: String,
    path: String,
    changeMode: Boolean,
    items: Array,
    type: Boolean,
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
      if (props.changeMode) {
        // 백에 데이터 보내 비밀번호 맞는지 확인 -> 맞으면 회원정보 수정 페이지로
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
      badge,
      selectAlias,
      doNothing
    }
  }
}
</script>