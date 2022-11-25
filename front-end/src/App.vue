<template>
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
  <div style="height: 2000px">
    <!-- 교사 navbar -->
    <div v-if="isLoggedIn && currentUser.userflag">
      <div class="q-pa-md q-gutter-sm">
        <q-bar style="height:100px;" >
          <a href="/"><img src="@/assets/educolab.png" alt="educolab" style="width:100px; height:100px;"></a>
          <div class="cursor-pointer"><router-link to="/notice">공지사항</router-link></div>
          <div class="cursor-pointer"><router-link to="/teacher/task">과제</router-link></div>
          <div class="cursor-pointer"><router-link to="/quiz">퀴즈</router-link></div>
          <div class="cursor-pointer"><router-link to="/search">설문조사</router-link></div>
          <div class="cursor-pointer"><router-link to="/teacher">마이페이지</router-link></div>
          <button @click="logoutBtn">로그아웃</button>
        </q-bar>
        <hr>
      </div>
    </div>

    <!-- 학생 navbar -->
    <div v-if="isLoggedIn && !currentUser.userflag">
      <div class="q-pa-md q-gutter-sm">
        <q-bar style="height:100px;" >
          <a href="/"><img src="@/assets/educolab.png" alt="educolab" style="width:100px; height:100px;"></a>
          <div class="cursor-pointer"><router-link to="/notice">공지사항</router-link></div>
          <div class="cursor-pointer"><router-link to="/student/task">과제</router-link></div>
          <div class="cursor-pointer"><router-link to="/student/writing">내 필기</router-link></div>
          <div class="cursor-pointer"><router-link to="/student/store">포인트 상점</router-link></div>
          <div class="cursor-pointer"><router-link to="/student">마이페이지</router-link></div>
          <button @click="logoutBtn">로그아웃</button>
        </q-bar>
        <hr>
      </div>
    </div>

  <router-view />
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'MainPage',
  computed: {
    ...mapGetters(['isLoggedIn', 'currentUser'])
  },
  methods: {
    ...mapActions(['logout']),
    logoutBtn() {
      if (this.isLoggedIn) {
        this.logout()
      } else {
        this.$router.back()
      }
    }
  }
}
</script>

<style>
/* 모든 페이지에서 공통으로 사용할 스타일 정의 */
  h3 {
    text-align: center;
  }
  .button {
    text-decoration: none;
  }
  .buttonGroup {
  display: flex;
  justify-content: center;
  text-align: center;
  gap: 10px;
  }
  .center {
    text-align: center;
  }
</style>
=======
  <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </nav>
  <router-view/>
=======
  <q-layout view="lHh Lpr lFf">
    <q-header elevated class="glossy">
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          @click="leftDrawerOpen = !leftDrawerOpen"
          aria-label="Menu"
          icon="mdi-menu"
        />

        <q-toolbar-title>
          Quasar App
        </q-toolbar-title>

        <div>Quasar v{{ $q.version }}</div>
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
      class="bg-grey-2"
    >
      <q-list>
        <q-item-label header>Essential Links</q-item-label>
        <q-item clickable tag="a" target="_blank" href="https://quasar.dev">
          <q-item-section avatar>
            <q-icon name="mdi-school" />
          </q-item-section>
          <q-item-section>
            <q-item-label>Docs</q-item-label>
            <q-item-label caption>quasar.dev</q-item-label>
          </q-item-section>
        </q-item>
        <q-item clickable tag="a" target="_blank" href="https://github.com/quasarframework/">
          <q-item-section avatar>
            <q-icon name="mdi-code-tags" />
          </q-item-section>
          <q-item-section>
            <q-item-label>Github</q-item-label>
            <q-item-label caption>github.com/quasarframework</q-item-label>
          </q-item-section>
        </q-item>
        <q-item clickable tag="a" target="_blank" href="https://chat.quasar.dev">
          <q-item-section avatar>
            <q-icon name="mdi-message-text" />
          </q-item-section>
          <q-item-section>
            <q-item-label>Discord Chat Channel</q-item-label>
            <q-item-label caption>chat.quasar.dev</q-item-label>
          </q-item-section>
        </q-item>
        <q-item clickable tag="a" target="_blank" href="https://forum.quasar.dev">
          <q-item-section avatar>
            <q-icon name="mdi-forum" />
          </q-item-section>
          <q-item-section>
            <q-item-label>Forum</q-item-label>
            <q-item-label caption>forum.quasar.dev</q-item-label>
          </q-item-section>
        </q-item>
        <q-item clickable tag="a" target="_blank" href="https://twitter.com/quasarframework">
          <q-item-section avatar>
            <q-icon name="mdi-twitter" />
          </q-item-section>
          <q-item-section>
            <q-item-label>Twitter</q-item-label>
            <q-item-label caption>@quasarframework</q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
    </q-drawer>

    <q-page-container>
      <HelloWorld />
    </q-page-container>
  </q-layout>
>>>>>>> 34b83a2 (Feat : 퀘이사 UI Framework 적용)
=======
  <!-- 로그인된 경우-->
  <!-- <the-nav-bar/> -->
  <!-- 로그인 안 된 경우 -->
  <login-view/>
>>>>>>> 23e74e9 (Feat : 로그인 화면 제작 완료 & 기능 구현 미완료 & 약관 동의 화면 구현)
=======
  <div>
    <!-- 로그인된 경우 nav bar-->
    
    <!-- 로그인 안 된 경우 login 페이지로 push ?? beforeEach 사용-->
    <router-view></router-view>
  </div>
>>>>>>> 860f864 (Refactor : 로그인, 회원가입 동의 페이지 코드 수정 & 404 페이지 만듦)
</template>

<style>
/* 모든 페이지에서 공통으로 사용할 스타일 정의 */
  h3 {
    text-align: center;
  }
  .button {
    text-decoration: none;
  }
  .buttonGroup {
  display: flex;
  justify-content: center;
  text-align: center;
  gap: 10px;
  }
  .center {
    text-align: center;
  }

</style>

<script>
// import TheNavBar from './components/TheNavBar.vue'
// import {created} from 'vue'
=======
  <div container style="height: 2000px">
    <!-- 교사 navbar -->
    <div class="q-pa-md q-gutter-sm">
      <q-bar container style="height: 100px">
        <div class="cursor-pointer"><router-link to="/notice">공지사항</router-link></div>
        <div class="cursor-pointer"><router-link to="/teacher/task">과제</router-link></div>
        <div class="cursor-pointer"><router-link to="/quiz">퀴즈</router-link></div>
        <div class="cursor-pointer"><router-link to="/search">설문조사</router-link></div>
        <div class="cursor-pointer"><router-link to="/teacher">마이페이지</router-link></div>      
      </q-bar>
    </div>
  <router-view />
=======
  <div>
  <div v-if='isLoggedIn'><router-link to='/'></router-link></div>
  <div v-else><router-link to='/quiz'></router-link></div>  

    <router-view />
>>>>>>> b22ae6e (공지사항 메인 페이지)
  </div>
</template>

<script>
<<<<<<< HEAD
>>>>>>> e66f000 (navbar 생성)
export default {
  name: 'theNavbar',

<<<<<<< HEAD
  components: {
    // TheNavBar,
  }
=======
>>>>>>> e66f000 (navbar 생성)
=======

export default {
  name: 'theNavbar',
  data() {
    let isLoggedIn = true
    if (isLoggedIn == false) {
      isLoggedIn = false
    }
    return {
      isLoggedIn
    }
  }
>>>>>>> b22ae6e (공지사항 메인 페이지)
}
<<<<<<< HEAD
</style>
>>>>>>> 1f63946 (vue 환경셋팅)
=======
</script>
>>>>>>> 34b83a2 (Feat : 퀘이사 UI Framework 적용)
