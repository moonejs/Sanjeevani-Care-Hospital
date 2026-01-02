<script setup>
import {RouterView } from 'vue-router';
import { useAuthStore } from './stores/auth';
import { onMounted } from 'vue';

const auth=useAuthStore();

onMounted(async()=>{
  console.log("onMounted");
  
  if(auth.isAuthenticated){
    try {
      await auth.fetchMe()
    } catch (error) {
      auth.logout()
    }
  }
})

</script>

<template>
  <RouterView/>
</template>
