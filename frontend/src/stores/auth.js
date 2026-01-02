import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { loginApi,currentUserApi,logoutApi } from '@/api/auth'
import { useRouter } from 'vue-router'

export const useAuthStore = defineStore('auth', () => {
  const token = ref(localStorage.getItem('token'))
  const user=ref(null)
  const role=ref(null)

  const router=useRouter()


  async function login(data){
    
      const res = await loginApi(data)
      console.log(res);
      token.value = res.data.response.user.authentication_token
      console.log(token.value);
      

      localStorage.setItem('token',token.value)

      await fetchMe()

  }
  async function fetchMe(){
    if(!token.value) return

    const userData = await currentUserApi()
    user.value=userData.data;
    role.value=user.value.roles[0];
  }

  async function logout(){
    await logoutApi()
    token.value = null
    user.value = null
    role.value = null
    
    localStorage.removeItem('token')
    router.replace('/')
    console.log("logout");
    
  }

  const isAuthenticated = computed(()=> !!token.value)

  return{
    token,
    user,
    role,
    login,
    isAuthenticated,
    logout,
    fetchMe
  }
})
