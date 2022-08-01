<template>
  <div>
    <span>{{ notice.index.classification }}</span>
    <span>{{ notice }}</span>
  </div>
</template>

<script>
export default {
  name: 'NoticeItem',
  props: {
    notice: Object,
  }
}
</script>