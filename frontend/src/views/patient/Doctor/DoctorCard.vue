<script setup>
    import Badge from '@/components/common/Badge.vue'
    import Btn from '@/components/common/Btn.vue'
    import { useAppointmentStore } from '@/stores/appointment.store'
    import { computed } from 'vue'
    import { useToastStore } from '@/stores/toast.store';
    
    const appointment=useAppointmentStore()
    const toast = useToastStore()

    const props=defineProps({
        doctor: Object
    })

    const hasActiveBooking = computed(() => {
      return appointment.activeAppointments.some(
        a => a.doctor.id === props.doctor.id
      )
    })
    const activeAppointment = computed(() => {
      return appointment.activeAppointments.find(
        a => a.doctor.id === props.doctor.id
      ) || null
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
        if (!activeAppointment.value) return
        
        const confirmCancel = confirm("Are you sure you want to cancel?")
        if (!confirmCancel) {
          toast.addToast({
            title:'Error',
            message: 'Failed to Cancelled Appointment',
            type: 'error'
          })
          return
        }

        toast.addToast({
          message: 'Appointment Cancelled successfully',
          type: 'success'
        })
        console.log(activeAppointment.value.id);
        await appointment.cancelBookedAppointment(activeAppointment.value.id,{reason:"Cancelled by patient"})
        
    }
    
</script>

<template>
  <div class=" doctor-card mb-4 animate-up-1 border   rounded-1 position-relative ">
    <div class="row g-0">
      
      <div class="col-md-4 doctor-card-img ">
        <img :src="doctor.profile_image || '/doctor-placeholder.png'" class=" rounded-start-2 " alt="Doctor" />
        <div class="position-absolute doctor-card-badge1 " >
            <Badge v-if="doctor.emergency_available" color="success" label="Emergency Available" />
            <Badge v-else color="danger" label="Emergency unavailable" />
        </div>
      </div>

      
      <div class="col-md-8">
        <div class="card-body">
          <div class="d-flex justify-content-between align-items-start ">
            <div>
                <div class="d-flex ">
                    <h5 class=" me-3">
                        Dr. {{ doctor.name }}
                    </h5>
                    <div>
                        <Badge v-for="qual in parseQualifications(doctor.qualification)" :key="qual.degree" :label="qual.degree" color="info" class="me-2 " style=" font-size: 10px;"/>
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
            <div v-if="hasActiveBooking" >
                <Badge label="Active Booking" color="primary" class="d-block mb-2" style=" font-size: 11px;"/>
                <Badge label="Reschedule Only" color="warning"  style=" font-size: 11px;"/>
                    
            </div>
            <Badge v-else :label="bookable ? 'Booking Open' : 'Booking closed'" :color="bookable ? 'success':'danger'" style=" font-size: 11px;"/>  
          </div>

          <div class="mb-1">
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
              <strong>Fee (₹):</strong> <mark> {{ doctor.consultation_fee || 'Not Provided'  }} </mark>
            </div>
          </div>
          <div class="row ">
            <p class="small mb-2 col">
              <strong>OPD :</strong> {{ doctor.opd_timing || 'Not Provided'  }}
            </p>
            
            <p class="text-capitalize mb-2 col me-3 small" >
              <strong>Languages : </strong> 
              <span v-for="(lang, index) in doctor.languages_spoken" :key="lang" v-if="doctor.languages_spoken.length !=0">
                {{ lang }}<span v-if="index < doctor.languages_spoken.length - 1">, </span>
              </span>
              <span v-else class="text-muted small">
                Not Provided
              </span>
            </p>
          </div>
          <div v-if="hasActiveBooking" class="d-flex ">
            <Btn label="Reschedule" class="btn-secondary me-2  btn-sm" @click="emit('doctor-appt')"/>
            <Btn label="Cancel Appointment" class="btn-outline-danger btn-sm" @click="cancelMyAppointment"/>
          </div >
          <Btn v-else label="Book Appointment" class="btn-secondary btn-sm" :disabled="!bookable" @click="emit('doctor-appt')" />
        </div>
      </div>
    </div>
  </div>
  
</template>



<style scoped>
.doctor-card {
  width: 57vw;
  
}
.doctor-card:hover{
  background-color: var(--hms-card-hover);
}
.doctor-card-badge1 {
  bottom: 6.5rem;
  right: 7.9rem;
}
.doctor-card-img img {
  height: 20.4rem;
  width: 100%;
  object-fit: cover;
}

</style>

