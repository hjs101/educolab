import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  // 회원 관리
  {
    path: '/login',
    name: 'login',
    component: () => import ('@/views/LoginView')
  },
  {
    path: '/signup/teacher',
    name: 'signupTeacher',
    component: () => import ('@/views/TeacherSignupView')
  },
  {
    path: '/signup',
    name: 'agree',
    component: () => import ('@/views/SignupAgreeView')
  },
  {
    path: '/nonlogin',
    redirect: {name: 'login'}
  },
  // 404 에러
  {
    path: '/404',
    name: 'NotFound',
    component: () => import ('@/views/NotFoundView')
  },
  // {
  //   path: '*',
  //   redirect: '/404'
  // }

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
