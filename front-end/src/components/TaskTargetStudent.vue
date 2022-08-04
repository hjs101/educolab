<template>
  <div>
    <q-expansion-item
      expand-separator
      :label="sample.name"
      :caption="sample.submitAt"
    >
      <q-card>
        <q-card-section>
          {{sample.content}}
          <br>
          첨부파일 |
          채점하기 버튼 |
          채점여부 |
          최신이 위로 오도록 정렬
          
        </q-card-section>
      </q-card>
    </q-expansion-item>

    <q-expansion-item
      expand-separator
      label="Wifi settings"
    >
      <q-card>
        <q-card-section>
          내용
        </q-card-section>
      </q-card>
    </q-expansion-item>

    <q-expansion-item
      expand-separator
      label="Drafts"
      header-class="text-purple"
    >
      <q-card>
        <q-card-section>
          내용
        </q-card-section>
      </q-card>
    </q-expansion-item>
  </div>
</template>

<script>
export default {
  name: 'TaskTargetStudent',
  props: {
    sample: Object,
  },
}
</script>