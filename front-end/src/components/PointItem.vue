<template>
  <q-card>
    <q-card-section class="row justify-center text-center">
      <q-card v-if="icon" class="size100 col-12">
        <img :src="img">
      </q-card>
      <div class="text-h6 col-12 q-pa-md">
        {{item.title}}
      </div>
      <br>
      <div class="col-12">
        {{item.content}}
      </div>
      <br>
    </q-card-section>
    <q-card-actions class="row justify-center">
      <q-btn
        color="primary"
        @click="confirmBuying"
        class="q-mb-md"
        :label="`${item.price} 포인트`" />
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

<style scoped>
  .size100 {
    width: 100px;
  }
</style>
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
  setup(props, {emit}) {
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
      message: `구매 후에는 포인트가 차감됩니다. 정말 ${item.type} ${item.title} 을/를 구매하시겠습니까?`,
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
        let message = null
        console.log(url)
        axios({
          url,
          method: 'post',
          headers: store.getters.authHeader,
          data: {pk: item.id}
        })
          .then((res) => {
            console.log(res.data)
            message = res.data.message
          })
          .catch(() => {
            message = '오류가 발생했습니다'
          })
          .finally(() => {
            buy.prompt = false
            emit('reverse', message)
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