
<script setup>
    import BaseTable from '@/components/layout/BaseTable.vue'
    import BaseTableHead from '@/components/layout/BaseTableHead.vue'
    import PatientAppointmentsRow from './PatientAppointmentsRow.vue'

    defineProps({
        appointments: Array,
        loading: Boolean
    })

    const emit = defineEmits(['view'])

    const tHead = [ 'Date', 'Time', 'Doctor', 'Department', 'Type', 'Status', 'Action' ]
</script>

<template>
  <BaseTable>
    <template #head>
      <BaseTableHead :t-head="tHead" />
    </template>

    <template #body>
      <tr v-if="loading">
        <td colspan="7" class="text-center text-muted">
          Loading appointments...
        </td>
      </tr>

      <PatientAppointmentsRow v-for="(appt, i) in appointments" :key="appt.id" :appointment="appt" :index="i" @view="emit('view', appt)" />

      <tr v-if="!loading && !appointments.length">
        <td colspan="7" class="text-center text-muted">
          No appointments found
        </td>
      </tr>
    </template>
  </BaseTable>
</template>
