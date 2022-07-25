import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/login',
    name: 'login',
    component: () => import ('@/views/LoginView')
  },
  {
    path: '/signup',
    name: 'agree',
    component: () => import ('@/views/SignupAgreeView')
  },

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
