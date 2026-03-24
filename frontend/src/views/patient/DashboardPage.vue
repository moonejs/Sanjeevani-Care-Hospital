<script setup>
    import { onMounted } from 'vue'
    import { usePatientStore } from '@/stores/patient.store'
    import NextAppointmentPatientCard from '@/components/Patient/NextAppointmentPatientCard.vue';
    import LastVisitCard from '@/components/Patient/LastVisitCard.vue';
    
    const patient = usePatientStore()

    onMounted(() => {
        patient.fetchPatientDashboardData()
    })
</script>

<template>
  <div class="container-fluid mt-4">

    <div class="row g-3">

      <div class="col mx-auto">
        <h5 class="card-title mb-3">Your Next Appointment</h5>
        <NextAppointmentPatientCard :appointment="patient.nextAppointment" :count="patient.upcomingCount" :loading="patient.loading"
        />

      </div>
      <div class="col ">
        <h5 class="card-title mb-3">Last Visit Summery</h5>
        <LastVisitCard  :visit="patient.lastVisit"  :loading="patient.loading"/>
      </div>

    </div>

  </div>
</template>
