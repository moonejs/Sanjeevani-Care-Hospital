<script setup>
    import { onMounted,ref } from 'vue'
    import { useAppointmentStore } from '@/stores/appointment.store'
    import DoctorDashTableCaption from './DoctorDashTableCaption.vue'
    import BaseTableHead from '../layout/BaseTableHead.vue'
    import DoctorAppointmentRow from './DoctorAppointmentRow.vue'
    import BaseTable from '../layout/BaseTable.vue'
    const appointment = useAppointmentStore()


    const navArray=ref(["Today","This Week"])
    const tHead=ref(["Time","Slot","Patient","Status","Type","Action"])

    onMounted(async () => {
      const today = appointment.formatDate(appointment.today)
      appointment.selectedDate = today
      await appointment.fetchAppointmentsByDoctor(today)
    })
</script>

<template>
  <BaseTable>
    <template #caption>
      <DoctorDashTableCaption  title="Upcoming Appointments" :nav-array="navArray"/>

    </template>

    <template #head>
      <BaseTableHead :t-head="tHead"/>
    </template>
    
    <template #body>
      <DoctorAppointmentRow 
      v-for="(app,index) in appointment.appointmentListByDoctor"
      :key="app.appointment_id"
      :appointment="app" :index="index"/>
    </template>
    
  </BaseTable>
</template>
