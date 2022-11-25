<<<<<<< HEAD
<<<<<<< HEAD
=======
import './plugins/axios'
>>>>>>> 1f63946 (vue 환경셋팅)
=======
>>>>>>> b1d70e4 (edit vue settings)
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
<<<<<<< HEAD
import { Quasar } from 'quasar'
import quasarUserOptions from './quasar-user-options'

createApp(App).use(Quasar, quasarUserOptions).use(store).use(router).mount('#app')
=======

createApp(App).use(store).use(router).mount('#app')
>>>>>>> 1f63946 (vue 환경셋팅)
