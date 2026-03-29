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
  <div class="container-fluid patient-page px-3 py-2">

    <div class="row h-100">
        <div v-if="profile" class="col-4 border-end pe-3 d-flex flex-column">
            <PatientSummery :patient="profile.patient"/>
            <PatientStats :stats="profile.stats"/>

        </div>
      <div v-if="profile" class="col-8 ps-3 d-flex flex-column">
            <PatientTabs :current-appointment="profile.current_appointment" :appointments="profile.appointments" :treatments="profile.treatments"/>

      </div>

    </div>

  </div>
</template>
