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
          <div v-if="isString">
            <a :href="url+item['atch_file']">
              {{item['atch_file_name']}}
            </a>
          </div>
          <div v-else>
            <div v-for="(file, idx) in item['atch_file_name']" :key="idx">
              <a :href="url+item['atch_file'][idx]">{{file}}</a>
            </div>
          </div> 
          <q-input type="number" label="점수" min="-1" max="5"/>
          <q-btn color="primary" label="채점하기" />
        </q-card-section>
      </q-card>
    </q-expansion-item>
  </div>
</template>

<script>
import {computed} from 'vue'
import dayjs from 'dayjs'
import drf from '@/api/drf.js'
export default {
  name: 'TaskTargetStudent',
  props: {
    item: Object,
  },
  setup(props) {
    const date = props.item.submit_flag?` (${dayjs(props.item['submit_at']).format('YYYY-MM-DD HH:mm')})`:''
    let submitState = computed(() => props.item.submit_flag?'제출':'미제출')
    const url = drf.file.path()+props.item['atch_file']
    let isString = computed(() => typeof(props.item['atch_file_name']) === 'string')
    return {
      date,
      submitState,
      url,
      isString
    }
  }
}
</script>