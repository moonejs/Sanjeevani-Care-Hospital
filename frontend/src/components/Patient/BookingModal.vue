  <script setup>
    import { useAppointmentStore } from '@/stores/appointment.store';
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
      'confirm'
    ])
  </script>

  <template>
  <div v-if="showModal">
    <div class="modal show" style="display: block;">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">

          <div class="modal-header">
            <h5 class="modal-title">{{ appointment.activeAppointment && appointment.activeAppointment.doctor.id == selectedDoctor.doctor.id ? "Reschedule Appointment" : "Book Appointment" }}</h5>
            <button class="btn-close" @click="emit('close')"></button>
          </div>
          <div v-if="appointment.activeAppointment && appointment.activeAppointment.doctor.id == selectedDoctor.doctor.id" class="alert alert-warning">
            You already have an appointment.
            Selecting a new slot will reschedule it.
          </div>

          <div class="modal-body">
            <p><b>Doctor:</b> Dr. {{ selectedDoctor.doctor.name }}</p>
            <p><b>Time:</b> {{ selectedSlot.time }}</p>
            <p><b>Slot:</b> {{ slotSession }}</p>

            <label>
              <input type="radio" value="opd"
                :checked="appointmentType === 'opd'"
                @change="emit('update:appointmentType', 'opd')" />
              OPD
            </label>

            <label>
              <input type="radio" value="follow_up"
                :checked="appointmentType === 'follow_up'"
                @change="emit('update:appointmentType', 'follow_up')" />
              Follow-up
            </label>

            <label>
              <input type="radio" value="emergency"
                :checked="appointmentType === 'emergency'"
                @change="emit('update:appointmentType', 'emergency')" />
              Emergency
            </label>
          </div>

          <div class="modal-footer">
            <button class="btn btn-secondary" @click="emit('close')">Cancel</button>
            <button class="btn btn-primary" @click="emit('confirm')">{{ appointment.activeAppointment && appointment.activeAppointment.doctor.id == selectedDoctor.doctor.id ? 'Reschedule' : 'Confirm Booking' }}</button>
          </div>

        </div>
      </div>
    </div>

    <div class="modal-backdrop fade show"></div>
  </div>
</template>
