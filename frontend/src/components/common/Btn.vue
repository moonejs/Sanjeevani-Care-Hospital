<script setup>
    defineProps({
        type:String,
        label:String
    })
    const emit=defineEmits(['click'])
</script>
<template>
    <button  class="btn btn-tertiary" :type="type" @click="emit('click')">{{ label }}</button>
</template>