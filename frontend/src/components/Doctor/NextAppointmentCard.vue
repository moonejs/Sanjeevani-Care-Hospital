<script setup>
    import { computed } from 'vue'
    import Btn from '@/components/common/Btn.vue'
    import { useDoctorStore } from '@/stores/doctor.store'

    const doctor = useDoctorStore()

    const appointment = computed(() => doctor.nextAppointment)
</script>

<template>
  <div class="card shadow-sm bg-warning-subtle" v-if="appointment && appointment.type && appointment.patient">
    <div class="card-body">

      <h5 class="card-title mb-3">Next Appointment</h5>

      <div class="d-flex align-items-center gap-3 mb-2">
        <span class="fw-bold fs-5">
          {{ appointment.start_time }}
        </span>

        <span class="fs-5">→</span>

        <span class="fw-bold fs-5">
          {{ appointment.end_time }}
        </span>

        <span class="ms-auto badge bg-dark">
          {{ appointment.type.toUpperCase() }}
        </span>
      </div>

      <div class="mb-3">
        <span class="fw-semibold">
          {{ appointment.patient.name }}
        </span>
        <Btn label="View" class="btn-tertiary btn-sm ms-2" />
      </div>

      
    </div>
  </div>

  <div v-else class="card bg-light">
    <div class="card-body text-muted">
      No Confirm appointments
    </div>
  </div>
</template>
