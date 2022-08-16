<template>
  <q-dialog persistant v-model="confirm.prompt">
    <q-card style="min-width: 350px">
      <q-card-section>
        <div class="text-h6">{{title}}</div>
      </q-card-section>

      <q-card-section v-if="changeMode">
        <div :class="{red: confirm.computedMatch}">{{confirm.computedMessage}}</div>
        <q-input
          clearable
          label="비밀번호"
          type="password"
          v-model="confirm.password"/>
      </q-card-section >
      <!-- 칭호 테스트 완료 -->
      <q-card-section v-else-if="type">
        <q-btn
        flat
        v-for="title in titles"
        :key="title.id"
        :text-color="title?.id === alias.computedId? 'blue':'black'"
        @click="selectAlias(0,title.id, title.title)">
          <!-- 칭호명 -->
          {{title.title}}
        </q-btn>
      </q-card-section>
      <!-- 배지 -->
      <q-card-section v-else>
        <q-card
          v-for="icon in icons"
          :key="icon.id"
          @click="selectAlias(1,icon.id, icon.title)"
          class="cursor-pointer">
          <q-card-section>
            <img :src="url+icon.icon" width="50px" >
            <br>
            <q-btn flat :text-color="icon?.id === alias.computedId? 'blue':'black'">
              {{icon.title}}
            </q-btn>
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
import {useRouter} from 'vue-router'
import educolab from '@/assets/educolab.png'
import axios from 'axios'
import drf from '@/api/drf.js'
import { computed, reactive } from 'vue'
import { useStore } from 'vuex'
export default {
  name: 'PasswordInput',
  props: {
    title: String,
    path: String,
    changeMode: Boolean,
    titles: Array,
    icons: Array,
    type: Boolean,
  },
  setup(props, {emit}) {
    const router = useRouter()
    const store = useStore()
    const confirm = reactive({
      password: null,
      prompt: true,
      incorrect: false,
      computedMatch: computed(() => confirm.incorrect),
      computedMessage: computed(() => confirm.incorrect? '비밀번호가 틀렸습니다':'비밀번호 입력이 필요합니다')
    })
    const doNothing = () => {
      if (props.changeMode) {
        router.back()
        emit('reverse', true)
      } else {
        confirm.prompt = false
        emit('reverse', false)
      }
    }
    let url = drf.file.path()
    const alias = reactive({
      name: null,
      id: null,
      computedId: computed(() => alias.id)
    })
    const badge = reactive({
      name: null,
      id: null,
      computedId: computed(() => badge.id),
    })
    const selectAlias = (option, id, name) => {
      console.log('선택', option, id, name)
      if (option === 0) {
        alias.id = id
        alias.name = name
      } else {
        badge.id = id
        badge.name = name
      }
    }
    // const samples = [
    //   {id:2, title: '개미는 뚠뚠'},
    //   {id:3, title: '내가 바로 과제 마스터'},
    //   {id:4, title: '배고파'}
    // ]
    const move = () => {
      if (props.changeMode) {
        axios({
          url: drf.accounts.checkePw(),
          method: 'post',
          headers: store.getters.authHeader,
          data: {
            password: confirm.password
          }
        })
        .then((res) => {
          if (!res.data.success) {
            confirm.incorrect = true
            confirm.prompt = true
          } else {
            confirm.prompt = false
          }
            emit('reverse', false, res.data.success)
        })
        .catch(({response}) => {
          console.log(response)
          confirm.password = null
          confirm.prompt = true
          // 실패했음을 알림
          // password.message = response.data.message
        })
      } else {
        if (props.type) {
          emit('reverse', true, props.type, alias.id, alias.name)
        } else {
          emit('reverse', true, props.type,badge.id, badge.name)
        }
        confirm.prompt = false
      }
    }
    return {
      move,
      confirm,
      alias,
      selectAlias,
      doNothing,
      badge,
      educolab,
      url
    }
  }
}
</script>