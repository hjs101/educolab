<template>
  <main class="baseStyle" >
    <h4 class="text-center">포인트 상점</h4>
    <hr>
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
        <q-tab class="text-size" name="alias" label="칭호" />
        <q-tab class="text-size" name="badge" label="배지" />
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
                  <point-item :title="title" @reverse="success" />
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
                  <point-item :icon="icon" @reverse="success" />
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
import {useRouter} from 'vue-router'
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
    const router = useRouter()
    let items = ref(null)
    let tab = ref('alias')
    onBeforeMount(() => {
      if (!store.getters.isLoggedIn) {
      router.push('/educolab/login')
    } else if (store.getters.currentUser.userflag) {
      router.push('/educolab')
    } else {
      axios({
        url: drf.pointShop.main(),
        methods: 'get',
        headers: store.getters.authHeader
      })
        .then((res) => {
          items.value = res.data
        })
    }
    })
    const confirm = reactive({
      message: null,
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
    const success = (message) => {
      confirm.message = message
      confirm.prompt = true
    }
    return {
      items,
      tab,
      page,
      confirm,
      changePage,
      success
    }
  },
}
</script>

<style scoped>
  .text-size {
    font-size: 1rem;
  }
</style>