<script setup>
    import { onMounted, ref } from 'vue'
    import { useRoute } from 'vue-router'

    import { useDoctorStore } from '@/stores/doctor.store'
    import PatientSummery from '@/components/Doctor/patient/PatientSummery.vue'
    import PatientStats from '@/components/Doctor/patient/PatientStats.vue'
    import PatientTabs from './PatientTabs.vue'
    const doctor=useDoctorStore()
    const route = useRoute()
    const profile = ref(null)
    const patient_id=route.params.id

    onMounted(async () => {
        await doctor.fetchPatientProfile(patient_id)
        profile.value=doctor.selectedPatient
    })
</script>

<template>
    <div class="patient-profile-layout d-flex">
      <div v-if="profile" class="patient-profile-left-panel bg-danger">
        <PatientSummery  :patient="profile.patient"/>
        <PatientStats :stats="profile.stats" /> 
      </div >
  
      <div v-if="profile" class="patient-profile-right-panel bg-success-subtle">
        <PatientTabs
        :current-appointment="profile.current_appointment"
        :appointments="profile.appointments"
        :treatments="profile.treatments"
        />  
      
      </div> 
    </div>


</template>
