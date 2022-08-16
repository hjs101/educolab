<template>
  <q-dialog
      v-model="load.state">
      <q-card>
        <q-card-section>
          <q-spinner-grid color="teal" size="5.5em"/>
        </q-card-section>
      </q-card>
    </q-dialog>
</template>

<script>
import { reactive, computed } from 'vue'
export default {
  name: 'TheSpinner',
  props: {
    loading: Boolean,
  },
  setup() {
    const load = reactive({
      ing: true,
      state: computed(() => load.ing)
    })
    return {
      load,
    }
  },
}
</script>