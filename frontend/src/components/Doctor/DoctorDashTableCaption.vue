<script setup>
    import TableNavigaionBox from '../common/TableNavigaionBox.vue';
    import TableStats from '../common/TableStats.vue';
   
    defineProps({
        title:String,
        navArray:Array,
        stats:String,
        tableStatsArr:Array
    })
    
</script>
<template>
    <div class="d-flex align-items-center gap-7">
        <h1>{{ title }}</h1>
        <div v-if="stats=='title'">
            <TableStats :table-stats="tableStatsArr" />
        </div>
    </div>
    <div class="d-flex align-items-center">
        <div>
            <TableNavigaionBox :nav-array="navArray"/>
        </div>
        <div v-if="stats=='navs'">
            <TableStats :table-stats="tableStatsArr" />
        </div>
    </div>
 
</template>