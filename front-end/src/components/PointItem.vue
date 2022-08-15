<template>
  <q-card>
    <q-card-section>
      {{item.id}}
      <img v-if="icon" :src="img">
      <br>
      이름 {{item.title}}
      <br>
      설명 {{item.content}}
      <br>
      가격 {{item.price}} 포인트
    </q-card-section>
    <q-card-actions>
      <q-btn color="primary" @click="confirmBuying">구매하기</q-btn>
    </q-card-actions>
    <!-- 경고 및 구매/적용 창 --> 
    <message-pop-up
      v-if="buy.state"
      :title="buy.title"
      :cancel="true"
      :message="buy.message"
      @reverse="buyItem"
    />
  </q-card>
</template>

<script>
import MessagePopUp from '@/components/MessagePopUp.vue'
import { computed, reactive } from 'vue'
import {useStore} from 'vuex'
import drf from '@/api/drf.js'
import axios from 'axios'
export default {
  name: 'PointItem',
  components: {
    MessagePopUp,
  },
  props: {
    title: Object,
    icon: Object,
  },
  setup(props) {
    // 현재 포인트 정보 필요
    const store = useStore()
    const item = reactive({
      type: props.title? '칭호':'배지',
      id: props.title?.id || props.icon?.id,
      title: props.title?.title || props.icon?.title,
      content: props.title?.content || props.icon?.content,
      price: props.title?.price || props.icon?.price,
    })
    const buy = reactive({
      title: `${item.type} 구매 확인`,
      message: `구매 후에는 포인트가 차감됩니다. \n 정말 ${item.type} ${item.title} 을/를 구매하시겠습니까?`,
      prompt: false,
      state: computed(() => buy.prompt)
    })
    const confirmBuying = () => {
      buy.prompt = true
    }
    const buyItem = (val) => {
      if (val) {
        let url = null
        if (props.title) {
          url = drf.pointShop.buyTitle()
        } else {
          url = drf.pointShop.buyIcon()
        }
        axios({
          url,
          method: 'post',
          headers: store.getters.authHeader,
          data: {pk: item.id}
        })
      }
    }
    let img = drf.file.path() + props.icon?.icon
    return {
      buyItem,
      confirmBuying,
      img,
      buy,
      item
    }
  },
}
</script>