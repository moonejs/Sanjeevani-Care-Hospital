<script setup>
    defineProps({
        label:String
    })
</script>

<template>
    <div class="table-top-box bg-info d-flex justify-content-center align-items-center">
        <h2>{{ label }}</h2>
    </div>
</template>