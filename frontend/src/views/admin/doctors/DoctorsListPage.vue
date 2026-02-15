<script setup>
    import AdminDoctorsTable from '@/components/admin/AdminDoctorsTable.vue';
    import { ref } from 'vue';
    import { useRouter } from 'vue-router';
    import AdminDoctorDetailsOffCanvas from '@/components/admin/AdminDoctorDetailsOffCanvas.vue';
    import Btn from '@/components/common/Btn.vue';

    const showDetails=ref(false)
    const selectedDoctorDetails=ref(null)
    const router=useRouter()

    function openDoctorDetails(doctor){
        selectedDoctorDetails.value=doctor
        showDetails.value=true
        console.log(doctor);
        
    }

    function openAddDoctor(){
        router.push('doctors/create')
    }

</script>
<template>
    <div class="bg-info">
        <div class="">
            <Btn label="Add Doctor" class="btn-warning" @click="openAddDoctor"/>
        </div>
    </div>
    <div class="container-fluid">
        <AdminDoctorsTable @view="openDoctorDetails"/>
        <AdminDoctorDetailsOffCanvas :show="showDetails" :doctor="selectedDoctorDetails" @close="showDetails=false"/>
    </div>

</template>