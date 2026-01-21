<script setup>
    import BaseTable from '../layout/BaseTable.vue';
    import BaseTableHead from '../layout/BaseTableHead.vue';
    import { onMounted, ref,computed } from 'vue';
    import DoctorDashTableCaption from './DoctorDashTableCaption.vue';
    import { useDoctorStore } from '@/stores/doctor.store';
    import { useAppointmentStore } from '@/stores/appointment.store';
    import AssignedPatientRows from './AssignedPatientRows.vue';


    const appointment=useAppointmentStore()
    const doctor=useDoctorStore()
    const tHead=ref(["Name","Age","Gender","Last Visit","Visits","Action"])
    

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
            <DoctorDashTableCaption title="Assigned Patients" stats="title" :table-stats-arr="tableStatsArr"/>
        </template>

        <template #head>
            <BaseTableHead :t-head="tHead"/>
        </template>

        <template #body>
            <AssignedPatientRows 
            v-for="(patient,index) in doctor.assignedPatientsList" :key="patient.patient_id "
            :patient="patient" :index="index" 
            />
        </template>

    </BaseTable>
</template>