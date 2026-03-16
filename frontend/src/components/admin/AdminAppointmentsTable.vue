<script setup>
    import BaseTable from '@/components/layout/BaseTable.vue';
    import BaseTableHead from '@/components/layout/BaseTableHead.vue';
    import AdminAppointmentsTableRow from './AdminAppointmentsTableRow.vue';
    import DoctorDashTableCaption from '../Doctor/DoctorDashTableCaption.vue';
    import { ref } from 'vue';
    const props = defineProps({
        appointments:Array
    })
    const emit=defineEmits(['view'])
    const tHead=ref(["Date","Time","Status","Type","Patient Name","Diagnosis","Follow_up_date","Actions"])
</script>
<template>
    <BaseTable>
        <template #caption>
            <DoctorDashTableCaption title="Appointment History"/>
        </template>
        <template #head>
            <BaseTableHead :t-head="tHead"/>
        </template>
        <template #body>
            <AdminAppointmentsTableRow v-for="(app,index) in appointments" :key="app.id"
            :appointment="app" :index="index" @view="emit('view',app)"
            />
        </template>
    </BaseTable>
</template>