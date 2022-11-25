<template>
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e6b54fb (asdu)
  <div class="q-px-xl">
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
