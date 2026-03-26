<script setup>
    import TableNavigaionBox from '../common/TableNavigaionBox.vue';
    import TableStats from '../common/TableStats.vue';
    import SearchInput from '@/components/common/SearchInput.vue';
    import DateFilter from '@/components/common/DateFilter.vue';
    
    defineProps({
        title:String,
        navArray:Array,
        stats:String,
        tableStatsArr:Array,
        searchQuery:String,
        dateFilter:String,
        placeholder:String,
        class1:String,
        class2:String,
        class3:String,
        isDate:Boolean
    })
    const emit = defineEmits(['today-or-week', 'update:searchQuery','update:dateFilter'])
</script>
<template>
    <div class="d-flex align-items-center justify-content-between mb-3 ">
        <div class="d-flex align-items-center" :class="class2">
            <h4 class="m-0 fw-bold text-dark" >{{ title }}</h4>
            <div :class="class3">
                <div v-if="isDate">
                    <DateFilter :modelValue="dateFilter" @update:modelValue="(val) => emit('update:dateFilter', val)"  />  
                </div>
                <SearchInput :class="class1" :modelValue="searchQuery"@update:modelValue="(val) => emit('update:searchQuery', val)":placeholder="placeholder"/>
            </div>
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