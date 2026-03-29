<script setup>
    defineProps({
    stats: Object
    })
</script>

<template>
  <div class="row">
    <div class="col">
      <span>Total Visits : </span>
      <strong class="fw-bold">{{ stats.total_visits }}</strong>
    </div>

    <div class="col">
      <span>Last Visit : </span>
      <strong> <mark>{{ stats.last_visit || '—' }}</mark></strong>
    </div>

  </div>
</template>