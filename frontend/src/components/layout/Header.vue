<script setup>
    defineProps({
        label:String
    })
</script>

<template>
    <div class="bg-success patient-header pt-5 ps-5">
        <h1>{{ label }}</h1>
    </div>
</template>