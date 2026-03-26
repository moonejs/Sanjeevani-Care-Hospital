<script setup>
    defineProps({
        label:String,
        stats:Number
    })
</script>
<template>
    <div class="v rounded-start-1 count-card pt-2 animate-right-3 ">
        <h6 class="text-center text-muted pt-1 small">Total {{ label }}</h6>
        <h4 class="text-center">{{ stats || 0 }}</h4>
        
    </div>
</template>
<style scoped>
.v{
    background-color: #F0F2F4;
    border-left: 4px solid #151616;
}
</style>

