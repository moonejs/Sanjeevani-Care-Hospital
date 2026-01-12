<script setup>
    defineProps({
        label:String,
        for:String
    })
</script>
<template>
    <label :for="for">{{ label }}</label>
</template>