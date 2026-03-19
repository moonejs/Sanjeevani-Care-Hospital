<script setup>
    import BaseTable from '@/components/layout/BaseTable.vue'
    import BaseTableHead from '@/components/layout/BaseTableHead.vue'
    import DoctorDashTableCaption from '@/components/Doctor/DoctorDashTableCaption.vue'
    import DoctorPatientsRow from './DoctorPatientsRow.vue';
    import { ref } from 'vue'
    import { useDoctorStore } from '@/stores/doctor.store'
    import { useSearchFilter } from '@/utils/useSearchFilter';
    import { storeToRefs } from 'pinia';

    defineProps({
        total: Number,
        loading:Boolean
    })

    const doctorStore=useDoctorStore()

    const {patients} = storeToRefs(doctorStore)
    const { searchQuery, filteredData } = useSearchFilter(
        patients,
        ['name'],
        
    )



    const tHead = ref(['Name','Age','Gender','Last Visit','Total Visits','Active','Action'])
</script>

<template>
  <BaseTable>
    <template #caption>

      <DoctorDashTableCaption title="Patients" stats="title" :table-stats-arr="[{ 'Total Patients': total }]" v-model:searchQuery="searchQuery" class1="ms-12 ps-12" class2="gap-12"/>

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

      <DoctorPatientsRow v-for="(patient, index) in filteredData" :key="patient.patient_id" :patient="patient" :index="index" />

      <tr v-if="!loading && !patients.length">
        <td colspan="7" class="text-center text-muted">
          No patients found
        </td>
      </tr>
    </template>
  </BaseTable>
</template>
