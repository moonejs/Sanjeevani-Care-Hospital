<script setup>
    import TableNavigaionBox from '../common/TableNavigaionBox.vue';
    import TableStats from '../common/TableStats.vue';
   
    defineProps({
        title:String,
        navArray:Array,
        stats:String,
        tableStatsArr:Array
    })
    const emit=defineEmits(['todayOrWeek'])
</script>
<template>
    <div class="d-flex align-items-center justify-content-between mb-3">
        <h5 class="m-0 fw-bold text-dark">{{ title }}</h5>
        
        <div v-if="stats == 'title'" class="d-flex align-items-center">
            <TableStats :table-stats="tableStatsArr" />
        </div>
    </div>

    <div class="d-flex align-items-center justify-content-between border-top pt-2 mt-2" v-if="stats == 'navs'">
        <TableNavigaionBox @today-or-week="(value) => emit('todayOrWeek', value)"/>
        <TableStats :table-stats="tableStatsArr" />
    </div>
</template>

<style scoped>
    h5 {
        letter-spacing: -0.2px;
        font-size: 1.1rem;
    }
</style>