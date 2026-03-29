<script setup>
    const props=defineProps({
        label:String,
        route:String
    })
</script>
<template>
    <RouterLink class="btn list-group-item rounded-0 " active-class="active" :to="`${route}`">{{ label}}</RouterLink>

</template>