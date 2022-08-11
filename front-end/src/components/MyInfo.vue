<template>
  <q-card class="my-card">
    안녕하세요 {{info.name}}님
    <h5 class="text-center">내 정보</h5>
    <q-card-section horizontal>
      <q-img
        class="col-5"
        :src="info.profil"
      />

      <q-card-section>
        아이디 {{info.username}} | 생년월일 {{info.birthday}}
        <br>
        학교 {{school}}
        <span v-if="!info.userflag">
          {{info.grade}}학년  {{info.class_field}}반
        </span>
        <span v-if="!info.userflag">
          칭호 {{info.wear_title.title}}
        </span>
      </q-card-section>
    </q-card-section>

    <q-separator />

    <q-card-actions>
      <q-btn color="primary">
        정보 수정
      </q-btn>
      <q-btn color="primary">
        비밀번호 변경
      </q-btn>
      <!-- 학생만 -->
      <q-btn color="primary">
        업적/칭호 적용
      </q-btn>
    </q-card-actions>
  </q-card>
</template>

<script>
import {useStore} from 'vuex'
export default {
  name: 'MyInfo',
  props: {
    info: Object,
  },
  setup() {
    const store = useStore()
    const school = store.getters.currentUser.school
    return {
      school
    }
  },
}
</script>