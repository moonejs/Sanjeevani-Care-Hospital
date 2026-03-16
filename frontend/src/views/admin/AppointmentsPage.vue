<script setup>
    import Pagination from '@/components/common/Pagination.vue';
    import AdminAppointmentsTable from '@/components/admin/AdminAppointmentsTable.vue';
    import LoadingState from '@/components/common/LoadingState.vue';
    import { useAdminStore } from '@/stores/admin.store';
    import { onMounted,ref } from 'vue';
    import AppointmentDetailsOffcanvas from '@/components/Doctor/appointment/AppointmentDetailsOffcanvas.vue';

    const adminStore=useAdminStore()
    const selectedAppointment=ref(null)
    const showDetails=ref(false)
    onMounted(async ()=>{
        await adminStore.fetchAdminAppointments(1)
    })
    function changePage(page) {
        appointment.fetchDoctorAppointmentHistory(page)
    }
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
        <div class="bg-info doctor-appointment-filter">
            filter
        </div>
        <LoadingState :loading="adminStore.loading">

            <div class="container-fluid" v-if="adminStore.adminAppointments.length !=0">
                <AdminAppointmentsTable :appointments="adminStore.adminAppointments" @view="openDetails"/>
                <Pagination :pagination="adminStore.adminAppointmentsPagination" @change="changePage" />
            </div>
            <h2 v-else class="text-muted text-center mt-10">No Appointment History</h2>
            <AppointmentDetailsOffcanvas :show="showDetails" :appointment="selectedAppointment" @close="closeDetails"/>
        </LoadingState>
    </div>
</template>