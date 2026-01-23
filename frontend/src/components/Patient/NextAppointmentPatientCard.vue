<script setup>
    import Btn from '@/components/common/Btn.vue'
    import { useRouter } from 'vue-router'

    defineProps({
        appointment: Object,
        count: Number,
        loading: Boolean
    })

    const router = useRouter()

    function openMyAppointments(){
        router.push('/appointments')
    }
</script>

<template>
  <div class=" bg-success shadow-sm mb-4">
    <div class="card-body">

      <h5 class="card-title mb-3">Your Next Appointment</h5>

      <div v-if="loading" class="text-muted">
        Loading...
      </div>

      <div v-else-if="appointment">
        <p class="fw-bold mb-1">
          {{ appointment.doctor.name }}
          <span class="text-muted">
            ({{ appointment.doctor.department }})
          </span>
        </p>

        <p class="mb-1">
          {{ appointment.date }} · {{ appointment.time }}
        </p>

        <p class="mb-3">
          Status:
          <span class="badge bg-success">
            {{ appointment.status }}
          </span>
        </p>
        <p class="mb-3">
          Type:
          <span class="badge bg-success">
            {{ appointment.type }}
          </span>
        </p>

        <div class="d-flex gap-2">
          <Btn label="View Details" class="btn-outline-primary btn-sm" @click="" />
          <Btn label="Cancel" class="btn-outline-danger btn-sm" />
        </div>

        <div v-if="count > 0" class="mt-3 text-primary">
          You have {{ count }} more upcoming appointment{{ count > 1 ? 's' : '' }}
          <div>
            <button class="btn btn-link p-0" @click="openMyAppointments">
              View all
            </button>
          </div>
        </div>
      </div>

      <div v-else class="text-muted">
        No upcoming appointments
      </div>

    </div>
  </div>
</template>
