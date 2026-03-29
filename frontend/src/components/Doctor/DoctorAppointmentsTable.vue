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
    import LoadingState from '../common/LoadingState.vue'
    import Btn from '../common/Btn.vue'
    import { useToastStore } from '@/stores/toast.store';

    const appointment = useAppointmentStore()
    const showCompleteModal=ref(false)
    const selectedPatient=ref(null)
    const selectedAppointmentId = ref(null)
    const toast = useToastStore()
    

    const {appointmentListByDoctor} = storeToRefs(appointment)
    const dateFilter=ref(null)
    const statusFilter=ref(null)
    const { searchQuery, filteredData } = useSearchFilter(
        appointmentListByDoctor,
        ['patient.name'],
        {
          date:dateFilter,
          status:statusFilter
        }
        
    )

    const navArray=ref(["Today","This Week"])
    const tHead=ref(["Time","Slot","Patient","Type","Status","Action"])
    const tHead2=ref(["Time","Date","Slot","Patient","Type","Status","Action"])
    const tHeadClasses=ref(["","","","","",""])

    onMounted(async () => {
      const today = appointment.formatDate(appointment.today)
      appointment.selectedDate = today
      await appointment.fetchAppointmentsByDoctor(today,"today")
    })

    async function updateStatus(app,status){
      try {
        await appointment.updateAppointmentStatus(app.appointment_id,status)
        toast.addToast({
            message: `Appointment ${status} Successfully.`,
            type: 'success'
        })
      } catch (error) {
        toast.addToast({
                message: 'Some Error Occured',
                type: 'error'
            })
      }

      
    }

    function openCompleteModal(app){
      showCompleteModal.value=true
      selectedPatient.value=app.patient
      selectedAppointmentId.value = app.appointment_id
    }
    async function completeVisit(payload){
      try {
        showCompleteModal.value = false
        await appointment.completeAppointment(selectedAppointmentId.value,payload)
        toast.addToast({
                message: 'Appointment Completed Succesfully.',
                type: 'success'
            })
        
      } catch (error) {
        toast.addToast({
                message: 'Some Error Occured',
                type: 'error'
            })
      }
      
    }
    const tableStatsArr=computed(()=>{
      return [appointment.appointmentSummary] 
    })

    async function showTodayOrWeek(range){
      appointment.selectedRange = range
      const today = appointment.formatDate(appointment.today)

      await appointment.fetchAppointmentsByDoctor(today, range)
    }
</script>

<template>
  <BaseTable>
    <template #caption>
      <DoctorDashTableCaption  title="Upcoming Appointments" :nav-array="navArray" stats="navs" @today-or-week="showTodayOrWeek" :table-stats-arr="tableStatsArr" v-model:searchQuery="searchQuery"  placeholder="Search Appointments..." :is-date="appointment.selectedRange=='week'" v-model:date-filter="dateFilter" :is-dropdown="true" filter-drop-label="Status" :filter-drop="statusFilter" :filter-drop-options="['pending','completed','cancelled','confirmed']" v-model:filter-drop="statusFilter" class3="d-flex gap-2 ms-5" class4="w-100 ms-4" class2=""/>

      
    </template>

    <template #head>
      <BaseTableHead :t-head="appointment.selectedRange === 'today' ? tHead : tHead2" :t-head-classes="tHeadClasses"/>
    </template>
    
    <template #body>
      <LoadingState :loading="appointment.loading" class=" position-absolute ms-12 ps-5  top-5 ">
        <h5 class="text-muted position-absolute ms-11 mt-4" v-if="filteredData.length ==0">No Upcoming Appointments</h5>
        <DoctorAppointmentRow v-else
        v-for="(app,index) in filteredData"
        :key="app.appointment_id"
        :appointment="app" :index="index"
        @confirm="updateStatus(app,'confirmed')"
        @complete="openCompleteModal(app)"
        @cancel="updateStatus(app,'cancelled')"
        />
      </LoadingState>
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
