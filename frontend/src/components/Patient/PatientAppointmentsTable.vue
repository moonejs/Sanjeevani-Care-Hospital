
<script setup>
    import BaseTable from '@/components/layout/BaseTable.vue'
    import BaseTableHead from '@/components/layout/BaseTableHead.vue'
    import PatientAppointmentsRow from './PatientAppointmentsRow.vue'
    import DoctorDashTableCaption from '../Doctor/DoctorDashTableCaption.vue'
    import { usePatientStore } from '@/stores/patient.store'
    import { useSearchFilter } from '@/utils/useSearchFilter';
    import { storeToRefs } from 'pinia';
    import { useToastStore } from '@/stores/toast.store';
    import Btn from '../common/Btn.vue'
    import { ref } from 'vue'

    const patientStore = usePatientStore()
    const toast = useToastStore()

    const {patientAppointmentHistory}=storeToRefs(patientStore)
    const dateFilter = ref('')
    const { searchQuery, filteredData } = useSearchFilter(
        patientAppointmentHistory,
        ['doctor.name'],
        {
            date:dateFilter
        }
    )

    defineProps({
        appointments: Array,
        loading: Boolean
    })

    const emit = defineEmits(['view'])

    const tHead = [ 'Date', 'Time', 'Doctor', 'Department', 'Type', 'Status', 'Action' ]

    async function exportTreatment(){
      try {
        await patientStore.exportPatientTreatment()
        toast.addToast({
          message: 'Downloaded Csv successfully',
          type: 'success'
        })
      } catch (error) {
        toast.addToast({
          title: 'Error',
          message: 'Failed to Download csv',
          type: 'error'
        })
      }

    }

    
</script>

<template>
  <BaseTable>
    <template #caption>
      <DoctorDashTableCaption title="Appointments" v-model:searchQuery="searchQuery" v-model:date-filter="dateFilter" :is-date="true" class2=" gap-12 " class1="" class3="d-flex ms-9 ps-5  gap-4 align-items-center"/>
      <Btn  label="Clear" class="btn-primary btn-sm position-absolute right-9 top-6 mt-3 me-6"  @click="searchQuery = ''; statusFilter = '' ;dateFilter=''"/>
      
      <Btn  :label="patientStore.exportLoading? 'Exporting...' : 'Export csv'" :loader="patientStore.exportLoading" @click="exportTreatment" class="btn-outline-primary btn-sm position-absolute right-7 top-6 mt-3"/>
    </template>
    <template #head>
      <BaseTableHead :t-head="tHead" />
    </template>

    <template #body>
      <tr v-if="loading  && !patientStore.exportLoading">
        <td colspan="7" class="text-center text-muted">
          Loading appointments...
        </td>
      </tr>

      <PatientAppointmentsRow v-for="(appt, i) in filteredData" :key="appt.id" :appointment="appt" :index="i" @view="emit('view', appt)" />

      <tr v-if="!loading && !appointments.length">
        <td colspan="7" class="text-center text-muted">
          No appointments found
        </td>
      </tr>
    </template>
  </BaseTable>
</template>

<style scoped>

</style>
