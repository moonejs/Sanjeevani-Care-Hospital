<script setup>
    import { useDoctorStore } from "@/stores/doctor.store"
    import Badge from "@/components/common/Badge.vue";
    const doctorStore = useDoctorStore()
</script>   

<template>
  <div class="d-flex justify-content-between align-items-center">
    <div>
      <h5 class="text-capitalize fw-bolder"> Dr. {{ doctorStore.doctorProfile?.name }}</h5>
      <small class="text-muted">{{ doctorStore.doctorProfile?.specialization }}</small>
    </div>

    <Badge :label="doctorStore.doctorProfile?.profile_completed ? 'Verified & Live' : 'Pending'"  :color="doctorStore.doctorProfile?.profile_completed ? 'success' : 'warning'" />
    
  </div>
</template>
