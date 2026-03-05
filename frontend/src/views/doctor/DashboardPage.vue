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
  <div class="container-fluid py-4" style="min-height: 90vh;">
    
    <div class="d-flex justify-content-between align-items-end mb-4 px-2">
      <div>
        <h2 class="fw-normal">Dashboard</h2>
        <p class="text-muted mb-0">Overview of your clinic today</p>
      </div>
      <div class="text-end">
        <Time /> </div>
    </div>

    <div class="row g-4">
      <div class="col-lg-8">
        <div class="ga-card p-3 h-100">
          <DoctorAppointmentsTable />
        </div>
      </div>

      <div class="col-lg-4">
        <div class="d-flex flex-column gap-4">
          
          <div class="ga-card  border-start ">
             <NextAppointmentCard />
          </div>

          <div class="ga-card p-3">
            <AssignedPatientTable />
          </div>

        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* We remove the old .doctor-dashboard-table-1, table-2 absolute positioning */
/* The layout is now handled by Bootstrap's 'row' and 'col' classes */
.container-fluid {
  background-color: var(--hms-bg-canvas);
}
</style>