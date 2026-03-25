<script setup>
    import Btn from '@/components/common/Btn.vue'
    import { usePatientStore } from '@/stores/patient.store';
    import Badge from '@/components/common/Badge.vue';

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

    async function downloadPdf(){
    await patientStore.downloadPdf(props.appointment.id)
  }
    

</script>
<template>
  <div class="offcanvas offcanvas-end " tabindex="-1" id="appointmentOffcanvas">
    <div class="offcanvas-header border-bottom ">
      <h5 class="offcanvas-title fw-semibold">
        Appointment Details
      </h5>
      <button type="button" class="btn-close" @click="emit('close')"></button>
    </div>

    <div class="offcanvas-body" v-if="appointment">

      <div class="">

        <div v-if="owner=='doctor'" class="d-flex gap-2">
          <div class="text-muted ">Patient</div>
          <div class="fw-bold">{{ appointment?.patient.name }}</div>
        </div>

        <div v-if="owner=='patient'" class="d-flex gap-2">
          <div class="text-muted small">Doctor : </div>
          <div class="fw-bold"> {{ appointment?.doctor.name }} </div>
        </div>

        <div v-if="owner=='patient'" class="d-flex gap-2 align-items-center">
          <div class="text-muted small">Department : </div>
          <div class="fw-bold"> <mark>{{ appointment?.department.name }} </mark></div>
        </div>

      </div>

     <hr>
      <div class="">

        <div class="">
          <div class="d-flex gap-2 align-items-center mb-2">
            <div class="text-muted small">Date : </div>
            <div class="fw-bold">{{ appointment.date }}</div>
          </div>

          <div class="d-flex gap-2 align-items-center mb-2">
            <div class="text-muted small">Time : </div>
            <div class="fw-bold">{{ appointment.time }}</div>
          </div>

          <div class="d-flex gap-2 align-items-center mb-2">
            <div class="text-muted small">Status : </div>
            <Badge 
              :label="appointment.status" 
              :color="
                appointment.status === 'completed' ? 'success' :
                appointment.status === 'pending' ? 'warning' :
                appointment.status === 'confirmed' ? 'primary' :
                appointment.status === 'cancelled' ? 'danger' : 'secondary'
              " 
            />
            
          </div>
          <hr>
          <h5 class="text-muted mb-3">Treatment</h5>
          <div class="d-flex gap-2 align-items-center mb-2">
            <div class="text-muted small">Type : </div>
            <div class="fw-bold text-danger text-uppercase">{{ appointment.type }}</div>
          </div>

        </div>

      </div>
      <div class="">
        <div v-if="appointment.treatment">

          <div class="d-flex gap-2 align-items-center mb-2 ">
            <div class="text-muted small">Diagnosis : </div>
            <div class="fw-bold text-underline">{{ appointment.treatment.diagnosis }}</div>
          </div>

          <div class="d-flex gap-2 align-items-center mb-2">
            <div class="text-muted small">Notes : </div>
            <div class="text-italic">
              {{ appointment.treatment.notes || '—' }}
            </div>
          </div>

          <div class="d-flex gap-2 align-items-center mb-2">
            <div class="text-muted small">Medicines : </div>

            <ul v-if="appointment.treatment.medicines?.length" class="">
              <li v-for="(m, i) in appointment.treatment.medicines" :key="i" class="fw-bold ">
                {{ m.name }} — {{ m.dose }} — {{ m.frequency }}
              </li>
            </ul>

            <div v-else class="text-muted small">
              No medicines prescribed
            </div>
          </div>

          <hr>
          <div v-if="appointment.treatment.follow_up_date" class="d-flex gap-2 align-items-center mb-2">
            <div class="text-muted small">Follow-up : </div>
            <div class="fw-bold"> <mark>{{ appointment.treatment.follow_up_date }}</mark>
              
            </div>
          </div>
        </div>
        
        <div v-else class="text-muted small">
          No treatment recorded
        </div>

      </div>

    </div>
    <div class="offcanvas-footer border-top p-3 d-flex gap-2">

      <Btn :label="patientStore.loadingPdf ? 'Generating...' : 'Download Report'" class="btn-outline-primary btn-sm" @click="downloadPdf"/>

      <Btn label="Close" class="btn-outline-dark btn-sm" @click="emit('close')" />

    </div>

  </div>
</template>

<style></style>
