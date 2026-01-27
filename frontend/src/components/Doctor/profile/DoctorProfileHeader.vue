<script setup>
    import { useDoctorStore } from "@/stores/doctor.store"
    const store = useDoctorStore()
</script>   

<template>
  <div class="d-flex justify-content-between align-items-center">
    <div>
      <h5>{{ store.doctorProfile?.name }}</h5>
      <small class="text-muted">Doctor Profile</small>
    </div>

    <span
      class="badge"
      :class="store.doctorProfile?.profile_completed ? 'bg-success' : 'bg-warning'"
    >
      {{ store.doctorProfile?.profile_completed ? 'Verified & Live' : 'Pending' }}
    </span>
  </div>
</template>
