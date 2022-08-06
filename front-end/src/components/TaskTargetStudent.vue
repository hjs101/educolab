<template>
  <div>
    <q-expansion-item
      expand-separator
      :label="item.student.name"
      :caption="item['submit_at']"
    >
      <q-card>
        <q-card-section>
          {{item.content}}
          <br>
          {{item['submit_flag']}}
          {{item['atch_file_name']}}
          <!-- {{item['atch_file']}} -->
          <q-input type="number" label="점수" />
          또는 select
          <q-btn color="primary" label="채점하기" />
          최신이 위로 오도록 정렬
        </q-card-section>
      </q-card>
    </q-expansion-item>
  </div>
</template>

<script>
export default {
  name: 'TaskTargetStudent',
  props: {
    item: Object,
  },
}
</script>