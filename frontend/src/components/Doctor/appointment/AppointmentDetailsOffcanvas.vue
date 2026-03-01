<script setup>
    import Btn from '@/components/common/Btn.vue'
    import { usePatientStore } from '@/stores/patient.store';

    const patientStore=usePatientStore()
    
    import { watch,onMounted } from 'vue';
    const props = defineProps({
        show: Boolean,
        appointment: Object,
        owner:String
    })

    const emit = defineEmits(['close'])
    let instance = null
    let el = null
    onMounted(() => {
      el = document.getElementById('appointmentOffcanvas')
      if (!el) return

      instance = bootstrap.Offcanvas.getOrCreateInstance(el)

      el.addEventListener('hidden.bs.offcanvas', () => {
        emit('close')
      })
    })

    watch(
      () => props.show,
      (val) => {
        if (!instance) return
        val ? instance.show() : instance.hide()
      }
    )

    async function exportTreatment(){
      await patientStore.exportPatientTreatment()
    }
   

</script>
<template>
  <div  class="offcanvas offcanvas-end"  tabindex="-1" id="appointmentOffcanvas">
    <div class="offcanvas-header">
      <h5 class="offcanvas-title">
        Appointment Details
      </h5>
      <button type="button" class="btn-close" @click="emit('close')" aria-label="Close"></button>
    </div>

    <div class="offcanvas-body" v-if="appointment">
      <div class="mb-3" v-if="owner=='doctor'">
        <h6 class="text-muted" >Patient</h6>
        <p class="fw-bold mb-0">{{ appointment?.patient.name }}</p>
      </div>
      <div class="mb-3" v-if="owner=='patient'">
        <h6 class="text-muted" >Doctor</h6>
        <p class="fw-bold mb-0">{{ appointment?.doctor.name }}</p>
      </div>
      <div class="mb-3" v-if="owner=='patient'">
        <h6 class="text-muted" >Department</h6>
        <p class="fw-bold mb-0">{{ appointment?.department.name }}</p>
      </div>

      <hr />
      <div class="mb-3">
        <p><b>Date:</b> {{ appointment.date }}</p>
        <p><b>Time:</b> {{ appointment.time }}</p>
        <p>
          <b>Status:</b>
          <span
            :class="{
              'text-success': appointment.status === 'completed',
              'text-warning': appointment.status === 'pending',
              'text-primary': appointment.status === 'confirmed',
              'text-danger': appointment.status === 'cancelled'
            }"
          >
            {{ appointment.status }}
          </span>
        </p>
        <p><b>Type:</b> {{ appointment.type }}</p>
      </div>

      <hr />
      <div v-if="appointment.treatment">
        <h6 class="text-muted">Diagnosis</h6>
        <p>{{ appointment.treatment.diagnosis }}</p>

        <h6 class="text-muted mt-3">Notes</h6>
        <p>{{ appointment.treatment.notes || '—' }}</p>

        <h6 class="text-muted mt-3">Medicines</h6>
        <ul v-if="appointment.treatment.medicines?.length">
          <li
            v-for="(m, i) in appointment.treatment.medicines"
            :key="i"
          >
            {{ m.name }} — {{ m.dose }} — {{ m.frequency }}
          </li>
        </ul>
        <p v-else class="text-muted">No medicines prescribed</p>

        <p
          v-if="appointment.treatment.follow_up_date"
          class="mt-2"
        >
          <b>Follow-up:</b>
          {{ appointment.treatment.follow_up_date }}
        </p>
      </div>

      <div v-else class="text-muted">
        No treatment recorded
      </div>

      <hr />
      <div class="d-flex gap-2">
        <Btn  :label="patientStore.loading ? 'Exporting...' : 'Print'" class="btn-outline-secondary btn-sm" @click="exportTreatment" />
        <Btn label="Close" class="btn-outline-dark btn-sm" @click="emit('close')" />
      </div>
    </div>
  </div>
</template>
