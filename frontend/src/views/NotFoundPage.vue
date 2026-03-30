<script setup>
import { DotLottieVue } from '@lottiefiles/dotlottie-vue'
import Btn from '@/components/common/Btn.vue';
import { useRouter } from 'vue-router';
const router=useRouter()

function home(){
    router.push('/login')
}
</script>

<template>
    


  <DotLottieVue class="ms-12 position-absolute top-1 " style="height: 400px; width: 800px;" autoplay loop src="https://lottie.host/9001aad7-3141-4dae-843d-47a8380c2d60/I4tsphjsaQ.lottie" />

  <div class="position-absolute left-12 ms-9 mt-5 top-12">
      <h4 class="text-muted">OOPS!! I am Sleeping  Don't distrub me</h4>
      <Btn label="Home" class="btn-outline-secondary ms-9 mt-2 px-4" @click="home"/>
    </div>

</template>