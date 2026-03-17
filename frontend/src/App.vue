<script setup>
import {RouterView } from 'vue-router';
import { useAuthStore } from './stores/auth.store';
import { onMounted } from 'vue';
import AppToast from './components/common/AppToast.vue';
const auth=useAuthStore();

// onMounted(async()=>{
//   console.log("onMounted");
  
//   if(auth.token){
//     try {
//       await auth.fetchMe()
//     } catch (error) {
//       auth.logout()
//     }
//   }
// })

</script>

<template>
  <RouterView/>
  <AppToast/>
</template>
