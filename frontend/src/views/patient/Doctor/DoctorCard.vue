<script setup>
    import Badge from '@/components/common/Badge.vue'
    import Btn from '@/components/common/Btn.vue'
    import { useAppointmentStore } from '@/stores/appointment.store'
    import { computed } from 'vue'

    const appointment=useAppointmentStore()

    const props=defineProps({
        doctor: Object
    })
    const emit=defineEmits(['doctor-appt'])
    const parseQualifications = (qual) => {
        try {
            return typeof qual === 'string' ? JSON.parse(qual) : qual
        } catch {
            return []
        }
    }

    const bookable=computed(()=>{
        return props.doctor.is_bookable
    })
    async function cancelMyAppointment() {
        if (!appointment.activeAppointment) return

        const confirmCancel = confirm("Are you sure you want to cancel?")
        if (!confirmCancel) return

        await appointment.cancelBookedAppointment(appointment.activeAppointment.id,{reason:"Cancelled by patient"})
        showModal.value = false
    }
</script>

<template>
  <div class=" doctor-card card position-relative">
    <div class="row g-0">
      
      <div class="col-md-4 doctor-card-img ">
        <img :src="doctor.profile_image || '/doctor-placeholder.png'" class="img-fluid rounded-start " alt="Doctor" />
        <div class="position-absolute doctor-card-badge1 " >
            <Badge v-if="doctor.emergency_available" color="success" label="Emergency Available" />
            <Badge v-else color="danger" label="Emergency unavailable" />
        </div>
      </div>

      
      <div class="col-md-8">
        <div class="card-body">
          <div class="d-flex justify-content-between align-items-start mb-2">
            <div>
                <div class="d-flex ">
                    <h5 class="card-title me-3">
                        Dr. {{ doctor.name }}
                    </h5>
                    <div>
                        <Badge v-for="qual in parseQualifications(doctor.qualification)" :key="qual.degree" :label="qual.degree" color="info" class="mb-2 me-2"/>
                    </div>
                </div>
                <div class="text-muted  mb-1 text-capitalize">
                    <small class="" >
                        {{ doctor.specialization }},
                    </small>
                    <small>
                        {{ doctor.roles }}
                    </small>
              </div>
            </div>
            <div v-if="(appointment.activeAppointment && appointment.activeAppointment.doctor.id == props.doctor.id)" >
                <Badge label="Active Booking" color="info" class="d-block mb-2" />
                <Badge label="Reschedule Only" color="warning"  />
                    
            </div>
            <Badge v-else :label="bookable ? 'Booking Open' : 'Booking closed'" :color="bookable ? 'success':'danger'"/>  
          </div>

          <div class="mb-2">
            <p class="text-primary  fw-semibold small mb-0">
                Department : {{ doctor.department }}
              </p>
          </div>

          <p class="small mb-2 text-muted fst-italic text-truncate" style="max-width: 600px;" v-if="doctor.bio">
            "{{ doctor.bio }}"
          </p>
          

          <div class="row g-2 small mb-2">
            <div class="col-6">
              <strong>Experience (years): </strong> <mark>{{ doctor.experience_years ||'Not Provided'  }} </mark>  
            </div>
            <div class="col-6">
              <strong>Age (years) :</strong> {{ doctor.age || 'Not Provided'  }} 
            </div>
            <div class="col-6">
              <strong class="text-capitalize">Gender : {{ doctor.gender || 'Not Provided' }} </strong> 
            </div>
            <div class="col-6">
              <strong>Room:</strong> {{ doctor.room_number || 'Not Provided'  }}
            </div>
            <div class="col-6">
              <strong>Fee (₹):</strong> {{ doctor.consultation_fee || 'Not Provided'  }}
            </div>
          </div>

          <p class="small mb-2">
            <strong>OPD :</strong> {{ doctor.opd_timing || 'Not Provided'  }}
          </p>

          <p class="text-capitalize mb-2">
            <strong>Languages : </strong> 
            <span v-for="(lang, index) in doctor.languages_spoken" :key="lang" v-if="doctor.languages_spoken.length !=0">
              {{ lang }}<span v-if="index < doctor.languages_spoken.length - 1">, </span>
            </span>
            <span v-else class="text-muted small">
              Not Provided
            </span>
          </p>
          <div v-if="appointment.activeAppointment && appointment.activeAppointment.doctor.id == props.doctor.id" class="d-flex ">
            <Btn label="Reschedule" class="btn-warning me-2" @click="emit('doctor-appt')"/>
            <Btn label="Cancel Appointment" class="btn-outline-danger" @click="cancelMyAppointment"/>
          </div >
          <Btn v-else label="Book Appointment" class="btn-primary" :disabled="!bookable" @click="emit('doctor-appt')" />
        </div>
      </div>
    </div>
  </div>
  
</template>

