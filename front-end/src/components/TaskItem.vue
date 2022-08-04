<template>
  <router-link div class="button black" :to="{name: 'TaskDetailView', params: {
    userType: userType, taskPk: sample.pk
  }}">
    <q-card>
      <q-card-section >
        <div class="text-h6">{{sample.title}}</div>
        <div class="text-h6">제출 기한</div>
        <div class="text-subtitle2">{{sample.name}}</div>
      </q-card-section>
      <q-card-section>
        {{sample.content}}
        <br>
        최신이 위로 오도록 정렬 |
        카드 내부 클릭하면 상세 페이지로 이동
      </q-card-section>
    </q-card>
  </router-link>
</template>

<style>
  .black {
    color: black;
  }
</style>

<script>
export default {
  name: 'TaskItem',
  props: {
    sample: Object,
  },
  setup() {
    const userType = 'student'
    return {
      userType
    }
  }
}
</script>