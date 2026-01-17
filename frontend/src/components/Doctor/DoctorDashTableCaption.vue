<script setup>
    import TableNavigaionBox from '../common/TableNavigaionBox.vue';
    import TableStats from '../common/TableStats.vue';
    import { ref } from 'vue';
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
    <div>
        <div>
            <TableNavigaionBox :nav-array="navArray"/>
        </div>
        <div>
            
        </div>
    </div>
 
</template>