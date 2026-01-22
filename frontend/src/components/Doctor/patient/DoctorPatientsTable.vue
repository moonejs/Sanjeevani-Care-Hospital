<script setup>
    import BaseTable from '@/components/layout/BaseTable.vue'
    import BaseTableHead from '@/components/layout/BaseTableHead.vue'
    import DoctorDashTableCaption from '@/components/Doctor/DoctorDashTableCaption.vue'
    import DoctorPatientsRow from './DoctorPatientsRow.vue';
    import { ref } from 'vue'

    defineProps({
        patients: Array,
        total: Number,
        loading:Boolean
    })

    const tHead = ref(['Name','Age','Gender','Last Visit','Total Visits','Active','Action'])
</script>

<template>
  <BaseTable>
    <template #caption>

      <DoctorDashTableCaption title="Patients" stats="title" :table-stats-arr="[{ 'Total Patients': total }]"/>

    </template>

    <template #head>
      <BaseTableHead :t-head="tHead" />
    </template>

    <template #body>
      <tr v-if="loading">
        <td colspan="7" class="text-center text-muted">
          Loading patients...
        </td>
      </tr>

      <DoctorPatientsRow v-for="(patient, index) in patients" :key="patient.patient_id" :patient="patient" :index="index" />

      <tr v-if="!loading && !patients.length">
        <td colspan="7" class="text-center text-muted">
          No patients found
        </td>
      </tr>
    </template>
  </BaseTable>
</template>
