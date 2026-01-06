import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores/auth'


import publicRoutes from './public.routes'
import authRoutes from './auth.routes'
import adminRoutes from './admin.routes'
import doctorRoutes from './doctor.routes'
import patientRoutes from './patient.routes'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    ...publicRoutes,
    ...authRoutes,
    ...adminRoutes,
    ...doctorRoutes,
    ...patientRoutes
  ],
})

router.beforeEach(async(to,from)=>{
  const auth=useAuthStore() 

  if(!['login', 'register'].includes(to.name) && !auth.isAuthenticated && to.name!=='register'){
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
    if(auth.role=='patient') return {name : 'patient'}
  }

  if(to.meta.role && auth.role!==to.meta.role){
    if(auth.role=='doctor') return {name : 'doctor'}
    if(auth.role=='admin') return {name : 'admin'}
    if(auth.role=='patient') return {name : 'patient'}
  }


  // patients

  if(auth.role=='patient' && !auth.profileCompleted){
    console.log("dd"+auth.profileCompleted);
    
    if(to.name !='patient-profile'){
      return {name:'patient-profile'}
    }
  }

})

export default router
