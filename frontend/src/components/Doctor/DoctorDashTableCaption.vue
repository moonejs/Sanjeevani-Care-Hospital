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
    <div class="d-flex align-items-center justify-content-between">
        <h1>{{ title }}</h1>
        <div v-if="stats=='title'">
            <TableStats :table-stats="tableStatsArr" />
        </div>
    </div>
    <div class="d-flex align-items-center " v-if="stats=='navs'">
        <div >
            <TableNavigaionBox @today-or-week="(value) => emit('todayOrWeek', value)"/>
        </div>
        <div >
            <TableStats :table-stats="tableStatsArr" />
        </div>
    </div>
 
</template>