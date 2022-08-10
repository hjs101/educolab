<template>
  <div>
    <q-expansion-item
      expand-separator
      :label="item.student.name"
      :caption="submitState+date"
    >
      <q-card>
        <q-card-section>
          {{item.content}}
          <br>
          <div v-for="(file, idx) in item['atch_file_name']" :key="idx">
            <a :href="url+item['atch_file'][idx]">{{file}}</a>
          </div>
          <div v-if="!isChecked">
            <q-input type="number" v-model="point" label="점수" min="-1" max="5"/>
            <q-btn color="primary" label="채점하기" @click="checkTask"/>
          </div>
        </q-card-section>
      </q-card>
    </q-expansion-item>
    <message-pop-up
      v-if="confirm.isTrue"
      :message="message"
      @reverse="confirm.prompt = false"
    />
  </div>
</template>

<script>
import {computed, reactive, ref} from 'vue'
import {useStore} from 'vuex'
import dayjs from 'dayjs'
import drf from '@/api/drf.js'
import axios from 'axios'
import MessagePopUp from '@/components/MessagePopUp.vue'
export default {
  name: 'TaskTargetStudent',
  props: {
    item: Object,
    deadline: String,
    checkFlag: Boolean,
  },
  components: {
    MessagePopUp
  },
  setup(props) {
    const store = useStore()
    const date = props.item.submit_flag?` (${dayjs(props.item['submit_at']).format('YYYY-MM-DD HH:mm')})`:''
    const url = drf.file.path()+props.item['atch_file']
    let point = ref(null)
    let submitState = computed(() => props.item.submit_flag?'제출':'미제출')
    let message = ref(null)
    // 학생별 check_flag도!
    let isChecked = computed(() => props.deadline >= dayjs().format('YYYY-MM-DD') || props.checkFlag)
    const confirm = reactive({
      prompt: false,
      isTrue: computed(() => confirm.prompt)
    })
    const checkTask = () => {
      axios({
        url: drf.task.check(),
        method: 'post',
        headers: store.getters.authHeader,
        data: {
          pk: props.item.id,
          username: props.item.student.username,
          point: point.value * 1,
        },
      })
        .then(((res) => {
          message.value = res.data.message
          isChecked.value = true
        }))
        .catch(() => {
          message.value = '오류가 발생했습니다'
        })
        .finally(() => {
          confirm.prompt = true
        })
    }
    return {
      date,
      submitState,
      url,
      point,
      message,
      confirm,
      checkTask,
      isChecked
    }
  }
}
</script>