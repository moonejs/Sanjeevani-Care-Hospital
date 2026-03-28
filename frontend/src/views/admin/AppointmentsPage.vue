<script setup>
    import Pagination from '@/components/common/Pagination.vue';
    import AdminAppointmentsTable from '@/components/admin/AdminAppointmentsTable.vue';
    import { useAdminStore } from '@/stores/admin.store';
    import { onMounted,ref } from 'vue';
    import AppointmentDetailsOffcanvas from '@/components/Doctor/appointment/AppointmentDetailsOffcanvas.vue';


    const adminStore=useAdminStore()
    const selectedAppointment=ref(null)
    const showDetails=ref(false)

    

    onMounted(async ()=>{
        await adminStore.fetchAdminAppointments(1)
    })
    function openDetails(appt) {
        selectedAppointment.value = appt
        showDetails.value = true
    }
    function closeDetails() {
        showDetails.value = false
        selectedAppointment.value = null
    }  

</script>
<template>
    <div>
            <div class="container-fluid v mt-3">
                <AdminAppointmentsTable @view="openDetails"/>
            </div>
            <AppointmentDetailsOffcanvas :show="showDetails" :appointment="selectedAppointment" owner="admin" @close="closeDetails"/>
        
    </div>
</template>
<style scoped>
.v{
    overflow-x: hidden;
    height: 44rem;
}
</style>