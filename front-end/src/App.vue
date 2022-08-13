<template>
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
  <div style="height: 2000px">
<<<<<<< HEAD
<<<<<<< HEAD
    <!-- 교사 navbar -->
    <div v-if="isLoggedIn && currentUser.userflag">
=======
    <!-- 교사 navbar -->
    <div v-if="isLoggedIn">
>>>>>>> 77a4159 (로그아웃 구현)
=======
  <div style="height: 2000px">
    <!-- 교사 navbar -->
    <div v-if="isLoggedIn && currentUser.userflag">
>>>>>>> e6b54fb (asdu)
      <div class="q-pa-md q-gutter-sm">
        <q-bar style="height:100px;" >
          <a href="/"><img src="@/assets/educolab.png" alt="educolab" style="width:100px; height:100px;"></a>
<<<<<<< HEAD
          <div class="cursor-pointer"><router-link to="/notice">공지사항</router-link></div>
          <div class="cursor-pointer"><router-link to="/teacher/task">과제</router-link></div>
          <div class="cursor-pointer"><router-link to="/quiz">퀴즈</router-link></div>
          <div class="cursor-pointer"><router-link to="/survey">설문조사</router-link></div>
          <div class="cursor-pointer"><router-link to="/teacher">마이페이지</router-link></div>
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e6b54fb (asdu)
=======
          <div class="button"><router-link to="/notice" class="button">공지사항</router-link></div>
          <div class="cursor-pointer"><router-link to="/teacher/task" class="button">과제</router-link></div>
          <div class="cursor-pointer"><router-link to="/quiz" class="button">퀴즈</router-link></div>
          <div class="cursor-pointer"><router-link to="/search" class="button">설문조사</router-link></div>
          <div class="cursor-pointer"><router-link to="/teacher" class="button">마이페이지</router-link></div>
>>>>>>> f4abfa5 (Feat : 과제 생성 기능 완료 & 과제 목록 불러오기 진행 중)
          <button @click="logoutBtn">로그아웃</button>
        </q-bar>
        <hr>
=======
  <div id="app">
=======
  <div>
>>>>>>> c9ecd87 (퀴즈 임베디드 연동)
=======
  <div class="test">
>>>>>>> 6ecfa2b (기본 폰트, 스타일 적용)
    <!-- 교사 navbar -->
    <div v-if="isLoggedIn && currentUser.userflag">
      <div class="bord-bt">
        <div class="q-py-md q-px-xl row items-center jooa-font nav-size">
          <a href="/educolab"><img class="q-mx-lg" src="@/assets/educolab.png" alt="educolab" style="width:4rem; height:4rem;"></a>
          <router-link class="q-px-xl button color5" to="/notice">공지사항</router-link>
          <router-link class="q-px-xl button color5" to="/teacher/task">과제</router-link>
          <router-link class="q-px-xl button color5" to="/quiz">퀴즈</router-link>
          <router-link class="q-px-xl button color5" to="/survey">설문조사</router-link>
          <router-link class="q-px-xl button color5" to="/teacher">마이페이지</router-link>
          <button class="q-px-lg" @click="logoutBtn">로그아웃</button>
        </div>
>>>>>>> 9bb5647 (메인 페이지 css)
=======
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
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
      </div>
    </div>

    <!-- 학생 navbar -->
    <div v-if="isLoggedIn && !currentUser.userflag">
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
        </q-bar>
        <hr>
      </div>
      <button @click="logoutBtn">로그아웃</button>
    </div>
    <!-- 학생 navbar -->
    <!-- <div v-else-if="flag==='student'">
>>>>>>> 77a4159 (로그아웃 구현)
=======
>>>>>>> e6b54fb (asdu)
      <div class="q-pa-md q-gutter-sm">
        <q-bar style="height:100px;" >
          <a href="/"><img src="@/assets/educolab.png" alt="educolab" style="width:100px; height:100px;"></a>
<<<<<<< HEAD
<<<<<<< HEAD
=======
      <div class="q-pa-md q-gutter-sm">
        <q-bar style="height:100px;" >
          <a href="/"><img src="@/assets/educolab.png" alt="educolab" style="width:100px; height:100px;"></a>
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
=======
>>>>>>> f7e1d76 (Feat : 학생 마이페이지 구현 완료 & 프로필/뱃지/칭호 변경 및 상벌점 부여 기능 진행 중)
          <div class="cursor-pointer"><router-link to="/notice">공지사항</router-link></div>
          <div class="cursor-pointer"><router-link to="/student/task">과제</router-link></div>
          <div class="cursor-pointer"><router-link to="/student/writing">내 필기</router-link></div>
          <div class="cursor-pointer"><router-link to="/student/store">포인트 상점</router-link></div>
          <div class="cursor-pointer"><router-link to="/student">마이페이지</router-link></div>
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e6b54fb (asdu)
=======
          <div class="cursor-pointer button"><router-link to="/notice" class="button">공지사항</router-link></div>
          <div class="cursor-pointer button"><router-link to="/student/task" class="button">과제</router-link></div>
          <div class="cursor-pointer button"><router-link to="/student/writing" class="button">내 필기</router-link></div>
          <div class="cursor-pointer button"><router-link to="/student/store" class="button">포인트 상점</router-link></div>
          <div class="cursor-pointer button"><router-link to="/student" class="button">마이페이지</router-link></div>
>>>>>>> f4abfa5 (Feat : 과제 생성 기능 완료 & 과제 목록 불러오기 진행 중)
=======
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
=======
>>>>>>> f7e1d76 (Feat : 학생 마이페이지 구현 완료 & 프로필/뱃지/칭호 변경 및 상벌점 부여 기능 진행 중)
=======
      <div class="bord-bt">
        <div class="q-py-md q-px-xl row items-center jooa-font nav-size">
          <a href="/educolab"><img class="q-mx-lg" src="@/assets/educolab.png" alt="educolab" style="width:4rem; height:4rem;"></a>
          <router-link class="q-px-xl button color5" to="/notice">공지사항</router-link>
          <router-link class="q-px-xl button color5" to="/student/task">과제</router-link>
          <router-link class="q-px-xl button color5" to="/student/point">포인트 상점</router-link>
          <router-link class="q-px-xl button color5" to="/student">마이페이지</router-link>
>>>>>>> d127577 (기능별 메인 페이지 구성)
          <button @click="logoutBtn">로그아웃</button>
        </div>
      </div>
    </div>
<<<<<<< HEAD
<<<<<<< HEAD

<<<<<<< HEAD
<<<<<<< HEAD
=======
    <!-- 로그인 했을 때 -->
    <!-- <the-navbar v-if="isLoggedIn"></the-navbar> -->
    
>>>>>>> c942112 (로그인 프론트와 백 연결)
=======
        </q-bar>
        <hr>
      </div>
    </div> -->

>>>>>>> 77a4159 (로그아웃 구현)
=======
>>>>>>> e6b54fb (asdu)
=======
>>>>>>> fa227ef (Feat & Fix : 과제 생성/수정 기능 완료, 나머지 기능 진행 중, 회원 관리 부분 컴포넌트화 및 버그 수정 중)
=======
    <!-- <footer class="bord-top">
      <div class="row justify-center items-center">
        <img class="q-mx-md" src="@/assets/educolab.png" alt="educolab" style="width:4rem; height:4rem;">
        <div class="ftr-size">
          <span class="text-bold">"교육과 서비스의 조화" edu colab!!</span>
          <p class="margin">edu colab는 학습 역량 증진 / 교육 연계 보조 / 수업의 질 향상을 목표로</p>
          <p class="margin">교사에게는 편리한, 학생에게는 학습욕구를 팽창시켜드립니다!!ㄴ</p>
        </div>
      </div>
    </footer> -->
>>>>>>> 9bb5647 (메인 페이지 css)
=======
  <div style="height:1500px">

=======
  <div style="height:1200px">
>>>>>>> 38a5ff1 (공지사항  수정 해결)
=======
  <div>
>>>>>>> 7f2a492 (설문조사  sass)
      <!-- 교사 navbar -->
    <div v-if="isLoggedIn && currentUser.userflag" class="jooa-font">
        <div class="navBar q-px-xl q-py-md bord-bt">
          <a href="/educolab"><img src="@/assets/educolab.png" alt="educolab" style="width:4rem; height:4rem;"></a>
          <div class="navBarUi nav-size">
            <router-link class="q-ml-xl button color5 navBarLi" to="/notice">공지사항</router-link>
            <router-link class="q-ml-xl button color5 navBarLi" to="/teacher/task">과제</router-link>
            <router-link class="q-ml-xl button color5 navBarLi" to="/quiz">퀴즈</router-link>
            <router-link class="q-ml-xl button color5 navBarLi" to="/survey">설문조사</router-link>
            <router-link class="q-ml-xl button color5 navBarLi" to="/teacher">마이페이지</router-link>
            <button @click="logoutBtn" class="q-ml-xl">로그아웃</button>
          </div>
          
          <div class="navBar_tool">
            <div v-if="onNavList">
              <div @click="activeNav" class="column items-center q-px-md bg-grey-13">
                <router-link class="text-subtitle2 button color5 navBarLi" to="/notice" flat>공지사항</router-link>
                <router-link class="text-subtitle2 button color5 navBarLi" to="/student/task" flat>과제</router-link>
                <router-link class="text-subtitle2 button color5 navBarLi" to="/student/point" flat>포인트 상점</router-link>
                <router-link class="text-subtitle2 button color5 navBarLi" to="/student">마이페이지</router-link>
              </div>
            </div>
            <q-icon @click="activeNav" class="cursor-pointer" name="mdi-menu" />
          </div>
        </div>  
    </div>

    <!-- 학생 navbar -->
    <div class="jooa-font" v-if="isLoggedIn && !currentUser.userflag">
        <div class="navBar q-px-xl q-py-md bord-bt">
          <a href="/educolab"><img src="@/assets/educolab.png" alt="educolab" style="width:4rem; height:4rem;"></a>
          <div class="navBarUi nav-size">
            <router-link class="q-ml-xl button color5 navBarLi" to="/notice" flat>공지사항</router-link>
            <router-link class="q-ml-xl button color5 navBarLi" to="/student/task" flat>과제</router-link>
            <router-link class="q-ml-xl button color5 navBarLi" to="/student/point" flat>포인트 상점</router-link>
            <router-link class="q-ml-xl button color5 navBarLi" to="/student">마이페이지</router-link>
            <button @click="logoutBtn" class="q-ml-xl">로그아웃</button>
          </div>
  
          <div class="navBar_tool">
            <div v-if="onNavList">
              <div @click="activeNav" class="column items-center q-px-md bg-grey-13">
                <router-link class="text-subtitle2 button color5 navBarLi" to="/notice" flat>공지사항</router-link>
                <router-link class="text-subtitle2 button color5 navBarLi" to="/student/task" flat>과제</router-link>
                <router-link class="text-subtitle2 button color5 navBarLi" to="/student/point" flat>포인트 상점</router-link>
                <router-link class="text-subtitle2 button color5 navBarLi" to="/student">마이페이지</router-link>
              </div>
            </div>
            <q-icon @click="activeNav" class="cursor-pointer" name="mdi-menu" />
          </div>
        </div>
    </div>

<<<<<<< HEAD
      <!-- <footer class="bord-top bg-blue-grey-12 q-py-sm">
        <div class="row justify-start items-center">
          <img class="q-mx-xl" src="@/assets/footerlogo.png" alt="educolab" style="width:5rem; height:5rem;">
          <div class="ftr-size">
            <span class="text-bold">"교육과 서비스의 조화" edu colab!!</span><hr>
            <span>edu colab는 학습 역량 증진 / 교육 연계 보조 / 수업의 질 향상을 목표로 합니다.</span>
            <p>교사에게는 편리한, 학생에게는 학습욕구를 팽창시켜드립니다!!</p>
          </div>
        </div>
<<<<<<< HEAD
    </footer>

>>>>>>> e824b6b (메인페이지 화면 구성)
=======
    </footer> -->
    
>>>>>>> 38a5ff1 (공지사항  수정 해결)
=======
>>>>>>> 7f2a492 (설문조사  sass)
  <router-view />
<<<<<<< HEAD
  
=======

  <router-view />
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
=======
>>>>>>> f7e1d76 (Feat : 학생 마이페이지 구현 완료 & 프로필/뱃지/칭호 변경 및 상벌점 부여 기능 진행 중)
  </div>
</template>

<<<<<<< HEAD
<script>
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e6b54fb (asdu)
import { mapGetters, mapActions } from 'vuex'
<<<<<<< HEAD
import {onBeforeMount} from 'vue'
import {useStore} from 'vuex'
import {isEmpty} from 'lodash'
=======
import { mapGetters, mapActions } from 'vuex'
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
=======
>>>>>>> f7e1d76 (Feat : 학생 마이페이지 구현 완료 & 프로필/뱃지/칭호 변경 및 상벌점 부여 기능 진행 중)

export default {
  name: 'MainPage',
<<<<<<< HEAD
  data() {
    return {
      isHovering : true
    }
  },
  computed: {
    ...mapGetters(['isLoggedIn', 'currentUser']),
    flag() {
      const flag = this.currentUser.userflag
      return flag
    }
=======
  computed: {
    ...mapGetters(['isLoggedIn', 'currentUser'])
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
  },
  methods: {
    ...mapActions(['logout']),
    logoutBtn() {
      if (this.isLoggedIn) {
        this.logout()
      } else {
        this.$router.back()
      }
    },
<<<<<<< HEAD
    selectedHovering() {
      this.isHovering = true
    },
    unselectedHovering() {
      this.isHovering = false
    }
  },
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
  setup() {
    const store = useStore()
    onBeforeMount(() => {
      // 현재 로그인이 되어있는지 확인 (토큰이 있는지 확인) -> 없으면 그대로, 있으면 main
      // 현재 사용자 타입과 로그인한 사용자 타입이 맞는지 확인 -> 맞으면 그래도, 아니면 다른 곳으로 (접근 권한 없다는 페이지? 팝업 후 메인?)
      // 리프레시 토큰
      // 
      if (isEmpty(store.getters.currentUser)) {
        // 요청 보내기
      }
    })
=======
  created() {
    if (this.isLoggedIn === false) {
      this.$router.push({name:'login'})
    }
>>>>>>> f7e1d76 (Feat : 학생 마이페이지 구현 완료 & 프로필/뱃지/칭호 변경 및 상벌점 부여 기능 진행 중)
  }
<<<<<<< HEAD
=======
// import TheNavbar from '@/views/TheNavbar.vue'

export default {
  name: 'MainPage',
  // data() {
  //   return {
  //     isLoggedIn : false,
  //   }
  // },
  // components: {
  //   TheNavbar
  // },
>>>>>>> c942112 (로그인 프론트와 백 연결)
=======
import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'MainPage',
  computed: {
    ...mapGetters(['isLoggedIn'])
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
>>>>>>> 77a4159 (로그아웃 구현)
=======
>>>>>>> e6b54fb (asdu)
=======
>>>>>>> 452a9d1 (설문조사  등록)
=======
  created() {
    if (this.isLoggedIn === false) {
      this.$router.push({name:'login'})
    }
  }
>>>>>>> 9bb5647 (메인 페이지 css)
=======
  }
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
=======
  // created() {
  //   if (this.isLoggedIn === false) {
  //     this.$router.push({name:'login'})
  //   }
  // }
>>>>>>> bf6f861 (Feat : 교사 상/벌점 부여 기능 구현 완료)
}
</script>

=======
>>>>>>> 38a5ff1 (공지사항  수정 해결)
<style>
/* 모든 페이지에서 공통으로 사용할 스타일 정의 */
<<<<<<< HEAD

 /* 폰트 적용 */
  @font-face {
    font-family: "jooa";
    src: url("@/assets/fonts/BMJUA_ttf.ttf");
  }
  
  .jooa-font {
    font-family: "jooa"
  }

  .navBar {
    display: flex;
    flex-direction: row;
  }
  
  .navBarUi {
    display: flex;
    align-items: center;
  }

  /* 컴포넌트 기본 css */
  .baseStyle {
    width: 80%;
    margin: auto;
    font-family: "jooa";
    min-width: 450px;
    height:1200px;
  }
  .surveyStyle {
    width: 80%;
    margin: auto;
    min-width: 450px;
    height:1200px;
  }

<<<<<<< HEAD
  .font-size2 {
    font-size: 1.1rem
  }
=======
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
=======
  .nav-size {font-size: 1.3rem}

>>>>>>> d127577 (기능별 메인 페이지 구성)
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
    margin: 100px 0px;
    }
  .center {
    text-align: center;
  }
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
  <div style="height:2000px;">

    <!-- 로그인 했을 때 -->
    <the-navbar v-if="isLoggedIn"></the-navbar>

    <!-- 로그인 안했을 때 -->
    <login-view v-else-if="!isLoggedIn"></login-view>
    
>>>>>>> 3d37e1b (공지사항 검색기능 구현)
  </div>

</template>

<script>
<<<<<<< HEAD
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
=======
import TheNavbar from '@/views/TheNavbar.vue'
import LoginView from '@/views/LoginView.vue'
>>>>>>> 3d37e1b (공지사항 검색기능 구현)

export default {
  name: 'MainPage',
  data() {
    return {
      isLoggedIn : true,
    }
  },
  components: {
    TheNavbar, LoginView
  }
>>>>>>> b22ae6e (공지사항 메인 페이지)
}
<<<<<<< HEAD
</style>
>>>>>>> 1f63946 (vue 환경셋팅)
=======
</script>
>>>>>>> 34b83a2 (Feat : 퀘이사 UI Framework 적용)
=======
</style>
>>>>>>> e6b54fb (asdu)
=======
  .bord-bt {
    border-bottom: 1px solid #99DFF9;
  }
  .bord-top {
    border-top: 1px solid #99DFF9;
  }
  .color1 {color: #FF9966;}
  .color2 {color: #8BFF8B;}
  .color3 {color: #FFC000;}
  .color4 {color: #99DFF9;}
  .color5 {color: black;}

  .ftr-size {
    font-size: 0.9rem;
  } 
  footer {
    position: absolute;
    bottom: -1000px;
    width: 100%
  }
<<<<<<< HEAD
  .hidden {
    visibility: hidden;
  }
  .active {
    color: blue;
    font-weight: bold;
  }
</style>
<<<<<<< HEAD
>>>>>>> 9bb5647 (메인 페이지 css)
=======
</style>
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
=======
>>>>>>> f7e1d76 (Feat : 학생 마이페이지 구현 완료 & 프로필/뱃지/칭호 변경 및 상벌점 부여 기능 진행 중)
=======
  .navBarLi:hover {
    border-bottom: 2px solid #8BFF8B;
  }
  .navBar_tool {
    position: absolute;
    right: 32px;
    font-size: 2rem;
    color: #FF9966;
    display : none;
  }

  @media screen and (max-width: 840px) {
    .navBar {
      display: flex;
      flex-direction: column;
    }
    .navBarUi {
      display: flex;
      flex-direction: column;
      display: none;
    }
    .navBar_tool {
      display: flex;
    }
  }
</style>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'MainPage',
  data() {
    return {
      isHovering : true,
      onNavList : false,
    }
  },
  computed: {
    ...mapGetters(['isLoggedIn', 'currentUser']),
    flag() {
      const flag = this.currentUser.userflag
      return flag
    },
  },
  methods: {
    ...mapActions(['logout']),
    logoutBtn() {
      if (this.isLoggedIn) {
        this.logout()
      } else {
        this.$router.back()
      }
    },
    selectedHovering() {
      this.isHovering = true
    },
    unselectedHovering() {
      this.isHovering = false
    },
    activeNav() {
      if(this.onNavList == true) {
        this.onNavList = false
      } else {
        this.onNavList = true
      }
    }
  },
  created() {
    if (this.isLoggedIn === false) {
      this.$router.push({name:'login'})
    }
  }
}
</script>
>>>>>>> 38a5ff1 (공지사항  수정 해결)
