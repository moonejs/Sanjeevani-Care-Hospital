<script setup>
    defineProps({
        label:String,
        stats:Number
    })
</script>
<template>
    <div class="card rounded-0 count-card">
        <h4>Total {{ label }}</h4>
        <h4 class="text-center">{{ stats || 0 }}</h4>
        
    </div>
</template>

