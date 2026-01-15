<script setup>
    defineProps({
        label:String,
        color:String
    })
</script>

<template>
    <span class="badge" :class="`text-bg-${color}`" >{{ label }}</span>
</template>