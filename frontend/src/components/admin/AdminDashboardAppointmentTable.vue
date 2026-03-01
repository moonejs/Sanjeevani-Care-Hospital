<script setup>
    import BaseTable from '../layout/BaseTable.vue';
    import DoctorDashTableCaption from '../Doctor/DoctorDashTableCaption.vue';
    import { ref,computed } from 'vue';
    import AdminDashboardAppointmentRow from './AdminDashboardAppointmentRow.vue';
    import BaseTableHead from '../layout/BaseTableHead.vue';
    import { useAdminStore } from '@/stores/admin.store';
    import Loading from '../common/Loading.vue';
    const adminStore=useAdminStore()

    const type=ref('today')
    const tHead=["Department","Doctor","Patient","Time","Date","Type","Slot","Status","Action"]
    async function showTodayOrWeek(range){
        await adminStore.fetchAdminDashboardDetails(range)
        // stats.value=adminStore.dashboard.stats        
    }
    const tableStatsArr=computed(()=>{
        return [adminStore.appointmentSummary]
    })
</script>
<template>
    <BaseTable>
        <template #caption>
            <DoctorDashTableCaption title="Upcoming Appointments "   @today-or-week="showTodayOrWeek" stats="navs" :table-stats-arr="tableStatsArr"/>
        </template>
        <template #head>
            <BaseTableHead :t-head="tHead"/>
        </template>
        <template #body>
            <Loading :loading="adminStore.loading" class="ms-2 mt-3 start-50 position-absolute" />

            <template v-if="!adminStore.loading">
                <h2 v-if="adminStore.dashboard.upcoming_appointments.length === 0" class="text-muted position-absolute ms-10 mt-4">No Upcoming Appointments</h2>
                
                <AdminDashboardAppointmentRow v-else v-for="(app, index) in adminStore.dashboard.upcoming_appointments" :key="index" :index="index" :appointment="app"/>
            </template>
            

        </template>
    </BaseTable>
</template>