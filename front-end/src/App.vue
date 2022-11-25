<template>
  <div>
    <!-- 교사 navbar -->
    <div v-if="flag && currentUser.userflag" class="jooa-font">
      <div class="navBar q-px-xl q-py-md bord-bt">
      <a href="/educolab"><img src="@/assets/educolab.png" alt="educolab" style="width: 4rem; height: 4rem"/></a>
        <div class="navBarUi nav-size">
          <div class="row justify-end">
            <div class="row items-center">
              <router-link class="q-ml-xl button color5 navBarLi" to="/notice">공지사항</router-link>
              <router-link class="q-ml-xl button color5 navBarLi" to="/teacher/task">과제</router-link>
              <router-link class="q-ml-xl button color5 navBarLi" to="/quiz">퀴즈</router-link>
              <router-link class="q-ml-xl button color5 navBarLi" to="/survey">설문조사</router-link>
              <router-link class="q-ml-xl button color5 navBarLi" to="/teacher">마이페이지</router-link>
              <a href="/" @click="logoutBtn" class="button color5 q-ml-xl cursor-pointer navBarLi">로그아웃</a>
            </div>
            <div class="row">
              <div class="row justify-end items-center q-ml-xl">
                <img :src="ProImg" style="width:70px; width:70px;">
                <div>
                  <div class="text-bold profil-size">{{ currentUser.name }}</div>
                  <div class="profil-size">{{ currentUser.schoolname }}</div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="navBar_tool">
          <div v-if="onNavList">
            <div @click="activeNav" class="column items-center q-px-md bg-grey-13">
              <router-link class="text-subtitle2 button color5 navBarLi" to="/notice" flat>공지사항</router-link>
              <router-link class="text-subtitle2 button color5 navBarLi" to="/teacher/task" flat >과제</router-link>
              <router-link class="text-subtitle2 button color5 navBarLi" to="/quiz" flat >퀴즈</router-link>
              <router-link class="text-subtitle2 button color5 navBarLi" to="/survey">설문조사</router-link>
              <router-link class="text-subtitle2 button color5 navBarLi" to="/teacher" >마이페이지</router-link>
              <a href="/"  @click="logoutBtn" class=" button text-subtitle2 button color5 cursor-pointer navBarLi">로그아웃</a>
            </div>
          </div>
          <q-icon @click="activeNav" class="cursor-pointer" name="mdi-menu" />
        </div>
      </div>     
    </div>

    <!-- 학생 navbar -->
    <div class="jooa-font" v-if="flag && !currentUser.userflag">
      <div class="navBar q-px-xl q-py-md bord-bt">
      <a href="/educolab"><img src="@/assets/educolab.png" alt="educolab" style="width: 4rem; height: 4rem"/></a>
        <div class="navBarUi nav-size">
          <div class="row justify-end">
            <div class="row items-center">
              <router-link class="q-ml-xl button color5 navBarLi" to="/notice" flat>공지사항</router-link>
              <router-link class="q-ml-xl button color5 navBarLi" to="/student/task" flat >과제</router-link>
              <router-link class="q-ml-xl button color5 navBarLi" to="/student/point" flat >포인트 상점</router-link>
              <router-link class="q-ml-xl button color5 navBarLi" to="/student">마이페이지</router-link>
              <a href="/" @click="logoutBtn" class="q-ml-xl color5 button cursor-pointer navBarLi">로그아웃</a>
            </div>
            <div class="row">
              <div class="row justify-end items-center q-ml-xl">
                <img :src="ProImg" style="width:70px; width:70px;">
                <div>
                  <div class="text-bold profil-size">{{ currentUser.name }}</div>
                  <div class="profil-size">{{ currentUser.schoolname }}</div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="navBar_tool">
          <div v-if="onNavList">
            <div @click="activeNav" class="column items-center q-px-md bg-grey-13">
              <router-link class="text-subtitle2 button color5 navBarLi" to="/notice" flat >공지사항</router-link>
              <router-link class="text-subtitle2 button color5 navBarLi" to="/student/task" flat >과제</router-link>
              <router-link class="text-subtitle2 button color5 navBarLi" to="/student/point" flat >포인트 상점</router-link>
              <router-link class="text-subtitle2 button color5 navBarLi" to="/student" >마이페이지</router-link>
              <a href="/" @click="logoutBtn" class="text-subtitle2 color5 cursor-pointer navBarLi">로그아웃</a>
            </div>
          </div>
          <q-icon @click="activeNav" class="cursor-pointer" name="mdi-menu" />
        </div>
      </div>
    </div>

    <router-view :key="$route.fullPath" />
  </div>
</template>

<style>
/* 모든 페이지에서 공통으로 사용할 스타일 정의 */

/* 폰트 적용 */
@font-face {
  font-family: "jooa";
  src: url("@/assets/fonts/BMJUA_ttf.ttf");
}

.jooa-font {
  font-family: "jooa";
}

.navBar {
  display: flex;
  flex-direction: row;
}

/* 컴포넌트 기본 css */
.baseStyle {
  width: 80%;
  margin: auto;
  min-width: 450px;
  height: 1200px;
}
.surveyStyle {
  width: 80%;
  margin: auto;
  min-width: 450px;
  height: 1200px;
}
.navBarUi {
  display: flex;
  flex-direction: row;
  align-items: center;
}
.nav-size {
  font-size: 1.3rem;
}

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
.bord-bt {
  border-bottom: 1px solid #99dff9;
}
.bord-top {
  border-top: 1px solid #99dff9;
}
.color1 {
  color: #ff9966;
}
.color2 {
  color: #8bff8b;
}
.color3 {
  color: #ffc000;
}
.color4 {
  color: #99dff9;
}
.color5 {
  color: black;
}

.ftr-size {
  font-size: 0.9rem;
}
.navBarLi:hover {
  border-bottom: 2px solid #8bff8b;
}
.navBar_tool {
  position: absolute;
  right: 32px;
  font-size: 2rem;
  color: #ff9966;
  display: none;
}
.profil-size {
  font-size: 1rem
}

@media screen and (max-width: 1050px) {
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
.active {
  color: #5097de;
}
.red {
  color: red;
}
</style>

<script>
import { mapGetters, mapActions } from "vuex";
import drf from '@/api/drf.js'

export default {
  // components: { TheSpinner },
  name: "MainPage",
  data() {
    return {
      isHovering: true,
      onNavList: false,
    };
  },
  computed: {
    ...mapGetters(["isLoggedIn", "currentUser"]),
    flag() {
      if (this.isLoggedIn) return true;
      return false;
    },
    ProImg() {
      return drf.file.path() + this.currentUser.profil
    }
  },
  methods: {
    ...mapActions(["logout", "currentingUser"]),
    logoutBtn() {
      if (this.isLoggedIn) {
        this.logout();
      } else {
        this.$router.back();
      }
    },
    selectedHovering() {
      this.isHovering = true;
    },
    unselectedHovering() {
      this.isHovering = false;
    },
    activeNav() {
      if (this.onNavList == true) {
        this.onNavList = false;
      } else {
        this.onNavList = true;
      }
    },
  },
  created() {
    this.currentingUser()
  },
};
</script>
