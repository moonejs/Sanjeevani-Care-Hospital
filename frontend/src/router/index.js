import { createRouter, createWebHistory } from 'vue-router'
import LandingPage from '@/views/LandingPage.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'LandingPage',
      component: LandingPage,
    },
    {
      path: '/login',
      name: 'login',
      component:()=> import('@/views/LoginView.vue')
    },
    {
      path: '/register',
      name:'register',
      component:()=> import('@/views/RegisterPage.vue')
    },
    {
      path:'/dashboard',
      name:'dashboard',
      component:()=> import('@/views/DashboardPage.vue')
    }
  ],
})

export default router
