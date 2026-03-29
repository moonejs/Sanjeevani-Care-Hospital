<script setup>
    import { useDoctorStore } from "@/stores/doctor.store"
    import Badge from "@/components/common/Badge.vue";
    const doctorStore = useDoctorStore()
</script>   

<template>
  <div class="d-flex justify-content-between align-items-center">
    <div>
      <div class="d-flex ">
        <h4 class="text-capitalize fw-bolder"> Dr. {{ doctorStore.doctorProfile?.name }}</h4> 
      </div> 
      <small class="text-muted">{{ doctorStore.doctorProfile?.specialization }}</small>
    </div>

    <Badge :label="doctorStore.doctorProfile?.profile_completed ? 'Verified & Live' : 'Pending'"  :color="doctorStore.doctorProfile?.profile_completed ? 'success' : 'warning'" class="position-absolute left-7  top-6 mt-3" />
    <Badge  :label="doctorStore.doctorProfile?.emergency_available ? 'Emergency Available':''" color="danger" class="position-absolute left-10 ms-3 top-6 mt-3"/>
  </div>
</template>
