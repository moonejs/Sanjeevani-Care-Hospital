<script setup>
    import { onMounted } from 'vue'
    import { useDoctorStore } from '@/stores/doctor.store'
    import DoctorPatientsTable from '@/components/Doctor/patient/DoctorPatientsTable.vue';
    import Pagination from '@/components/common/Pagination.vue';
    import LoadingState from '@/components/common/LoadingState.vue';
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
        <LoadingState :loading="doctor.loading">

            <div class="container-fluid" v-if="doctor.patients.length !=0">
                <DoctorPatientsTable
                :patients="doctor.patients"
                :total="doctor.totalPatients"
                :loading="doctor.loading"
                />
                <Pagination :pagination="doctor.historyPagination" @change="changePage"/>
            </div>

            <h2 v-else class="text-muted text-center mt-10">No Patients Found</h2>
        </LoadingState>

    </div>
</template>
