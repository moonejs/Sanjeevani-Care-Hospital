<script setup>
    import { onMounted, ref } from 'vue'
    import { usePatientStore } from '@/stores/patient.store'
    import PatientAppointmentsTable from '@/components/Patient/PatientAppointmentsTable.vue'
    import AppointmentDetailsOffcanvas from '@/components/Doctor/appointment/AppointmentDetailsOffcanvas.vue'

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
  <div class="container-fluid">
    
    <PatientAppointmentsTable
      :appointments="patient.patientAppointmentHistory"
      :loading="patient.loading"
      @view="openDetails"
    />

    <Pagination
      :pagination="patient.historyPagination"
      @change="changePage"
    />

    <AppointmentDetailsOffcanvas
      :show="showDetails"
      :appointment="selectedAppointment"
      @close="showDetails = false",
      owner="patient"
    />
  </div>
</template>