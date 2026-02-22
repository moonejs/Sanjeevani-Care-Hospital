<script setup>
    import AdminPatientsTable from '@/components/admin/AdminPatientsTable.vue';
    import AdminPatientModel from '@/components/admin/AdminPatientModel.vue';
    import { ref } from 'vue';

    const showModel=ref(false)
    const selectedPatientDetails=ref(null)
    

    function openPatientDetails(patient){
        selectedPatientDetails.value=patient
        showDetails.value=true
        console.log(patient);
        
    }

</script>
<template>
    <div class="bg-info">
        <div class="">
            <h2>Search</h2>
        </div>
    </div>
    <div class="container-fluid">
        <AdminPatientsTable @view="openPatientDetails"/>
        
    </div>
    <AdminPatientModel :show-model="showModel" :patient="selectedPatientDetails" @close="showModel=false"/>
</template>