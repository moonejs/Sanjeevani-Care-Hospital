<script setup>
    import Btn from '../common/Btn.vue';
    import { watch,onMounted } from 'vue';
    const props=defineProps({
        show:Boolean,
        doctor:Object
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

   
</script>

<template>
  <div class="offcanvas offcanvas-end" tabindex="-1" id="appointmentOffcanvas">
    <div class="offcanvas-header border-bottom">
      <h5 class="offcanvas-title">Doctor Details</h5>
      <button type="button" class="btn-close" @click="emit('close')" aria-label="Close"></button>
    </div>

    <div class="offcanvas-body" v-if="doctor">
      
      <div class="text-center mb-4">
        <img
          :src="doctor.profile_image"
          class="rounded-circle border"
          style="width: 100px; height: 100px; object-fit: cover"
        />
        <h5 class="mt-2 mb-0">Dr. {{ doctor.name }}</h5>
        <small class="text-muted">{{ doctor.specialization }}</small>

        <div class="mt-2">
          <span class="badge bg-success" v-if="doctor.profile_completed">Profile Completed</span>
          <span class="badge bg-warning text-dark" v-else>Profile Incomplete</span>

          <span
            class="badge ms-2"
            :class="doctor.emergency_available ? 'bg-danger' : 'bg-secondary'"
          >
            {{ doctor.emergency_available ? 'Emergency Available' : 'Emergency Not Available' }}
          </span>
        </div>
      </div>

      
      <div class="mb-3">
        <h6 class="fw-semibold border-bottom pb-1">Basic Info</h6>
        <p><b>Gender:</b> {{ doctor.gender }}</p>
        <p><b>Age:</b> {{ doctor.age }}</p>
        <p><b>Email:</b> {{ doctor.email }}</p>
        <p><b>Contact:</b> {{ doctor.contact }}</p>
      </div>

      
      <div class="mb-3">
        <h6 class="fw-semibold border-bottom pb-1">Professional Info</h6>
        <p><b>Department:</b> {{ doctor.department }}</p>
        <p><b>Roles:</b> {{ doctor.roles }}</p>
        <p><b>Qualification:</b> {{ doctor.qualification }}</p>
        <p><b>Experience:</b> {{ doctor.experience_years || 'N/A' }} years</p>
        <p><b>Registration No:</b> {{ doctor.registration_number }}</p>
      </div>

      
      <div class="mb-3">
        <h6 class="fw-semibold border-bottom pb-1">Hospital Details</h6>
        <p><b>Room:</b> {{ doctor.room_number }}</p>
        <p><b>OPD Timing:</b> {{ doctor.opd_timing }}</p>
        <p><b>Consultation Fee:</b> ₹{{ doctor.consultation_fee }}</p>
      </div>

      
      <div class="mb-3">
        <h6 class="fw-semibold border-bottom pb-1">Languages</h6>
        <div class="d-flex flex-wrap gap-2">
          <span v-for="(lang, i) in doctor.languages_spoken" :key="i" class="badge bg-light text-dark border">
            {{ lang }}
          </span>
        </div>
      </div>

      <div class="mb-4">
        <h6 class="fw-semibold border-bottom pb-1">Bio</h6>
        <p class="small text-muted">
          {{ doctor.bio || 'No bio provided.' }}
        </p>
      </div>


      <div class="d-flex gap-2 mt-3">
        <Btn label="Print" class="btn-outline-secondary btn-sm" />
        <Btn label="Close" class="btn-outline-dark btn-sm" @click="emit('close')" />
      </div>
    </div>
  </div>
</template>
