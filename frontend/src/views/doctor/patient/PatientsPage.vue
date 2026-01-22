<script setup>
    import { onMounted } from 'vue'
    import { useDoctorStore } from '@/stores/doctor.store'
    import DoctorPatientsTable from '@/components/Doctor/patient/DoctorPatientsTable.vue';
    import Pagination from '@/components/common/Pagination.vue';
    const doctor = useDoctorStore()

    onMounted(() => {
        doctor.fetchDoctorPatientsList()
    })
    function changePage(page) {
        appointment.fetchDoctorAppointmentHistory(page)
    }

</script>

<template>
    <div>
        <div class="bg-info doctor-appointment-filter">
            filter
        </div>
        <div class="container-fluid">
          <DoctorPatientsTable
            :patients="doctor.patients"
            :total="doctor.totalPatients"
            :loading="doctor.loading"
          />
          <Pagination :pagination="doctor.historyPagination" @change="changePage"/>
        </div>

    </div>
</template>
