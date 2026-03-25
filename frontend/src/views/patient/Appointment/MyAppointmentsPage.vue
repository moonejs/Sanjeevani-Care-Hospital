<script setup>
    import { onMounted, ref } from 'vue'
    import { usePatientStore } from '@/stores/patient.store'
    import PatientAppointmentsTable from '@/components/Patient/PatientAppointmentsTable.vue'
    import AppointmentDetailsOffcanvas from '@/components/Doctor/appointment/AppointmentDetailsOffcanvas.vue'
    import LoadingState from '@/components/common/LoadingState.vue'
    import Pagination from '@/components/common/Pagination.vue'

    const patient = usePatientStore()

    const showDetails = ref(false)
    const selectedAppointment = ref(null)

    onMounted(() => {
        patient.fetchPatientAppointmentsHistory(1)
    })

    function changePage(page) {
        patient.fetchPatientAppointmentsHistory(page)
    }

    function openDetails(appt) {
        selectedAppointment.value = appt
        showDetails.value = true
    }

    
</script>

<template>
  <LoadingState :loading="patient.loading">
    <div class="container-fluid history-page-p" v-if="patient.patientAppointmentHistory.length !=0">
        <PatientAppointmentsTable :appointments="patient.patientAppointmentHistory" :loading="patient.loading" @view="openDetails"/>

        <Pagination :pagination="patient.historyPagination" @change="changePage"/>

        <AppointmentDetailsOffcanvas :show="showDetails" :appointment="selectedAppointment" @close="showDetails = false", owner="patient" />
    </div>
    <div v-else>
      <h2 class="text-muted text-center mt-10 ">No Appointments Found</h2>
    </div>
  </LoadingState>
  
</template>

<style scoped>
.history-page-p{
  height: 40rem ;
  overflow-y: hidden;
}
</style>