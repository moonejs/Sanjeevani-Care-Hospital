<script setup>
    defineProps({
        navArray:Array
    })
</script>
<template>
    <div class="nav nav-tabs">
        <li class="nav-item" v-for="(nav,i) in navArray" :key="i">
            <h3 class="bg-danger me-3 p-1">{{ nav }}</h3>
        </li>
        
    </div>
</template>