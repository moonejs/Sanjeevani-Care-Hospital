<script setup>
    import { ref,computed } from 'vue';
    import { useRouter } from 'vue-router';
    import { registerApi } from '@/api/auth';
    import { useToastStore } from '@/stores/toast.store';

    const email =ref("")
    const password=ref("")
    const confirmPassword=ref("")
    const loading=ref(false)
    const router = useRouter()
    const toast = useToastStore()
    
    async function handleRegister(){
        loading.value=true
        try {
            await registerApi({
                email : email.value,
                password : password.value
            })
            toast.addToast({
                message: 'Registerd Succesfully',
                type: 'success'
            })
            router.push('/login')
        } 
        catch (err) {
            console.log(err);
            toast.addToast({
                message: 'Some Error Occurred',
                type: 'error'
            })
        }finally{
            loading.value=false
        }
    }



const passwordMatched = computed(()=>{
    if(!confirmPassword.value) return false;
    return password.value ===confirmPassword.value;
})

const disabled = computed(()=>{
    return !passwordMatched.value || !email.value || loading.value
})

function canRegister(){
    if (!passwordMatched.value) return;
    handleRegister();
    
}


</script>

<template>
    <div class="container-fluid vh-100 p-0 d-flex gap-9 overflow-hidden">
        <div class="w-50 h-100">
            <div id="carouselExampleAutoplaying" class="carousel slide" data-bs-ride="carousel">
                <div class="carousel-inner">
                    <div class="carousel-item active bg-info-subtle pb-7">
                        <img src="../../assets/images/img-1.png" height="500rem" class="mt-8 d-block w-100 object-fit-contain" alt="...">
                    </div>
                    <div class="carousel-item bg-danger-subtle pb-7">
                        <img src="../../assets/images/img-9.png" height="500rem" class="mt-8 d-block w-100 object-fit-contain" alt="...">
                    </div>
                    <div class="carousel-item bg-dark-subtle pb-7">
                        <img src="../../assets/images/img-10.png" height="500rem" class="mt-8 d-block w-100 object-fit-contain" alt="...">
                    </div>
                </div>
                <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleAutoplaying" data-bs-slide="prev">
                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Previous</span>
                </button>
                <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleAutoplaying" data-bs-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Next</span>
                </button>
            </div>
        </div>
        <div class="mt-3 border-top border-start">
            <div class="p-4">
                <div class="border-0 text-center pb-0">
                    <h2 class="h4 fw-bolder fs-3">Register</h2>
                </div>
                <div class="card-body">
                    <form @submit.prevent="canRegister">
                        <div class="form-group mb-4">
                            <label for="exampleInputEmailCard1">Your Email</label>
                            <div class="input-group">
                                <span class="input-group-text" id="basic-addon1"><span class="fas fa-envelope"></span></span>
                                <input type="email" class="form-control" placeholder="example@company.com" v-model.trim="email" required id="exampleInputEmailCard1" aria-describedby="exampleInputEmailCard1">
                            </div>
                        </div>
                        <div class="form-group mb-4">
                            <label for="exampleInputPasswordCard1">Your Password</label>
                            <div class="input-group">
                                <span class="input-group-text" id="basic-addon2"><span class="fas fa-unlock-alt"></span></span>
                                <input required type="password" v-model.trim="password" placeholder="Password" class="form-control" id="exampleInputPasswordCard1" aria-describedby="exampleInputPasswordCard1">
                            </div>
                        </div>
                        <div class="form-group mb-4">
                            <label for="exampleInputPasswordCard2">Confirm Password</label>
                            <div class="input-group">
                                <span class="input-group-text" id="basic-addon2"><span class="fas fa-unlock-alt"></span></span>
                                <input required type="password" v-model.trim="confirmPassword" placeholder="Confirm Password" class="form-control" :class="{ 'is-valid': confirmPassword && passwordMatched, 'is-invalid': confirmPassword && !passwordMatched }" id="exampleInputPasswordCard2">
                                <div class="valid-feedback">Passwords match</div>
                                <div class="invalid-feedback">Passwords do not match</div>
                            </div>
                        </div>
                        <div class="d-grid">
                            <button type="submit" :disabled="disabled" class="btn btn-primary">
                                <span v-if="loading">
                                    <span class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span>
                                    <span class="ml-1">Registering...</span>
                                </span>
                                <span v-else>Register</span>
                            </button>
                        </div>
                    </form>
                    <div class="mt-3 mb-4 text-center">
                        <span class="fw-normal">or Register with</span>
                    </div>
                    <div class="btn-wrapper my-4 text-center">
                        <button class="btn btn-icon-only btn-pill btn-outline-light text-google me-2 bg-primary-subtle">
                            <span aria-hidden="true" class="fab fa-google"></span>
                        </button>
                        <button class="btn btn-icon-only btn-pill btn-outline-light text-github bg-primary-subtle">
                            <span aria-hidden="true" class="fab fa-github"></span>
                        </button>
                    </div>
                    <div class="d-block d-sm-flex justify-content-center align-items-center mt-4">
                        <span class="fw-normal">
                            Already registered? <RouterLink to="/login" class="text-info text-underline">Login here</RouterLink>
                        </span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
