<script setup>
    defineProps({
        loading:Boolean
    })
</script>
<template>
    <div v-if="loading" class=" spinner-border text-primary " role="status">
        
    </div>
</template>

