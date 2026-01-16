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

    async function updateStatus(app,status){
      await appointment.updateAppointmentStatus(app.appointment_id,status)
      await appointment.fetchAppointmentsByDoctor(appointment.selectedDate)
    }
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
      :appointment="app" :index="index"
      @confirm="updateStatus(app,'confirmed')"
      @complete="updateStatus(app,'completed')"
      @cancel="updateStatus(app,'cancelled')"
      />
    </template>
    
  </BaseTable>
</template>
