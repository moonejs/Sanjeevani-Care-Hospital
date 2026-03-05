<script setup>
    import { computed } from 'vue'
    import Btn from '@/components/common/Btn.vue'
    import { useDoctorStore } from '@/stores/doctor.store'
    import Badge from '../common/Badge.vue'

    const doctor = useDoctorStore()

    const appointment = computed(() => doctor.nextAppointment)
</script>


<template>
  <div class="ga-card next-apt-card shadow-sm p-3" v-if="appointment && appointment.type && appointment.patient">
    <div class="d-flex flex-column h-100">
      
      <div class="d-flex justify-content-between align-items-center mb-2">
        <span class="text-uppercase small fw-bold tracking-wider text-muted">Up Next</span>
        <Badge :label="appointment.type" color="primary"/>
      </div>

      <div class="d-flex align-items-baseline gap-2 mb-1">
        <h3 class="fw-bold m-0 display-6 text-dark">{{ appointment.start_time }}</h3>
        <span class="text-muted small">to {{ appointment.end_time }}</span>
      </div>

      <div class="mt-2 pt-3 border-top d-flex align-items-center justify-content-between">
        <div>
          <div class="text-muted next-apt-small text-uppercase fw-semibold">Patient</div>
          <div class="h5 m-0 fw-bold text-dark">{{ appointment.patient.name }}</div>
        </div>
        
        <Btn label="View Record" class="btn-info btn-sm px-3" />
      </div>
      
    </div>
  </div>

  <div v-else class="ga-card p-4 text-center">
    <div class="text-muted small">
      <i class="fa-solid fa-calendar-check d-block mb-2 fs-4 opacity-50"></i>
      No confirmed appointments remaining
    </div>
  </div>
</template>

<style scoped>
  .next-apt-small {
      font-size: 0.7rem;
  }

</style>