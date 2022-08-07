<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
import './plugins/axios'
>>>>>>> 1f63946 (vue 환경셋팅)
=======
>>>>>>> b1d70e4 (edit vue settings)
=======
>>>>>>> e6b54fb (asdu)
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e6b54fb (asdu)
import { Quasar } from 'quasar'
import quasarUserOptions from './quasar-user-options'

<<<<<<< HEAD
createApp(App).use(Quasar, quasarUserOptions).use(store).use(router).mount('#app')
<<<<<<< HEAD
=======

createApp(App).use(store).use(router).mount('#app')
>>>>>>> 1f63946 (vue 환경셋팅)
=======
import { Quasar } from 'quasar'
import quasarUserOptions from './quasar-user-options'

createApp(App).use(Quasar, quasarUserOptions).use(store).use(router).mount('#app')
>>>>>>> 34b83a2 (Feat : 퀘이사 UI Framework 적용)
=======
>>>>>>> e6b54fb (asdu)
=======
createApp(App)
.use(Quasar, quasarUserOptions)
.use(store)
.use(router)
.mount('#app')
>>>>>>> fa227ef (Feat & Fix : 과제 생성/수정 기능 완료, 나머지 기능 진행 중, 회원 관리 부분 컴포넌트화 및 버그 수정 중)
