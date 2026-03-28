<script setup>
import Btn from '../common/Btn.vue'
import { watch, onMounted } from 'vue'
import Badge from '../common/Badge.vue'

const props = defineProps({
  showModel: Boolean,
  patient: Object
})

const emit = defineEmits(['close'])

let instance = null
let el = null

onMounted(() => {
  el = document.getElementById('patientOffcanvas')
  if (!el) return

  instance = bootstrap.Offcanvas.getOrCreateInstance(el)

  el.addEventListener('hidden.bs.offcanvas', () => {
    emit('close')
  })
})

watch(
  () => props.showModel,
  (val) => {
    if (!instance) return
    val ? instance.show() : instance.hide()
  }
)
</script>

<template>
  <div class="offcanvas offcanvas-end" tabindex="-1" id="patientOffcanvas">
    
    
    <div class="offcanvas-header border-bottom">
      <h5 class="offcanvas-title">Patient Details</h5>
      <button type="button" class="btn-close" @click="emit('close')"></button>
    </div>

  
    <div class="offcanvas-body" v-if="patient">
      
     
      <div class="text-center mb-4">
        <img
          :src="patient.profile_image"
          class="rounded-circle border"
          style="width: 100px; height: 100px; object-fit: cover"
        />

        <h5 class="mt-2 mb-0">{{ patient.name }}</h5>
        <small class="text-muted">{{ patient.email }}</small>

        <div class="mt-2">
          <Badge
            :label="patient.profile_completed ? 'Profile Completed' : 'Profile Incomplete'"
            :color="patient.profile_completed ? 'success' : 'warning'"
          />
        </div>
      </div>

      <hr />

     
      <div class="mb-3">
        <p><span class="fw-bold small">Gender : </span> <span class="small">{{ patient.gender || 'Not Provided' }}</span></p>
        <p><span class="fw-bold small">Age : </span> <span class="small">{{ patient.age || 'Not Provided' }}</span></p>
        <p><span class="fw-bold small">Blood Group : </span> <span class="small">{{ patient.blood_group || 'Not Provided' }}</span></p>
      </div>

      <hr />

    
      <div class="mb-3">
        <p><span class="fw-bold small">Contact : </span> <span class="small">{{ patient.contact || 'Not Provided' }}</span></p>
        <p><span class="fw-bold small">Emergency Contact : </span> <span class="small">{{ patient.emergency_contact_number || 'Not Provided' }}</span></p>
        <p><span class="fw-bold small">Emergency Name : </span> <span class="small">{{ patient.emergency_contact_name || 'Not Provided' }}</span></p>
      </div>

      <hr />

      
      <div class="mb-3">
        <p><span class="fw-bold small">Height (cm) : </span> <span class="small">{{ patient.height_cm || 'Not Provided' }}</span></p>
        <p><span class="fw-bold small">Weight (kg) : </span> <span class="small">{{ patient.weight_kg || 'Not Provided' }}</span></p>
      </div>

      <hr />

  
      <div class="mb-3">
        <p><span class="fw-bold small">Address : </span></p>
        <p class="small text-muted">{{ patient.address || 'Not Provided' }}</p>
      </div>


      <div class="d-flex gap-2 mt-3">
        <Btn label="Close" class="btn-outline-dark btn-sm" @click="emit('close')" />
      </div>

    </div>
  </div>
</template>