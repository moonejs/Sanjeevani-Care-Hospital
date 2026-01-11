<script setup>
    import { useRoute } from 'vue-router';
    import { onMounted,computed } from 'vue';
    import { useDoctorStore } from '@/stores/doctor.store';


    const doctor=useDoctorStore()
    const route=useRoute()
    const doctor_id=route.params.id
    onMounted(()=>{
        doctor.fetchDoctorById(doctor_id)
    })

    const currentDoctor=computed(()=>{
        return doctor.selectedDoctor
    })
</script>

<template>
    <div class="d-flex">
        <div class="doctorDetail-page-left bg-success">

        </div>
        <div class="doctorDetail-page-right bg-danger" v-if="currentDoctor">
            <h1>
                {{ currentDoctor.name}}
            </h1>
        </div>
    </div>
</template>