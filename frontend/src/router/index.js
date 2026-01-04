import { createRouter, createWebHistory } from 'vue-router'
import LandingPage from '@/views/LandingPage.vue'
import { useAuthStore } from '@/stores/auth'

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
      path:'/admin',
      name:'admin',
      component:()=> import('@/views/AdminDashboardPage.vue'),
      meta: { role: 'admin' }
    }
    ,{
      path:'/doctor',
      name:'doctor',
      component:()=> import('@/views/DoctorDashboardPage.vue'),
       meta: {role: 'doctor' }
    },
    {
      path:'/:pathMatch(.*)*',
      name:'NotFound',
      component:()=> import('@/views/NotFoundPage.vue')
    }
  ],
})

router.beforeEach(async(to,from)=>{
  const auth=useAuthStore()

  

  if(to.name!=='login' && !auth.isAuthenticated){
    return { name: 'login' }
  }

   if (auth.isAuthenticated && !auth.role) {
    try {
      await auth.fetchMe()
    } catch {
      auth.logout()
      return { name: 'login' }
    }
  }
  if(auth.isAuthenticated && to.name == 'login'){
    if(auth.role=='doctor') return {name : 'doctor'}
    if(auth.role=='admin') return {name : 'admin'}
  }

  if(to.meta.role && auth.role!==to.meta.role){
    if(auth.role=='doctor') return {name : 'doctor'}
    if(auth.role=='admin') return {name : 'admin'}
  }

})

export default router
