<template>
  <div class="baseStyle" v-if="!emptyQuiz">
    <h4 class="text-center">Quiz</h4>
    <hr>
    <div class="row justify-end q-mt-lg">
      <q-btn
        @click="QuizCreate"
        class="create-btn q-mx-lg q-py-sm"
        color="blue-6"
        label="퀴즈 등록"
      />
    </div>

    <div class="q-pa-md">
      <q-markup-table>
        <thead>
          <tr class="text-center">
            <th class="text-size">번호</th>
            <th class="text-center text-size">제목</th>
            <th class="text-center text-size">등록일</th>
            <th class="text-center text-size">퀴즈 시작</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="(quiz, index) in quiz.slice((page - 1) * 10, page * 10)"
            :key="index"
            >
            <td class="text-center text-size">{{ index + 1 + (page - 1) * 10 }}</td>
            <td
              @click="quizDetail(quiz.pk)"
              class="text-size cursor-pointer text-left"
            >
              {{ quiz.title }}
            </td>
            <td class="text-center text-size">
              {{ timeInfo(quiz.updated_at) }}
            </td>
            <!-- 퀴즈 시작 버튼에서 함수 구현 -->
            <td class="text-center text-size">
              <q-btn
                @click="startQUiz(quiz.pk)"
                class="button-size"
                color="amber-9"
                >Go Quiz!</q-btn
              >
            </td>
          </tr>
        </tbody>
      </q-markup-table>
      <the-pagination
        v-if="quizLength" 
        :limit="quizLength"
        @change-page="changePage" />
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import {ref} from 'vue'
import ThePagination from '@/components/ThePagination.vue'
import {isEmpty} from 'lodash'

export default({
  name: 'QuizView',
  components: {
    ThePagination,
  },
  computed: { 
    ...mapGetters(['quiz', 'quizLength', 'isLoggedIn', 'currentUser']),
    emptyQuiz() {
      return isEmpty(this.quiz)
    }
  },
  methods: {
    ...mapActions(["quizList"]),
    timeInfo(time) {
      const d = new Date(time);
      return d.getFullYear() + ". " + (d.getMonth() + 1) + ". " + d.getDate();
    },
    quizDetail(quizPk) {
      this.$router.push({ name: "QuizDetail", params: { quizPk: quizPk } });
    },
    QuizCreate() {
      this.$router.push({ name: "QuizCreate" });
    },
    // 여기서 구현 진행하시면 됩니다..
    startQUiz(quizPk) {
      this.$router.push({ name: "QuizWait", params: { quizPk: quizPk } });
    },
  },
  created() {
    if (!this.isLoggedIn) {
      this.$router.push('/educolab/login')
    } else if (!this.currentUser.userflag) {
      this.$router.push('/educolab')
    } else {
      this.quizList()
    }
  },
  setup() {
    let page = ref(1)
    const changePage = (value) => {
      page.value = value
    }
    return {
      page,
      changePage
    }
  }
})
</script>

<style scoped>
.text-size {
  font-size: 2vmin;
}
.button-size {
  font-size: 1.6vmin;
}
.text-nodec {
  text-decoration: none;
}
.button-magn {
  margin-right: 200px;
}
.create-btn {
  font-size: 1rem;
}
</style>
