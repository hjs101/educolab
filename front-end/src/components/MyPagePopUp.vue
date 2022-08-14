<template>
  <q-dialog persistant v-model="confirm.prompt">
    <q-card style="min-width: 350px">
      <q-card-section>
        <div class="text-h6">{{title}}</div>
      </q-card-section>

      <q-card-section v-if="changeMode">
        <div class="text-h6 center">비밀번호 입력이 필요합니다</div>
        <q-input label="비밀번호" v-model="confirm.password"/>
      </q-card-section >
      <!-- 칭호 테스트 중-->
      <q-card-section v-else-if="type">
        <q-btn
        flat
        v-for="sample in samples"
        :key="sample.id"
        :text-color="sample.id === alias.computedId? 'blue':'black'"
        @click="selectAlias(0,sample.id, sample.title)">
          <!-- 칭호명 -->
          {{sample.title}}
        </q-btn>
      </q-card-section>
      <!-- 칭호  -->
      <!-- <q-card-section v-else-if="type">
        <q-card v-for="item in items" :key="item.id" @click="selectAlias(0,item.id, item.title)">
          <q-card-section :class="{active: item.id === alias.id}">
            <p>{{item.title}}</p>
          </q-card-section>
        </q-card>
      </q-card-section> -->
      <!-- 배지 -->
      <q-card-section v-else>
        <q-card v-for="item in items" :key="item.id" @click="selectAlias(1,item.id, item.title)">
          <q-card-section :text-color="sample.id === alias.computedId? 'blue':'black'">
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
import { reactive} from '@vue/reactivity'
import badge from '@/assets/quiz.png'
import { computed } from '@vue/runtime-core'
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
    const confirm = reactive({
      password: null,
      prompt: true
    })
    const doNothing = () => {
      confirm.prompt = false
      emit('reverse', false)
    }
    const alias = reactive({
      name: null,
      id: null,
      computedId: computed(() => alias.id)
    })
    // 여기에 뱃지
    const selectAlias = (option, id, name) => {
      console.log('선택', option, id, name)
      if (option === 0) {
        alias.id = id
        alias.name = name
      }
    }
    const samples = [
      {id:2, title: '개미는 뚠뚠'},
      {id:3, title: '내가 바로 과제 마스터'},
      {id:4, title: '배고파'}
    ]
    const move = () => {
      if (props.changeMode) {
        // 비밀번호 확인 (url, 데이터)
        // axios({
        // url: drf.accounts.changePw(),
        // method: 'post',
        // data: {
        //   password: confirm.password
        //   }
        // })
        // .then(({data}) => {
        //   // 성공했음을 알리는 팝업
        //   console.log(data)
        //   password.message = data.message
        //   emit('reverse', false)
        // })
        // .catch(({response}) => {
        //   // 실패했음을 알림
        //   // password.message = response.data.message
        // })
        // .finally(() => {
        //   // password.prompt = true
        // })
        emit('reverse', false)
      } else {
        emit('reverse', true, alias.id, alias.name)
      }
      confirm.prompt = false
    }
    return {
      move,
      confirm,
      alias,
      badge,
      selectAlias,
      doNothing,
      samples
    }
  }
}
</script>