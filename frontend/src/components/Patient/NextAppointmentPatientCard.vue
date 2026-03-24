<script setup>
import Btn from '@/components/common/Btn.vue'
import { useRouter } from 'vue-router'
import { useAppointmentStore } from '@/stores/appointment.store'
import Badge from '../common/Badge.vue'
import { useToastStore } from '@/stores/toast.store';
const toast = useToastStore()

const appointmentStore = useAppointmentStore()

const props = defineProps({
  appointment: Object,
  count: Number,
  loading: Boolean
})

async function handleCancel() {
  if (!props.appointment?.appointment_id) return
  toast.addToast({
          message: 'Appointment Cancelled Succesfully',
          type: 'success'
        })
  try {
    await appointmentStore.cancelBookedAppointment(
      props.appointment.appointment_id,
      { reason: "Cancelled by patient" }
    )
    
  } catch (err) {
    console.log(err)
  }
}

const router = useRouter()

function openMyAppointments() {
  router.push('/appointments')
}


function getStatusColor() {
  if (props.appointment.status === 'confirmed') return 'success'
  if (props.appointment.status === 'pending') return 'warning'
  if (props.appointment.status === 'cancelled') return 'danger'

  return 'primary'
}
</script>

<template>
  <div class="ga-card  p-3 mb-3">

    <div v-if="loading" class="text-muted small">
      Loading...
    </div>

    <div v-else-if="appointment">

      
      <div class="d-flex justify-content-between align-items-start mb-2">

        <div>
          <div class="fw-semibold">
            {{ appointment.doctor.name }}
            <span class="text-muted">
              ({{ appointment.doctor.department }})
            </span>
          </div>
        </div>

       <Badge :label="appointment.status" :color="getStatusColor()" />
        

      </div>

      
      <div class="small text-muted mb-2">
        {{ appointment.date }} • {{ appointment.time }}
      </div>

      
      <div class="small mb-3">
        Type:
        <span class="text-muted">
          {{ appointment.type }}
        </span>
      </div>

      
      <div class="d-flex gap-2">
        <Btn v-if="appointment.status != 'confirmed'"
          label="Cancel" 
          class="btn-outline-danger btn-sm" 
          @click="handleCancel"
        />
      </div>

      
      

    </div>

    <div v-else class="text-muted small">
      No upcoming appointments
    </div>

  </div>
</template>

