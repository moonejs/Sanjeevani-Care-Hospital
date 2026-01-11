import { ref, computed ,watch} from 'vue'
import { defineStore } from 'pinia'
import { loginApi,currentUserApi,logoutApi } from '@/api/auth'


export const useAuthStore = defineStore('auth', () => {
  const token = ref(localStorage.getItem('token'))
  const user=ref(null)
  const role=ref(null)
  const profileCompleted=ref(false)

  async function login(data){
    
      const res = await loginApi(data)
      console.log(res);
      token.value = res.data.response.user.authentication_token

      localStorage.setItem('token',token.value)

      await fetchMe()

  }
  async function fetchMe(){
    if(!token.value) return

    const userData = await currentUserApi()
    user.value=userData.data;
    role.value=user.value.roles[0];
    profileCompleted.value=user.value.profile_completed
    
  }

  async function logout(){
    await logoutApi()
    token.value = null
    user.value = null
    role.value = null
    
    localStorage.removeItem('token')
    
    console.log("logout");
    
  
  }

   watch(token,(newToken)=>{
    if(!newToken){
      user.value=null
      role.value=null
    }
  })
  const isAuthenticated = computed(()=> !!token.value)

  return{
    token,
    user,
    role,
    login,
    isAuthenticated,
    logout,
    fetchMe,
    profileCompleted
  }
})
