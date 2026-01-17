<script setup>
    defineProps({
        tableStats:Array
    })
</script>
<template>
    <div>
        <div v-for="(stat,i) in tableStats" :key="i">
            <div v-for="(value, label) in stat" :key="label">
                <h6 class="text-muted d-inline">{{ label }} : </h6>
                <h6 class="fw-bold d-inline">{{ value }}</h6>
            </div>
        </div>
    </div>
</template>