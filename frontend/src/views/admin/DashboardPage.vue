<script setup>
    import CountCard from '@/components/admin/CountCard.vue';
    import { useAdminStore } from '@/stores/admin.store';
    import { onMounted,ref,computed } from 'vue';
    import AdminDashboardAppointmentTable from '@/components/admin/AdminDashboardAppointmentTable.vue';
    import Time from '@/components/Doctor/Time.vue';

    const adminStore=useAdminStore()
    const stats = computed(() => adminStore.dashboard.stats || {})
    onMounted(async()=>{
        await adminStore.fetchAdminDashboardDetails("today")
        // stats.value=adminStore.dashboard.stats
    })

    
</script>

<template>
    
    <div class="row container-fluid justify-content-between">
        <div class="col-10  mt-4 ">
            <AdminDashboardAppointmentTable />
        </div>
        <div class="col-2 ">
            <div class="row mt-4">
                <Time type="analog" />
            </div>
            <div class="row gap-3 mt-5 pt-4">
                <CountCard label="Doctors" :stats="stats?.doctors"/>
                <CountCard label="Patients" :stats="stats?.patients"/>
                <CountCard label="Appointments" :stats="stats?.appointments"/>
                <CountCard label="Departments" :stats="stats.departments"/>
            </div>
        </div>

    </div>
</template>

<style scoped>

</style>