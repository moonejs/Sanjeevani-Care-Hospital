<script setup>
    import { computed } from 'vue'
    import Btn from '@/components/common/Btn.vue'
    import { useDoctorStore } from '@/stores/doctor.store'
    import Badge from '../common/Badge.vue'

    const doctor = useDoctorStore()

    const appointment = computed(() => doctor.nextAppointment)
    
</script>


<template>
  <div class=" v border-end border-bottom rounded-1 p-3" v-if="appointment && appointment.type && appointment.patient">
    <div class="d-flex flex-column h-100">
      
      <div class="d-flex justify-content-between align-items-center mb-2">
        <span class="text-uppercase small fw-bold tracking-wider text-muted">Up Next</span>
        <Badge :label="appointment.type" color="danger"/>
      </div>

      <div class="d-flex align-items-baseline gap-2 mb-1">
        <h3 class="fw-bold m-0 display-6 text-dark"> <mark>{{ appointment.start_time }}</mark></h3>
        <span class="text-muted small">to {{ appointment.end_time }}</span>
      </div>

      <div class="mt-2 pt-3 border-top d-flex align-items-center justify-content-between">
        <div>
          <div class="text-muted next-apt-small text-uppercase fw-semibold">Patient</div>
          <div class="h6 m-0 fw-bold text-dark ">{{ appointment.patient.name }}</div>
        </div>
        
        
      </div>
      
    </div>
  </div>

  <div v-else class=" p-4 text-center">
    <div class="text-muted small d-flex justify-content-center gap-1 align-items-center">
      <i class="fa-solid fa-calendar-check fs-4 opacity-50"></i>
      <h6 class="text-muted mt-2"> No confirmed appointments </h6>
    </div>
  </div>
  <hr>
</template>

<style scoped>
  .next-apt-small {
      font-size: 0.7rem;
  }
  .v{
    border-left: 4px solid #151616;
}

</style>