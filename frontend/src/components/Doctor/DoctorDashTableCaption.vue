<script setup>
    import TableNavigaionBox from '../common/TableNavigaionBox.vue';
    import TableStats from '../common/TableStats.vue';
    import SearchInput from '@/components/common/SearchInput.vue';
    defineProps({
        title:String,
        navArray:Array,
        stats:String,
        tableStatsArr:Array,
        searchQuery:String,
        placeholder:String
    })
    const emit = defineEmits(['today-or-week', 'update:searchQuery'])
</script>
<template>
    <div class="d-flex align-items-center justify-content-between mb-3 ">
        <div class="d-flex gap-10 ">
            <h5 class="m-0 fw-bold text-dark">{{ title }}</h5>
            <SearchInput class="ms-12" :modelValue="searchQuery"@update:modelValue="(val) => emit('update:searchQuery', val)":placeholder="placeholder"/>
        </div>
        
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