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

    <div class="row g-4">

      <div class="col-lg-8">

        <NextAppointmentPatientCard :appointment="patient.nextAppointment" :count="patient.upcomingCount" :loading="patient.loading"/>

        <LastVisitCard :visit="patient.lastVisit" :loading="patient.loading"/>

      </div>

      <div class="col-lg-4">
        <div class="card bg-warning-subtle h-100">
          <div class="card-body">
            <h5 class="card-title">Notifications</h5>
            <p class="text-muted">No new notifications</p>
            <button class="btn btn-outline-secondary btn-sm">
              View all
            </button>
          </div>
        </div>
      </div>

    </div>

  </div>
</template>
