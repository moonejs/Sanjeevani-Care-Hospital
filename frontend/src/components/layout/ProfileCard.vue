<script setup>
    defineProps({
        label:String
    })
    const emit = defineEmits(['select'])
</script>

<template>
    <div class=" custom-card bg-info round d-flex justify-content-center align-items-center animate-up-2" @click="emit('select')" >
        <div class="">
            <i class="fa-solid fa-heart-pulse "></i>
            <h5 class="text-center">{{ label }}</h5>
        </div>
    </div>
    
</template>