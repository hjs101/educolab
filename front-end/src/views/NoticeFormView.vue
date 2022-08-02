<template>
  <div class="q-px-xl">
    <h1>공지 작성,수정 페이지</h1>

    <q-form @submit="submitNotice">

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

      <!-- <div class="q-gutter-lg row">
        <span class="q-py-md" style="width: 70px; text-align:center">파일첨부</span>
        <div class="custom-file">
            <input id="customFile" type="file" @change="handleFileChange"/>
            <label class="custom-file-label" for="customFile">{{file_name}}</label>
        </div>
      </div> -->
      <input type="file" @change="onFileSelected">
      <hr>

      <button @click="submitNotice(credentials)">등록</button>

    </q-form>

    <hr>
  <router-view />
  </div>
</template>

<script>
import {ref} from 'vue'
import { mapActions } from 'vuex'

export default {
  data() {
    return {
      credentials : {
        classification : '',
        title : '',
        content : '',
        // files : '',
      }
    }
  },
  setup() {
    return {
      content: ref(''),
      title : ref(''),
      classification: ref(null),
      options: [
        '공지', '변경', '행사'
      ],
      // files : ref(null)
    }    
  },
  methods: {
    ...mapActions(['submitNotice']),
    // onFileSelected(event) {
    //   this.credentials.files = event.target.files[0]
    // }
  }
}
</script>