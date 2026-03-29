<script setup>
import Badge from '@/components/common/Badge.vue';
    defineProps({
        appointment: Object
    })
</script>

<template>
  <div class=" mt-3">
    <div v-if="appointment">
      <div class="mb-2">
        <span><span>Date : </span><span class="fw-bold mark ">  {{ appointment.date }}</span></span>
      </div>
      <div class="mb-2">
        <span><span>Time : </span><span class="fw-bold text-underline">{{ appointment.time }}</span></span>
      </div>
      <div class="mb-2">
        <span><span>Status : </span><span class="fw-bold text-capitalize">
          <Badge :label="appointment.status" :color="appointment.status === 'confirmed' ? 'success':
          appointment.status === 'cancelled' ? 'danger' : appointment.status === 'completed' ? 'primary' : 'secondary'"/>


        </span></span>
      </div>
      <div class="mb-2">
        <span><span>Type : </span><span class="fw-bold text-danger text-uppercase">{{ appointment.type }}</span></span>
      </div>
    </div>

    <p v-else class="text-muted">No active appointment</p>
  </div>
</template>
