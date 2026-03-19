
<script setup>
    import BaseTable from '@/components/layout/BaseTable.vue'
    import BaseTableHead from '@/components/layout/BaseTableHead.vue'
    import PatientAppointmentsRow from './PatientAppointmentsRow.vue'
    import DoctorDashTableCaption from '../Doctor/DoctorDashTableCaption.vue'
    import { usePatientStore } from '@/stores/patient.store'
    import { useSearchFilter } from '@/utils/useSearchFilter';
    import { storeToRefs } from 'pinia';
    import Btn from '../common/Btn.vue'
    import { ref } from 'vue'

    const patientStore = usePatientStore()

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
</script>

<template>
  <BaseTable>
    <template #caption>
      <DoctorDashTableCaption title="Appointments" v-model:searchQuery="searchQuery" v-model:date-filter="dateFilter" :is-date="true"/>
      <Btn  label="Clear" class="btn-primary "  @click="searchQuery = ''; statusFilter = '' ;dateFilter=''"/>
    </template>
    <template #head>
      <BaseTableHead :t-head="tHead" />
    </template>

    <template #body>
      <tr v-if="loading">
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
