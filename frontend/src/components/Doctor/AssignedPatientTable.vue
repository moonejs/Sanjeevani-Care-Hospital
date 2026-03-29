<script setup>
    import BaseTable from '../layout/BaseTable.vue';
    import BaseTableHead from '../layout/BaseTableHead.vue';
    import { onMounted, ref,computed } from 'vue';
    import DoctorDashTableCaption from './DoctorDashTableCaption.vue';
    import { useDoctorStore } from '@/stores/doctor.store';
    import { useAppointmentStore } from '@/stores/appointment.store';
    import AssignedPatientRows from './AssignedPatientRows.vue';
    import { useSearchFilter } from '@/utils/useSearchFilter';
    import { storeToRefs } from 'pinia';
    import LoadingState from '../common/LoadingState.vue';

    const appointment=useAppointmentStore()
    const doctor=useDoctorStore()
    const tHead=ref(["Name","Last Visit","Visits","Action"])
    
    const {assignedPatientsList} =storeToRefs(doctor)
    const { searchQuery, filteredData } = useSearchFilter(
        assignedPatientsList,
        ['name'],
        
    )



    const tableStatsArr = computed(() => [
    { "Total Patients": doctor.totalAssignedPatients }
    ])
    onMounted(async ()=>{
        await refreshAssignedPatients()
    })
    async function refreshAssignedPatients() {
        const today = appointment.formatDate(appointment.today)
        await doctor.fetchAssignedTodayPatientsDetails(today)
    }




</script>
<template>
    <BaseTable>
        <template #caption>
            <DoctorDashTableCaption title="Assigned Patients" stats="title" :table-stats-arr="tableStatsArr" v-model:searchQuery="searchQuery"/>
        </template>

        <template #head>
            <BaseTableHead :t-head="tHead"/>
        </template>

        <template #body>
            <LoadingState :loading="doctor.loading" class="position-absolute end-0 me-11 top-9 ">
                <h6 class="text-muted position-absolute ms-8 mt-2" v-if="filteredData.length ==0">No Assigned Patients</h6>
                
                <AssignedPatientRows v-else
                v-for="(patient,index) in filteredData" :key="patient.patient_id "
                :patient="patient" :index="index" 
                />
            </LoadingState>
        </template>

    </BaseTable>
</template>