<script setup>
    import BaseTable from '../layout/BaseTable.vue';
    import BaseTableHead from '../layout/BaseTableHead.vue';
    import { ref } from 'vue';
    import DoctorDashTableCaption from './DoctorDashTableCaption.vue';
    const tHead=ref(["Name","Age","Gender","Last Visit","Visits","Action"])
</script>
<template>
    <BaseTable>
        <template #caption>
            <DoctorDashTableCaption title="Assigned Patients"/>
        </template>

        <template #head>
            <BaseTableHead :t-head="tHead"/>
        </template>

        <template #body>
            
        </template>

    </BaseTable>
</template>