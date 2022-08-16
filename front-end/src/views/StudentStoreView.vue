<template>
  <main class="baseStyle" >
    <h4 class="text-center">포인트 상점</h4>
    <hr>
    <!-- 회원 정보 -->
    <q-card class="q-my-lg bg-secondary text-white">
      <q-card-section>
        <div class="text-h6">name</div>
        <div class="text-subtitle2">학교 정보</div>
        <p>이미지, 칭호, 업적 들어갈 자리</p>
      </q-card-section>
    </q-card>
    <q-card>
      <q-tabs
        v-model="tab"
        dense
        class="text-grey"
        active-color="primary"
        indicator-color="primary"
        align="justify"
        narrow-indicator
      >
        <q-tab name="alias" label="칭호" />
        <q-tab name="badge" label="배지" />
      </q-tabs>

      <q-separator />
      <q-tab-panels v-model="tab">
        <q-tab-panel name="alias">
          <div
            bordered
            class="rounded-borders">
            <section v-if="items" class="q-py-md row">
              <div class="q-pa-md row">
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
              </div>
            </section>
          </div>
        </q-tab-panel>

        <q-tab-panel name="badge">
          <div
            bordered
            class="rounded-borders">
            <section v-if="items" class="q-py-md">
              <div class="q-pa-md row">
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
              </div>
            </section>
          </div>
        </q-tab-panel>
      </q-tab-panels>
    </q-card>
    <!-- 구매 성공을 알림 & 적용 여부 선택-->
    <message-pop-up
      v-if="confirm.computedState"
      :message="confirm.message"
      :cancel="true"
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
    let tab = ref('alias')
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
      tab,
      page,
      confirm,
      changePage
    }
  },
}
</script>