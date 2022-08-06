<template>
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e6b54fb (asdu)
  <div class="q-px-xl">
    <h1>공지 작성,수정 페이지</h1>
    <!-- {{credentials.classification}}
    <br>
    {{noticePk}} -->
    <br>
    <!-- {{noticeItem.notice.classification}} -->
=======
  <div class="q-px-xl">
    <h1>공지 작성,수정 페이지</h1>
    {{credentials.classification}}
    <br>
    {{noticePk}}
    <br>
    {{noticeItem.notice.classification}}
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
    <q-form v-if="!noticePk || noticeItem.notice">

      <div class="q-gutter-lg row">
        <span class="q-py-md" style="width: 70px; text-align:center">분류 </span>
        <div style="width: 300px">
          <div class="q-gutter-md">
            <q-select outlined v-model="credentials.classification" label="classification" :options="options" required/>
          </div>
        </div>
      </div>

      <hr>

      <div class="q-gutter-lg row">
        <span class="q-py-md" style="width: 70px; text-align:center">제목</span>
        <q-input outlined v-model="credentials.title" label="title" style="width: 500px;" required/>
      </div>

      <hr>

      <div class="q-gutter-lg row">
        <span class="q-py-md" style="width: 70px; text-align:center">내용</span>
        <div class="q-pa-md q-gutter-sm" style="width:500px; margin:0;">
          <q-editor
            v-model="credentials.content"
            label="content"
            :definitions="{
              bold: {label: 'Bold', icon: null, tip: 'My bold tooltip'}
            }"
          required/>
        </div>
      </div>

      <hr>

      <input type="file" multiple @change="onFileSelected">
      <hr>

      <button 
<<<<<<< HEAD
      @click.self.prevent="submitNotice(info)">
=======
      @click.self.prevent="index !== undefined ? submitNotice(credentials) : updateNotice(credentials) ">
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
      등록</button>
  
      <!-- {{ index !== undefined ? '작성' : '수정'}}</button> -->
      <!-- <button @click.self.prevent="submitNotice(info)">등록</button> -->
    </q-form>
    <hr>
    <h1>{{ noticePk }}</h1>
  <router-view />
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  computed : {
  ...mapGetters(['noticeItem'])
  },
  data() {
    // const noticePk = this.$route.params.noticePk
    return {
      noticePk : this.$route.params.noticePk,
      credentials : {
        classification : "",
        title : this.noticePk ? this.noticeItem.notice.title : "",
        content : this.noticePk !== undefined ? this.noticeItem?.notice.content : "",
        files : this.noticePk !== undefined ? this.noticeItem?.files : "",
      },
      info : null,
      options: [
        '공지', '변경', '행사'
      ],
    }
  },

  methods: {
<<<<<<< HEAD
    ...mapActions(['submitNotice']),
=======
    ...mapActions(['submitNotice',]),
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
    onFileSelected(event) {
      this.credentials.files = event.target.files
      console.log(this.credentials.files)
      this.info = new FormData()
      console.log(this.credentials.files.length)
      for(let i=0; i<this.credentials.files.length;i++){
        this.info.append('files',this.credentials.files[i])
      }
      this.info.append('classification',this.credentials.classification);
      this.info.append('title',this.credentials.title);
      this.info.append('content',this.credentials.content);
    }
  },
  created() {
    this.noticeItem
  }
}
<<<<<<< HEAD
<<<<<<< HEAD
</script>
=======
  <div>
=======
  <div class="q-px-xl">
>>>>>>> b22ae6e (공지사항 메인 페이지)
    <h1>공지 작성,수정 페이지</h1>

    <div class="q-gutter-lg row">
      <span class="q-py-md" style="width: 70px; text-align:center">분류 </span>
      <div style="width: 300px">
        <div class="q-gutter-md">
          <q-select outlined v-model="model" :options="options" />
        </div>
      </div>
    </div>

    <hr>

    <div class="q-gutter-lg row">
      <span class="q-py-md" style="width: 70px; text-align:center">제목</span>
      <q-input outlined v-model="text" style="width: 500px;"/>
    </div>

    <hr>

    <div class="q-gutter-lg row">
      <span class="q-py-md" style="width: 70px; text-align:center">내용</span>
      <div class="q-pa-md q-gutter-sm" style="width:500px; margin:0;">
        <q-editor
          v-model="editor"
          :definitions="{
            bold: {label: 'Bold', icon: null, tip: 'My bold tooltip'}
          }"
        />
      </div>
    </div>

    <hr>

    <div class="q-gutter-lg row">
      <span class="q-py-md" style="width: 70px; text-align:center">파일첨부</span>
      <div class="custom-file">
          <input id="customFile" type="file" @change="handleFileChange"/>
          <label class="custom-file-label" for="customFile">{{file_name}}</label>
      </div>
    </div>

    <hr>
    <button>등록</button>
  <router-view />
  </div>
</template>
<<<<<<< HEAD
>>>>>>> e66f000 (navbar 생성)
=======

<script>
import {ref} from 'vue'

export default {
  setup() {
    return {
      model: ref(null),
      options: [
        '공지', '변경', '행사'
      ]
    }    
  },
}
</script>
>>>>>>> b22ae6e (공지사항 메인 페이지)
=======
</script>
>>>>>>> e6b54fb (asdu)
=======
</script>
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
