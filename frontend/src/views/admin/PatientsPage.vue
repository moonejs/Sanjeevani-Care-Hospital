<script setup>
    import AdminPatientsTable from '@/components/admin/AdminPatientsTable.vue';
    import AdminPatientModel from '@/components/admin/AdminPatientModel.vue';
    import { ref } from 'vue';
    import { useSearchFilter } from '@/utils/useSearchFilter';
    import { storeToRefs } from 'pinia';
    import { useAdminStore } from '@/stores/admin.store';
    import SearchInput from '@/components/common/SearchInput.vue';
    import FilterDropdown from '@/components/common/FilterDropdown.vue';
    import Btn from '@/components/common/Btn.vue';

    const showModel=ref(false)
    const selectedPatientDetails=ref(null)
    
    const adminStore=useAdminStore()

    const { patientList } = storeToRefs(adminStore)
    const { searchQuery, filteredData } = useSearchFilter(
        patientList,
        ['name', 'email',],
    )


    function openPatientDetails(patient){
        selectedPatientDetails.value=patient
        showDetails.value=true
        console.log(patient);
        
    }

</script>
<template>
    <div class="bg-info">
        <div class="">
            <SearchInput  v-model="searchQuery" placeholder="Search Patients..."/>
            <Btn  label="Clear" class="btn-primary "  @click="searchQuery = ''"/>
        </div>
    </div>
    <div class="container-fluid">
        <AdminPatientsTable @view="openPatientDetails" :patients="filteredData"/>
        
    </div>
    <AdminPatientModel :show-model="showModel" :patient="selectedPatientDetails" @close="showModel=false"/>
</template>