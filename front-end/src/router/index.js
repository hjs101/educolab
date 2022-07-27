import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  // 회원 관리
  {
    path: '/login',
    name: 'login',
    component: () => import ('@/views/LoginView')
  },
  {
    path: '/signup/student',
    name: 'signupStudent',
    component: () => import ('@/views/SignupView')
  },
  {
    path: '/signup/teacher',
    name: 'signupTeacher',
    component: () => import ('@/views/SignupView')
  },
  {
    path: '/signup/*',
    redirect: {name: 'NotFound'}
  },
  // signup 뒤에 student, teacher 아닌 것이 있으면 404 에러
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
