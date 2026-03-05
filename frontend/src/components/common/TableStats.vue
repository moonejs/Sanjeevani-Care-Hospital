<script setup>
    defineProps({
        tableStats:Array
    })
</script>

<template>
    <div v-for="(stat, i) in tableStats" :key="i" class="d-flex gap-3">
        <div v-for="(value, label) in stat" :key="label" class="stat-item text-end">
            <span class="text-muted d-block small-label text-uppercase">{{ label }}</span>
            <span class="fw-bold h6 m-0">{{ value }}</span>
        </div>
    </div>
</template>

