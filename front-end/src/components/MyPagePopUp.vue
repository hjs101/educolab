<template>
  <q-dialog persistant v-model="confirm.prompt" no-esc-dismiss>
    <q-card style="min-width: 500px">
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
      <!-- 칭호 -->
      <q-card-section v-else-if="type">
        <q-btn
        flat
        v-for="title in titles"
        :key="title.id"
        :text-color="title?.id === alias.computedId? 'blue':'black'"
        @click="selectAlias(0,title.id, title.title)">
          {{title.title}}
        </q-btn>
      </q-card-section>
      <!-- 배지 -->
      <q-card-section v-else class="row justify-evenly align-center">
        <q-card
          v-for="icon in icons"
          :key="icon.id"
          @click="selectAlias(1,icon.id, icon.title, icon.icon)"
          class="cursor-pointer q-mb-lg">
          <q-card-section class="justify-center row">
            <img :src="url+icon.icon" style="width:50px; height:50px" class="col-12">
            <br>
            <q-btn flat :text-color="icon?.id === alias.computedId? 'blue':'black'" class="col-12">
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
    reload: Boolean
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
      url: null,
      computedId: computed(() => badge.id),
    })
    const selectAlias = (option, id, name, url) => {
      if (option === 0) {
        alias.id = id
        alias.name = name
      } else {
        badge.id = id
        badge.name = name
        badge.url = url
      }
    }
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
        })
      } else {
        if (props.type) {
          emit('reverse', true, props.type, alias.id, alias.name)
        } else {
          emit('reverse', true, props.type,badge.id, badge.name, badge.url)
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