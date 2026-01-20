<script setup>
    defineProps({
        tableStats:Array
    })
</script>
<template>
    <div v-for="(stat,i) in tableStats" :key="i" class="d-flex ">
        <div v-for="(value, label) in stat" :key="label" class="m-2">
            <h6 class="text-muted d-inline">{{ label }} : </h6>
            <h6 class="fw-bold d-inline">{{ value }}</h6>
        </div>
    </div>
    
    
</template>