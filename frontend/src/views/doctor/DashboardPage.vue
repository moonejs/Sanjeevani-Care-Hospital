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
        
    })

    const tHeadArray=ref([])
    tHeadArray.value=["Time","Patients","Status","Type","Actions"]


</script>

<template>
    <div class="row container-fluid justify-content-between">
      <div class="col-7">
         <DoctorAppointmentsTable />
      </div>
      <div class="col-4">
        <div class="row">
          <Time />
        </div>
        <div class="row mt-4">
          <NextAppointmentCard />
        </div>
        <div class="row mt-4">
          <AssignedPatientTable />
        </div>
      </div>
    </div>

</template>

