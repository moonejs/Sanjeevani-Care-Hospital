<script setup>
    import Pagination from '@/components/common/Pagination.vue';
    import AdminAppointmentsTable from '@/components/admin/AdminAppointmentsTable.vue';
    import LoadingState from '@/components/common/LoadingState.vue';
    import { useAdminStore } from '@/stores/admin.store';
    import { onMounted,ref } from 'vue';
    import AppointmentDetailsOffcanvas from '@/components/Doctor/appointment/AppointmentDetailsOffcanvas.vue';
    import { useSearchFilter } from '@/utils/useSearchFilter';
    import { storeToRefs } from 'pinia';
    import SearchInput from '@/components/common/SearchInput.vue';
    import FilterDropdown from '@/components/common/FilterDropdown.vue';
    import Btn from '@/components/common/Btn.vue';
    import DateFilter from '@/components/common/DateFilter.vue';

    const adminStore=useAdminStore()
    const selectedAppointment=ref(null)
    const showDetails=ref(false)

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

    onMounted(async ()=>{
        await adminStore.fetchAdminAppointments(1)
    })
    function changePage(page) {
        appointment.fetchDoctorAppointmentHistory(page)
    }
    function openDetails(appt) {
        selectedAppointment.value = appt
        showDetails.value = true
    }
    function closeDetails() {
        showDetails.value = false
        selectedAppointment.value = null
    }  

</script>
<template>
    <div>
        <div class="bg-info doctor-appointment-filter">
            <SearchInput  v-model="searchQuery" placeholder="Search Appointments..."/>
            <FilterDropdown  v-model="statusFilter" :options="['cancelled','pending','completed']" label="Status"/>
            <DateFilter v-model="dateFilter" label="Filter by Date" />
            <Btn  label="Clear" class="btn-primary "  @click="searchQuery = ''; statusFilter = '' ;dateFilter=''"/>
        </div>
        <LoadingState :loading="adminStore.loading">

            <div class="container-fluid" v-if="adminStore.adminAppointments.length !=0">
                <AdminAppointmentsTable :appointments="filteredData" @view="openDetails"/>
                <Pagination :pagination="adminStore.adminAppointmentsPagination" @change="changePage" />
            </div>
            <h2 v-else class="text-muted text-center mt-10">No Appointment History</h2>
            <AppointmentDetailsOffcanvas :show="showDetails" :appointment="selectedAppointment" @close="closeDetails"/>
        </LoadingState>
    </div>
</template>