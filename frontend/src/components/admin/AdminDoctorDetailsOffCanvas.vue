<script setup>
    import Btn from '../common/Btn.vue';
    import { watch,onMounted } from 'vue';
    import Badge from '../common/Badge.vue';
    import { useToastStore } from '@/stores/toast.store';
    import { useAdminStore } from '@/stores/admin.store';

    const toast = useToastStore()
    const adminStore=useAdminStore()
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

   async function downloadPdf(){
      try {
        await adminStore.downloadDoctorPdf(props.doctor.id)
        
        toast.addToast({
          message: 'Pdf Report Downloaded successfully',
          type: 'success'
        })
        
      } catch (error) {
        toast.addToast({
          title: 'Error',
          message: 'Failed to Download Appointment Report',
          type: 'error'
        })
      }
    }
</script>

<template>
  <div class="offcanvas offcanvas-end" tabindex="-1" id="appointmentOffcanvas">
    <div class="offcanvas-header border-bottom">
      <h5 class="offcanvas-title">Doctor Details</h5>
      <button type="button" class="btn-close" @click="emit('close')" aria-label="Close"></button>
    </div>

    <div class="offcanvas-body" v-if="doctor">
      
      <div class="text-center mb-4">
        <img :src="doctor.profile_image" class="rounded-circle border" style="width: 100px; height: 100px; object-fit: cover" />
        <h5 class="mt-2 mb-0">Dr. {{ doctor.name }}</h5>
        <small class="text-muted">{{ doctor.specialization }}</small>
        
        <div class="mt-2">
          <Badge :label="doctor.profile_completed ? 'Profile Completed' : 'profile Incomlete'" :color="doctor.profile_completed ? 'success':'warning'" class="me-3"/>
          
          <Badge :label="doctor.emergency_available ? 'Emergency Available' : 'Emergency Not Available'" :color="doctor.emergency_available ? 'primary':'danger'"/>
          
        </div>
      </div>

      <hr>
      <div class="mb-3 ">
        <p> <span class="small fw-bold">Gender : </span>  <span class="small">{{ doctor.gender || 'Not Provided'}}</span> </p>
        <p><span class="small fw-bold">Age : </span> <span class="small">{{ doctor.age || "Not Provided" }}</span></p>
        <p><span class="small fw-bold">Email : </span> <span class="fw-bold small">{{ doctor.email }}</span></p>
        <p><span class="small fw-bold">Contact : </span> <span class="small">{{ doctor.contact ?? 'Not Provided' }}</span></p>
      </div>

      <hr>
      <div class="mb-3">
        <p><span class="small fw-bold">Department : </span> <span class="small">{{ doctor.department || 'Not Provided' }}</span></p>
        <p><span class="small fw-bold">Roles : </span> <span class="small">{{ doctor.roles || 'Not Provided' }}</span></p>
        <p><span class="small fw-bold">Qualification : </span> <span class="small">{{ doctor.qualification || 'Not Provided' }}</span></p>
        <p><span class="small fw-bold">Experience (years) : </span> <span class="small">{{ doctor.experience_years ?? 'Not Provided' }}</span></p>
        <p><span class="small fw-bold">Registration No : </span> <span class="small fw-bold">{{ doctor.registration_number || 'Not Provided' }}</span></p>
      </div>

      <hr>
      <div class="mb-3">
        <p><span class="small fw-bold">Room : </span> <span class="small">{{ doctor.room_number ?? 'Not Provided' }}</span></p>
        <p><span class="small fw-bold">OPD Timing : </span> <span class="small">{{ doctor.opd_timing ?? 'Not Provided'}}</span></p>
        <p><span class="small fw-bold">Consultation Fee (₹) : </span> <span class="small"> <mark>{{ doctor.consultation_fee ?? 'Not Provided'}}</mark></span></p>
      </div>

      
      <div class="mb-3">
        <h6 class="fw-semibold border-bottom pb-1 small">Languages</h6>
        <div class="d-flex flex-wrap gap-2">
          <span v-if="doctor.languages_spoken.length !=0" v-for="(lang, i) in doctor.languages_spoken" :key="i" class="badge bg-light text-dark border">
            {{ lang }}
          </span>
          <span v-else class="text-muted small">No Languages Provided</span>
        </div>
      </div>

      <div class="mb-4">
        <h6 class="fw-semibold border-bottom pb-1">Bio</h6>
        <p class="small text-muted">
          {{ doctor.bio || 'No bio provided.' }}
        </p>
      </div>


      <div class="d-flex gap-2 mt-3">
         <Btn :label="adminStore.pdfLoading ? 'Generating...' : 'Download Report'" :loader="adminStore.pdfLoading" class="btn-outline-primary btn-sm" @click="downloadPdf"/>

        <Btn label="Close" class="btn-outline-dark btn-sm" @click="emit('close')" />
      </div>
    </div>
  </div>
</template>
