<template>
  <q-card>
    <q-card-section>
      <div class="text-h6">상/벌점</div>
    </q-card-section>
    <q-card-section>
      <q-input
        label="학생명"
      />
      <q-btn color="primary">검색</q-btn>
      <div>
        학생 이름이 뜨는 곳
      </div>
      <div>
        유형
        <q-radio dense v-model="type" val="plus" label="상점" />
        <q-radio dense v-model="type" val="minus" label="벌점" />
      </div>
      <div>
        점수
        <q-input type="number" :min="min" :max="max"/>
        사유
        <q-input />
      </div>
    </q-card-section>
    <q-card-action>
      <q-btn label="점수 부여" />
      <q-btn label="초기화" />
    </q-card-action>
  </q-card>
</template>

<script>
import {computed, ref} from 'vue'
export default {
  name: 'GrantPoint',
  setup() {
    let type = ref(null)
    let min = computed(() => type.value === 'plus'? 1 : -10)
    let max = computed(() => type.value === 'plus'? 10 : -1)
    return {
      type,
      min,
      max
    }
  },
}
</script>