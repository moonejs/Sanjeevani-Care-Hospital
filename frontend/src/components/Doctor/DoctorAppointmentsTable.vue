<script setup>
    import { onMounted,ref } from 'vue'
    import { useAppointmentStore } from '@/stores/appointment.store'
    import DoctorDashTableCaption from './DoctorDashTableCaption.vue'
    import BaseTableHead from '../layout/BaseTableHead.vue'
    import DoctorAppointmentRow from './DoctorAppointmentRow.vue'
    import BaseTable from '../layout/BaseTable.vue'
    import CompleteModal from '@/views/doctor/CompleteModal.vue'

    const appointment = useAppointmentStore()
    const showCompleteModal=ref(false)
    const selectedPatient=ref(null)
    const selectedAppointmentId = ref(null)
    

    const navArray=ref(["Today","This Week"])
    const tHead=ref(["Time","Slot","Patient","Status","Type","Action"])

    onMounted(async () => {
      const today = appointment.formatDate(appointment.today)
      appointment.selectedDate = today
      await appointment.fetchAppointmentsByDoctor(today)
    })

    async function updateStatus(app,status){
      await appointment.updateAppointmentStatus(app.appointment_id,status)

      
    }

    function openCompleteModal(app){
      showCompleteModal.value=true
      selectedPatient.value=app.patient
      selectedAppointmentId.value = app.appointment_id
    }
    async function completeVisit(payload){
      await appointment.completeAppointment(selectedAppointmentId.value,payload)
      showCompleteModal.value = false
      
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
      @complete="openCompleteModal(app)"
      @cancel="updateStatus(app,'cancelled')"
      />
    </template>
  </BaseTable>
  <CompleteModal
    :show-complete-modal="showCompleteModal"
    :patient="selectedPatient"
    :appointment-id="selectedAppointmentId"
    @close="showCompleteModal = false"
    @submit="completeVisit"
  />
</template>
