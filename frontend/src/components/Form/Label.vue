<script setup>
    defineProps({
        label:String,
        for:String
    })
</script>
<template>
    <label class="form-label" :for="for">{{ label }}</label>
</template>