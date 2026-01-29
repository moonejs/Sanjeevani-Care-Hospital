<script setup>
    import Badge from '../common/Badge.vue';
    import { computed } from 'vue';
    const props=defineProps({
        doctor: {
            type: Object,
            required: true
        }
    })
    const bookable=computed(()=>{
            return props.doctor.is_bookable
        })
</script>

<template>
  <div class="bg-light doctor-mini-card p-3 mb-3 pointer animate-up-1 border-1 position-relative">
    <div class="d-flex align-items-center gap-3">

      <div class="doctor-avatar">
        <img
          :src="doctor.profile_image || '/doctor-placeholder.png'"
          alt="Doctor"
        />
      </div>

      
      <div class="flex-grow-1">
        <h5 class="mb-1 fw-semibold">
          Dr. {{ doctor.name }}
        </h5>

        <p class="mb-0 text-muted small">
          {{ doctor.specialization }}
          <span v-if="doctor.roles">
            • {{ doctor.roles }}
          </span>
        </p>
      </div>
      <Badge :label="bookable ? 'Booking Open' : 'Booking closed'" :color="bookable ? 'success':'danger'" class="position-absolute top-0 end-0 mt-1 me-1"/>  
    </div>
  </div>
</template>
