<script setup>
    import { computed, onMounted,ref } from 'vue'
    import { useAppointmentStore } from '@/stores/appointment.store'
    import DoctorDashTableCaption from './DoctorDashTableCaption.vue'
    import BaseTableHead from '../layout/BaseTableHead.vue'
    import DoctorAppointmentRow from './DoctorAppointmentRow.vue'
    import BaseTable from '../layout/BaseTable.vue'
    import CompleteModal from '@/views/doctor/CompleteModal.vue'
    import { useSearchFilter } from '@/utils/useSearchFilter';
    import { storeToRefs } from 'pinia';

    const appointment = useAppointmentStore()
    const showCompleteModal=ref(false)
    const selectedPatient=ref(null)
    const selectedAppointmentId = ref(null)
    

    const {appointmentListByDoctor} = storeToRefs(appointment)
    const { searchQuery, filteredData } = useSearchFilter(
        appointmentListByDoctor,
        ['patient.name'],
        
    )

    const navArray=ref(["Today","This Week"])
    const tHead=ref(["Time","Slot","Patient","Status","Type","Action"])
    const tHeadClasses=ref(["","","","","",""])

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
    const tableStatsArr=computed(()=>{
      return [appointment.appointmentSummary] 
    })
</script>

<template>
  <BaseTable>
    <template #caption>
      <DoctorDashTableCaption  title="Upcoming Appointments" :nav-array="navArray" stats="navs" :table-stats-arr="tableStatsArr" v-model:searchQuery="searchQuery" class1="ms-12 ps-8"/>

    </template>

    <template #head>
      <BaseTableHead :t-head="tHead" :t-head-classes="tHeadClasses"/>
    </template>
    
    <template #body>
      <h2 class="text-muted position-absolute ms-9 mt-4" v-if="appointment.appointmentListByDoctor.length ==0">No Upcoming Appointments</h2>
      <DoctorAppointmentRow v-else
      v-for="(app,index) in filteredData"
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
