    <script setup>
      import { useAppointmentStore } from '@/stores/appointment.store';
      import Btn from '../common/Btn.vue';
      import { computed } from 'vue'
      const appointment=useAppointmentStore()
      const props = defineProps({
        showModal: Boolean,
        selectedDoctor: Object,
        selectedSlot: Object,
        appointmentType: String,
        slotSession:String
      })

      const emit = defineEmits([
        'update:appointmentType',
        'close',
        'confirm',
        'cancel-appointment'
      ])
      

    const isMySlot = computed(() => {
      return props.selectedSlot?.appointment_id !== null
    })

    const isConfirmed = computed(() => {
      return props.selectedSlot?.appointment_status === "confirmed"
    })

    const hasAppointmentWithSameDoctor = computed(() => {
      return Object.values(props.selectedDoctor?.sessions || {})
        .flat()
        .some(slot => slot.appointment_id !== null)
    })

    const isReschedule = computed(() => {
      return hasAppointmentWithSameDoctor.value && !isMySlot.value
    })
          
    const myAppointmentId = computed(() => {
      return props.selectedSlot?.appointment_id
    })

    </script>

    <template>
    <div v-if="showModal">
      <div class="modal show " style="display: block;">
        <div class="modal-dialog modal-dialog-centered">
          <div class="modal-content v">
            <div class="modal-header">
              <h5 class="modal-title">{{isMySlot && isConfirmed
                  ? "Appointment Confirmed"
                  : isMySlot
                  ? "Cancel Appointment"
                  : isReschedule
                  ? "Reschedule Appointment"
                  : "Book Appointment"
                }} 
              </h5>
              <button class="btn-close" @click="emit('close')"></button>
            </div>
            <div v-if="isMySlot && isConfirmed" class="alert  alert-success fw-bold">
                Appointment is confirmed. You cannot cancel it.
            </div>
            <div v-else-if="isMySlot" class="alert alert-danger m-3">
              This will cancel your current appointment.
            </div>

            <div v-else-if="isReschedule" class="alert alert-warning m-3">
              You already have an appointment with this doctor.
              Selecting this slot will reschedule it.
            </div>
            <div class="modal-body">
              <p><span class="text-muted small fw-bold" >Doctor : </span> <span class="fw-bold">Dr. {{ selectedDoctor?.doctor?.name }}</span> </p>
              <p> <span class="text-muted small fw-bold" >Time : </span> <span class="fw-bold"> <mark>{{ selectedSlot?.time }}</mark> </span> </p>
              <p> <span class="text-muted small fw-bold" >Slot : </span><span class="fw-bold text-success">{{ slotSession }}</span> </p>
              <hr>
              <label class="me-2">
                <input type="radio" value="opd" 
                  :checked="appointmentType === 'opd'"
                  @change="emit('update:appointmentType', 'opd')" />
                OPD
              </label>

              <label class="me-2">
                <input type="radio" value="follow_up"
                  :checked="appointmentType === 'follow_up'"
                  @change="emit('update:appointmentType', 'follow_up')" />
                Follow-up
              </label>

              <label class="me-2 text-danger">
                <input type="radio" value="emergency"
                  :checked="appointmentType === 'emergency'"
                  @change="emit('update:appointmentType', 'emergency')" />
                Emergency
              </label>
            </div>

            <div class="modal-footer">
              <div v-if="isMySlot && isConfirmed" class="text-success fw-bold">
                Appointment Confirmed
              </div>
              <Btn  v-else-if="isMySlot && !isConfirmed" label="Cancel Appointment" class="btn-sm btn-danger" @click="emit('cancel-appointment', myAppointmentId)"/>
              <Btn  v-else-if="isReschedule" label="Reschedule" class="btn btn-primary btn-sm" @click="emit('confirm')" />

              <Btn  v-else label="Confirm Booking" class="btn btn-outline-primary btn-sm" @click="emit('confirm')"/>

            </div>      
          </div>
        </div>
      </div>

      <div class="modal-backdrop fade show"></div>
    </div>
  </template>

  <style scoped>

  .v{
    background-color: #f1f3f5;  
  }
  </style>
