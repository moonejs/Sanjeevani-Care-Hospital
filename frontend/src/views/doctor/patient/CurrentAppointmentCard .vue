<script setup>
    defineProps({
        appointment: Object
    })
</script>

<template>
  <div class="bg-warning mb-3">
    <h5>Current Appointment</h5>

    <div v-if="appointment">
      <p><b>Date:</b> {{ appointment.date }}</p>
      <p><b>Time:</b> {{ appointment.time }}</p>
      <p><b>Status:</b> {{ appointment.status }}</p>
      <p><b>Type:</b> {{ appointment.type }}</p>
    </div>

    <p v-else class="text-muted">No active appointment</p>
  </div>
</template>
