<script setup>
    import { onMounted } from 'vue'
    import { useAppointmentStore } from '@/stores/appointment.store'
    import DoctorAppointmentsPageTable from '@/components/Doctor/appointment/DoctorAppointmentsPageTable.vue'
    import Pagination from '@/components/common/Pagination.vue'
    import AppointmentDetailsOffcanvas from '@/components/Doctor/appointment/AppointmentDetailsOffcanvas.vue'
    import { ref } from 'vue'

    const appointment = useAppointmentStore()
    const showDetails = ref(false)
    const selectedAppointment = ref(null)

    onMounted(() => {
        appointment.fetchDoctorAppointmentHistory(1)
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
        <div class="container-fluid">
            <DoctorAppointmentsPageTable :appointments="appointment.appointmentHistory" @view="openDetails" />
            <Pagination :pagination="appointment.historyPagination" @change="changePage"/>
        </div>
        <AppointmentDetailsOffcanvas :show="showDetails" :appointment="selectedAppointment" @close="closeDetails"/>
    </div>
</template>