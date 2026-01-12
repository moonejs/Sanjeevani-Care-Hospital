<script setup>
    defineProps({
        type:String,
        label:String
    })
</script>
<template>
    <button class="btn btn-tertiary" :type="type">{{ label }}</button>
</template>