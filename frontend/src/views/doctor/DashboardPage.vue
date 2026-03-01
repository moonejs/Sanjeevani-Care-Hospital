<script setup>
    import DoctorAppointmentsTable from '@/components/Doctor/DoctorAppointmentsTable.vue';
    import AssignedPatientTable from '@/components/Doctor/AssignedPatientTable.vue';
    import { ref,onMounted } from 'vue';
    import { useAppointmentStore } from '@/stores/appointment.store';
    import { useDoctorStore } from '@/stores/doctor.store';
    import NextAppointmentCard from '@/components/Doctor/NextAppointmentCard.vue';
    import Time from '@/components/Doctor/Time.vue';
    
    const appointment=useAppointmentStore()
    const doctor=useDoctorStore()

    onMounted(async()=>{
        const today = appointment.formatDate(appointment.today)
        appointment.selectedDate = today
        await appointment.fetchAppointmentsByDoctor(today)
        doctor.refreshDoctor()
        setInterval(async () => {
            await appointment.fetchAppointmentsByDoctor(today)
            await doctor.refreshDoctor()
        }, 15000)
    })

    const tHeadArray=ref([])
    tHeadArray.value=["Time","Patients","Status","Type","Actions"]


</script>

<template>
    <div class="container-fluid bg-danger-subtle d-flex">
        <Time/>
        <div class=" bg-success-subtle doctor-dashboard-table-1">
            <DoctorAppointmentsTable/>
        </div>
        <div class="bg-warning-subtle position-absolute doctor-dashboard-table-2">
            <AssignedPatientTable/>
        </div>

        <NextAppointmentCard class="position-absolute next-app-card"/>
    </div>
</template>