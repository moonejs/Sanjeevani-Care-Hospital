<script setup>
    import AdminDoctorsTable from '@/components/admin/AdminDoctorsTable.vue';
    import { ref } from 'vue';
    import AdminDoctorDetailsOffCanvas from '@/components/admin/AdminDoctorDetailsOffCanvas.vue';

    const showDetails=ref(false)
    const selectedDoctorDetails=ref(null)

    function openDoctorDetails(doctor){
        selectedDoctorDetails.value=doctor
        showDetails.value=true
        console.log(doctor);
        
    }
</script>
<template>
    <div class="">
        <div class="col">
            Add Doctor
        </div>
    </div>
    <div class="container-fluid">
        <AdminDoctorsTable @view="openDoctorDetails"/>
        <AdminDoctorDetailsOffCanvas :show="showDetails" :doctor="selectedDoctorDetails" @close="showDetails=false"/>
    </div>

</template>