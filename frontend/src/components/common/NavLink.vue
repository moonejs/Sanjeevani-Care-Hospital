<script setup>
    import { RouterLink } from 'vue-router';
    defineProps({
        label:{
            type:String,
            required:true
        },
        route:{
            type:String,
            required:true
        },
        
    })
</script>
<template>
  <RouterLink class="nav-link px-3 "active-class="active-link" :to="route">
    {{ label }}
  </RouterLink>
</template>

<style scoped>
.custom-link {
  color: #495057;
  font-weight: 500;
  border-radius: 3px;
  padding: 6px 12px;
  transition: all 0.2s ease;
}

.nav-link:hover {
  background-color: #f1f3f4;
  color: #202124;
}

.active-link {
  background-color: #242E4C;
  color: #FCFDFD !important;
}
</style>