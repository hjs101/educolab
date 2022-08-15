<template>
  <main class="baseStyle" >
    <h3>포인트 페이지</h3>
    <!-- 회원 정보 -->
    <q-card class="my-card bg-secondary text-white">
      <q-card-section>
        <div class="text-h6">name님 환영합니다</div>
        <div class="text-subtitle2">학교 정보</div>
      </q-card-section>

      <q-card-section>
        <p>이미지, 칭호, 업적 들어갈 자리</p>
      </q-card-section>

      <q-separator dark />

      <q-card-actions>
        <q-btn flat>로그아웃</q-btn>
        <q-btn flat>프로필 수정</q-btn>
      </q-card-actions>
    </q-card>
    <!-- 여기에 칭호 목록 -->
    <section v-if="items" class="q-py-md">
      <q-card class="q-pa-md row">
        <h5 class="text-center col-12">칭호</h5>
        <div
          class="q-pa-sm col-4"
          v-for="title in items.titles.slice((page.title-1)*10, page.title*10)"
          :key="title.id">
          <point-item :title="title"/>
        </div>
        <the-pagination
          v-if="page.titleLength"
          :limit="page.titleLength"
          target="title"
          class="col-12"
          @change-page="changePage"
        />
      </q-card>
    </section>
    <!-- 여기에 배지 목록 -->
    <section v-if="items" class="q-py-md">
      <q-card class="q-pa-md row">
        <h5 class="text-center col-12">배지</h5>
        <div
          class="q-pa-sm col-4"
          v-for="icon in items.icons.slice((page.icon-1)*10, page.icon*10)"
          :key="icon.id">
          <point-item :icon="icon"/>
        </div>
        <the-pagination
          v-if="page.iconLength"
          :limit="page.iconLength"
          target="icon"
          class="col-12"
          @change-page="changePage"
        />
      </q-card>
    </section>
    <!-- 구매 성공을 알림 -->
    <message-pop-up
      v-if="confirm.computedState"
      :message="confirm.message"
      @reverse="confirm.prompt = false"
    />
  </main>
</template>

<script>
import {onBeforeMount, reactive, ref, computed} from 'vue'
import axios from 'axios'
import drf from '@/api/drf.js'
import {useStore} from 'vuex'
import PointItem from '@/components/PointItem.vue'
import ThePagination from '@/components/ThePagination.vue'
import MessagePopUp from '@/components/MessagePopUp.vue'
export default {
  components: {
    PointItem,
    ThePagination,
    MessagePopUp
  },
  setup() {
    const store = useStore()
    let items = ref(null)
    onBeforeMount(() => {
      axios({
        url: drf.pointShop.main(),
        methods: 'get',
        headers: store.getters.authHeader
      })
        .then((res) => {
          items.value = res.data
          console.log(items)
        })
    })
    const confirm = reactive({
      message: '구매되었습니다. 바로 적용하시겠습니까?',
      prompt: false,
      computedState: computed(() => confirm.prompt),
    })
    const page = reactive({
      title: 1,
      icon: 1,
      titleLength: computed(() => Math.ceil(items.value?.titles.length/10)),
      iconLength: computed(() => Math.ceil(items.value?.icons.length/10)),
    })
    const changePage = (val, target) => {
      page[target] = val
    }
    return {
      items,
      page,
      confirm,
      changePage
    }
  },
}
</script>