<script setup>
    import { onMounted } from 'vue'
    import { useAppointmentStore } from '@/stores/appointment.store'
    import DoctorAppointmentsPageTable from '@/components/Doctor/appointment/DoctorAppointmentsPageTable.vue'
    import Pagination from '@/components/common/Pagination.vue'
    import AppointmentDetailsOffcanvas from '@/components/Doctor/appointment/AppointmentDetailsOffcanvas.vue'
    import { ref } from 'vue'
    import LoadingState from '@/components/common/LoadingState.vue'

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
        
        <LoadingState :loading="appointment.loading">

            <div class="container-fluid" v-if="appointment.appointmentHistory.length !=0">
                <DoctorAppointmentsPageTable  @view="openDetails" />
                <Pagination :pagination="appointment.historyPagination" @change="changePage"/>
            </div>
            <h2 v-else class="text-muted text-center mt-10">No Appointment History</h2>
            <AppointmentDetailsOffcanvas :show="showDetails" :appointment="selectedAppointment" @close="closeDetails" owner="doctor"/>
        </LoadingState>
    </div>
</template>