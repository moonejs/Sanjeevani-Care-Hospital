<script setup>
    defineProps({
    stats: Object
    })
</script>

<template>
  <div class=" mt-3">
    <h5 class="mb-2">Patient Stats</h5>

    <div class="d-flex justify-content-between">
      <span>Total Visits</span>
      <strong>{{ stats.total_visits }}</strong>
    </div>

    <div class="d-flex justify-content-between">
      <span>Last Visit</span>
      <strong>{{ stats.last_visit || '—' }}</strong>
    </div>
  </div>
</template>
