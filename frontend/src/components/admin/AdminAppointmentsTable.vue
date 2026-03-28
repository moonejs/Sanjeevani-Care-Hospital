<script setup>
    import BaseTable from '@/components/layout/BaseTable.vue';
    import BaseTableHead from '@/components/layout/BaseTableHead.vue';
    import AdminAppointmentsTableRow from './AdminAppointmentsTableRow.vue';
    import DoctorDashTableCaption from '../Doctor/DoctorDashTableCaption.vue';

    import LoadingState from '../common/LoadingState.vue';
    import Btn from '../common/Btn.vue';
    import { storeToRefs } from 'pinia';
    import { useAdminStore } from '@/stores/admin.store';
    import { ref } from 'vue';
    import { useSearchFilter } from '@/utils/useSearchFilter';

    const adminStore = useAdminStore()

    const props = defineProps({
        appointments:Array
    })

    const emit=defineEmits(['view'])
    const tHead=ref(["Date","Time","Status","Doctor Name","Patient Name","Type","Department","Follow_up_date","Actions"])

    

    const dateFilter = ref('')
    const statusFilter=ref('')
    const {adminAppointments}=storeToRefs(adminStore)
    const { searchQuery, filteredData } = useSearchFilter(
        adminAppointments,
        ['doctor.name','patient.name'],
        {
            status:statusFilter,
            date: dateFilter
        }
    )
    async function exportAppointments(){
      try {
        await adminStore.exportAppointments()
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
    <BaseTable >
        <template #caption>
            <DoctorDashTableCaption title="Appointment History" v-model:searchQuery="searchQuery" 
            :is-dropdown="true" 
            v-model:date-filter="dateFilter"
            v-model:filter-drop="statusFilter"
            filter-drop-label="Status"
            :filter-drop-options="['cancelled','pending','completed']" :is-date="true" 
            placeholder="Search Appointments..."
            class3=" d-flex  gap ms-5" class1=" ps-2" class4="ms-5 w-100"/>

            <Btn  label="Clear" class="btn-primary btn-sm position-absolute right-7 top-4
            mt-2 me-6 "   @click="searchQuery = ''; statusFilter = '' ; dateFilter = '' ; "/>

            <Btn  :label="adminStore.exportAppointmentsLoading? 'Exporting...' : 'Export csv'" :loader="adminStore.exportAppointmentsLoading" @click="exportAppointments" class="btn-outline-secondary btn-sm position-absolute right-6 top-4 mt-2"/>

        </template>
        <template #head>
            <BaseTableHead :t-head="tHead"/>
        </template>
        <template #body>
            <LoadingState :loading="adminStore.loading" class="position-absolute start-50 ms-5 top-1 " >
                <h4  v-if="filteredData.length == 0" class="text-muted text-center mt-10 position-absolute start-50 top-1">No Appointment History</h4>
                <AdminAppointmentsTableRow v-else v-for="(app,index) in filteredData" :key="app.id"
                :appointment="app" :index="index" @view="emit('view',app)"
                />
            </LoadingState>
        </template>
    </BaseTable>
</template>