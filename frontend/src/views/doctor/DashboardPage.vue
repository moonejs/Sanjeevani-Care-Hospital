<script setup>
    import DoctorAppointmentsTable from '@/components/Doctor/DoctorAppointmentsTable.vue';
    import { ref,onMounted } from 'vue';
    import { useAppointmentStore } from '@/stores/appointment.store';

    const appointment=useAppointmentStore()

    onMounted(async()=>{
        const today = appointment.formatDate(appointment.today)
        appointment.selectedDate = today
        await appointment.fetchAppointmentsByDoctor(today)
    })

    const tHeadArray=ref([])
    tHeadArray.value=["Time","Patients","Status","Type","Actions"]


</script>

<template>
    <div class="container-fluid">
        <div class="  doctor-dashboard-table-1">
            <DoctorAppointmentsTable/>
        </div>
    </div>
</template>