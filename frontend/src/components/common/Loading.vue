<script setup>
    defineProps({
        loading:Boolean
    })
</script>
<template>
    <div v-if="loading" class="spinner-border" role="status">
        
    </div>
</template>

