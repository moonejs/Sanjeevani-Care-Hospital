<script setup>
    import AdminDoctorsTable from '@/components/admin/AdminDoctorsTable.vue';
    import { ref } from 'vue';
    import { useRouter } from 'vue-router';
    import { useDoctorStore } from '@/stores/doctor.store';
    import AdminDoctorDetailsOffCanvas from '@/components/admin/AdminDoctorDetailsOffCanvas.vue';
    import Btn from '@/components/common/Btn.vue';
    import LoadingState from '@/components/common/LoadingState.vue';
    import { onMounted } from 'vue';

    const showDetails=ref(false)
    const selectedDoctorDetails=ref(null)
    const router=useRouter()
    const doctorStore=useDoctorStore()

    onMounted(()=>{
        doctorStore.fetchDoctors()
    })  


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
    <LoadingState :loading="doctorStore.loading">
        <h2 v-if="doctorStore.doctorsList.length == 0" class="text-muted d-flex justify-content-center mt-10">No Registered Doctors Found</h2>

        <div v-else class="container-fluid">
            <AdminDoctorsTable @view="openDoctorDetails"/>
            <AdminDoctorDetailsOffCanvas :show="showDetails" :doctor="selectedDoctorDetails" @close="showDetails=false"/>
        </div>
    </LoadingState>

</template>