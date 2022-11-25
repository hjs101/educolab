<template>
  <q-card class="q-pa-md row">
    <h6 class="text-center col-12">내 정보</h6>
    <q-card-section horizontal class="q-ml-sm">
      <!-- 프로필 -->
      <label for="profil">
        <img :src="profil.change" class="cursor-pointer" width="100" />
      </label>
      <input
        type="file"
        class="hidden"
        id="profil"
        @input="changeProfil"
        accept="image/gif, image/jpeg, image/png"
      />
      <!-- 배지-->
      <div v-if="!info.userflag">
        <q-icon
          v-if="!info.wear_icon"
          name="mdi-plus-circle-outline"
          size="50px"
          color="grey-13"
          @click="myTitle(false)"
          class="cursor-pointer"
        />
        <img
          v-else
          :src="badge.change"
          class="cursor-pointer"
          @click="myTitle(false)"
          width="50">
        <q-btn
          v-if="!info.userflag"
          color="black"
          class="text-bold text-size d-inline"
          flat @click="myTitle(true)"
          :label="computedTitle" />
      </div>
      <q-separator />
        <q-card-section class="q-ml-md">
        <span>
          아이디 <b class="text-size"> {{info.username}} </b>
          생년월일 <b class="text-size">{{birthday}}</b>
          <span v-if="info.userflag">
            담당과목 <b class="text-size">{{info.subject}}</b>
          </span>
          <br>
          <br>
          학교 <b class="text-size">{{school}}</b>
        </span>
        <span v-if="!info.userflag || info.homeroom_teacher_flag">
          <span>&nbsp;{{info.userflag? '담당 반':'학년/반'}}</span>
          <b class="text-size">
            &nbsp;{{info.grade}}학년  {{info.class_field}}반
          </b>
        </span>
        <br>
        <br>
        <span v-if="!info.userflag">
          현재(누적) 상점/벌점 &nbsp; <b class="text-size">+{{info.plus_point}} ({{info.acc_point}}) / {{info.minus_point}}</b>
        </span>
      </q-card-section>
    </q-card-section>

    <q-separator />
      
    <q-card-actions class="col-12">
      <q-btn flat @click="deleteProfil">프로필 삭제</q-btn>
      <q-btn color="primary" flat @click="toChangePage('info')">
        정보 수정
      </q-btn>
      <q-btn color="primary" flat @click="toChangePage('password')">
        비밀번호 변경
      </q-btn>
    </q-card-actions>
    <!-- 업적/칭호 적용 창 -->
    <my-page-pop-up
      v-if="apply.mode && !info.userflag"
      :title="apply.title"
      :changeMode="false"
      :type="type"
      :titles="info.own_title"
      :icons="info.own_icon"
      @reverse="applyTitle"
    />
  </q-card>
</template>

<script>
import { useStore } from "vuex";
import { computed, reactive, ref } from "vue";
import { useRouter } from "vue-router";
import dayjs from "dayjs";
import axios from "axios";
import drf from "@/api/drf.js";
import MyPagePopUp from "@/components/MyPagePopUp.vue";
export default {
  name: "MyInfo",
  components: {
    MyPagePopUp,
  },
  props: {
    info: Object,
  },
  setup(props) {
    const store = useStore();
    const router = useRouter();
    const school = store.getters.currentUser.schoolname;
    let title = ref(props.info.wear_title?.title);
    let icon = ref(props.info.wear_icon?.title);
    let computedTitle = computed(() => title.value);
    const date = dayjs(props.info.birthday);
    const birthday = `${date.get("y")}년 ${date.get("M") + 1}월 ${date.get(
      "D"
    )}일생`;
    const profil = reactive({
      path: props.info.profil,
      change: computed(() => drf.file.path() + profil.path),
    });
    const badge = reactive({
      path: props.info.wear_icon?.icon,
      change: computed(() => drf.file.path() + badge.path),
    });
    let files = null;
    const apply = reactive({
      prompt: false,
      title: null,
      mode: computed(() => apply.prompt),
    });
    let type = ref(null);
    const myTitle = (title) => {
      type.value = title;
      apply.title = title ? "보유 업적 목록" : "보유 배지 목록";
      apply.prompt = true;
    };
    const applyTitle = (val, type, pk, name, path) => {
      if (val && name !== title.value ) {
        let url = null
        if (type) {
          url = drf.myPage.changeTitle()
        } else {
          url = drf.myPage.changeIcon();
        }
        axios({
          url,
          method: "put",
          headers: store.getters.authHeader,
          data: {pk,}
        })
          .then(() => {
            if (props.type) {
              title.value = name
            } else {
              icon.value = name
              badge.path = path
            }
            router.go()
          })
      }
      apply.prompt = false;
    };
    const changeProfil = () => {
      // 자세한 건 수정 필요
      const photo = document.getElementById("profil");
      const form = new FormData();
      form.append("profil", photo.files[0]);
      axios({
        url: drf.myPage.changeProfil(),
        method: "put",
        headers: {
          ...store.getters.authHeader,
          "Content-Type": "multipart/form-data",
        },
        data: form,
      }).then(() => {
        profil.path = drf.file.change() + photo.files[0].name;
      });
    };
    const deleteProfil = () => {
      axios({
        url: drf.myPage.changeProfil(),
        method: "delete",
        headers: store.getters.authHeader,
      }).then(() => {
        profil.path = drf.file.default();
      });
    };
    const toChangePage = (path) => {
      if (path === "password") {
        store.dispatch("changePwInfo", {
          name: props.info.name,
          email: props.info.email,
          username: props.info.username,
        });
        router.push("/change/password");
      } else {
        store.dispatch("changeInfo", props.info);
        router.push("/change/info");
      }
    };
    return {
      school,
      apply,
      title,
      icon,
      type,
      birthday,
      files,
      profil,
      badge,
      myTitle,
      applyTitle,
      changeProfil,
      deleteProfil,
      toChangePage,
      computedTitle,
    };
  },
};
</script>

<style scoped>
  .text-size{font-size: 1rem;}
  .searchWrap{border-radius:5px; text-align:center; padding:20px 0; margin-bottom:10px;}
  .tbList th{border-top:1px solid #888;}
	.tbList th, .tbList td{border-bottom:1px solid #eee; padding:5px 0;}
	.tbList td.txt_left{text-align:left;}
  .btn{margin-bottom:40px;}
</style>