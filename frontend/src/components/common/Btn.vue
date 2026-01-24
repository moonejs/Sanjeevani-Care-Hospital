<script setup>
    defineProps({
        type:String,
        label:String,
        disabled:Boolean
    })
    const emit=defineEmits(['click'])
</script>
<template>
    <button  class="btn " :disabled="disabled" :type="type" @click="emit('click')">{{ label }}</button>
</template>