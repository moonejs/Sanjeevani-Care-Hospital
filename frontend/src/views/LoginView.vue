<script setup>
    import { ref } from 'vue';
    import { loginApi } from '@/api/auth';
    import { useRouter } from 'vue-router';

    const email =ref("")
    const password=ref("")
    const loading=ref(false)
    const router = useRouter()

    async function handleLogin(){
        loading.value=true
        
        try{
            const res = await loginApi({
                email : email.value,
                password : password.value
            })
            console.log(res);
            const token = res.data.response.user.authentication_token

            localStorage.setItem('token',token)
            router.replace('/dashboard')
        }
        catch(err){
            console.log(err);
        }
        finally{
            loading.value=false
        }

    }
</script>

<template>
    <div class="container-fluid vh-100 p-0  d-flex">
        <div class=" w-50 h-100">
           ddfdf 
        </div>
        <div class="mt-5">
            <div class="card p-4">
                <div class="card-header border-0 bg-white text-center pb-0">
                    <h2 class="h4 fw-bolder fs-3">Login</h2>
                </div>
                <div class="card-body">
                    <form @submit.prevent="handleLogin">
                        <div class="form-group mb-4">
                            <label for="exampleInputEmailCard1">Your Email</label>
                            <div class="input-group">
                                <span class="input-group-text" id="basic-addon1"><span class="fas fa-envelope"></span></span>
                                <input type="email" class="form-control" placeholder="example@company.com" v-model="email"
                                required id="exampleInputEmailCard1" aria-describedby="exampleInputEmailCard1"  >
                            </div>
                        </div>
                        <div class="form-group mb-4">
                            <label for="exampleInputPasswordCard1">Your Password</label>
                            <div class="input-group">
                                <span class="input-group-text" id="basic-addon2"><span class="fas fa-unlock-alt"></span></span>
                                <input required type="password" 
                                v-model="password"
                                placeholder="Password" class="form-control" id="exampleInputPasswordCard1" aria-describedby="exampleInputPasswordCard1"/>
                            </div>
                        </div>
                        <div class="d-grid">
                            <button type="submit"  :disabled="loading" class="btn btn-primary">
                                <span v-if="loading">
                                    <span class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span>
                                    <span class="ml-1">Loging...</span>
                                </span>
                                <span v-else>
                                    Login
                                </span>
                            </button>
                        </div>
                    </form>
                    <div class="mt-3 mb-4 text-center">
                        <span class="fw-normal">or Sign up with</span>
                    </div>
                    <div class="btn-wrapper my-4 text-center">
                        <button class="btn btn-icon-only btn-pill btn-outline-light text-google me-2  bg-primary-subtle">
                            <span aria-hidden="true" class="fab fa-google"></span>
                        </button>
                        
                        <button class="btn btn-icon-only btn-pill btn-outline-light text-github bg-primary-subtle" 
                        >
                            <span aria-hidden="true" class="fab fa-github"></span>
                        </button>
                    </div>
                        <div class="d-block d-sm-flex justify-content-center align-items-center mt-4">
                        <span Name="fw-normal">
                            Not registered?
                            
                        </span>
                    </div>
                </div>
            </div>
        </div>
        
    </div>

</template>
