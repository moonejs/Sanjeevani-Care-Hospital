<script setup>
    const props=defineProps({
        label:String,
        route:String
    })
</script>
<template>
    <RouterLink class="btn list-group-item " active-class="active" :to="`${route}`">{{ label}}</RouterLink>

</template>