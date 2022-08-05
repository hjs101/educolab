<template>
  <router-link div class="button black" :to="{name: 'TaskDetailView', params: {
    userType: userType, taskPk: 1
  }}">
    <q-card>
      <q-card-section >
        <div class="text-h6">{{item.title}}</div>
        <div class="text-h6">제출 기한</div>
        <div class="text-subtitle2">{{item.teacher}}</div>
      </q-card-section>
      <q-card-section>
        {{item.created_at}}
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
    item: Object,
  },
  setup() {
    const userType = 'student'
    return {
      userType
    }
  }
}
</script>