<script setup>
    import CountCard from '@/components/admin/CountCard.vue';
    import { useAdminStore } from '@/stores/admin.store';
    import { onMounted,ref } from 'vue';
    import AdminDashboardAppointmentTable from '@/components/admin/AdminDashboardAppointmentTable.vue';

    const adminStore=useAdminStore()
    const stats=ref()
    onMounted(async()=>{
        await adminStore.fetchAdminDashboardDetails("today")
        // stats.value=adminStore.dashboard.stats
    })

    
</script>

<template>
    <div class="row container-fluid justify-content-between">
        
        <div class="col-10 bg-warning-subtle  ">
            <AdminDashboardAppointmentTable />
        </div>
        <div class="col-2 bg-info-subtle">
            <div class="row">
                dd
            </div>
            <div class="row gap-3">
            <CountCard label="Doctors" :stats="stats?.doctors"/>
            <CountCard label="Patients" :stats="stats?.patients"/>
            <CountCard label="Appointments" :stats="stats?.appointments"/>
            
            </div>
        </div>
        
    </div>
</template>