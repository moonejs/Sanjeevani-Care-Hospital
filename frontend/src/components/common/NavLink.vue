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
    <RouterLink class="nav-link" active-class="active" :to="`${route}`">{{ label}}</RouterLink>
</template>