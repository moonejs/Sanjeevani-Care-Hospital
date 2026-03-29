<script setup>
    import AdminPatientDetailsOffCanvas from '@/components/admin/AdminPatientDetailsOffCanvas.vue';
    import AdminPatientsTable from '@/components/admin/AdminPatientsTable.vue';
    import { ref } from 'vue';
    const showModel=ref(false)
    const selectedPatientDetails=ref(null)
    
    
    function openPatientDetails(patient){
        selectedPatientDetails.value=patient
        showModel.value=true
        console.log(patient);
        
    }

</script>
<template>
    <div class="container-fluid mt-2">
        <AdminPatientsTable @view="openPatientDetails" />
        
    </div>
    <AdminPatientDetailsOffCanvas :show-model="showModel" :patient="selectedPatientDetails" @close="showModel=false"/>
</template>