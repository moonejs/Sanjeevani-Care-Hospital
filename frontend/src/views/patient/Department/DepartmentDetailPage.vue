<script setup>
    import { useDepartmentStore } from '@/stores/department.store';
    import { useDoctorStore } from '@/stores/doctor.store';
    import ProfileCard from '@/components/layout/ProfileCard.vue';
    import { useRoute,useRouter } from 'vue-router';
    import { onMounted ,computed } from 'vue';

    const department=useDepartmentStore()
    const route=useRoute()
    const router=useRouter()
    const departmentId = route.params.id
    const doctor=useDoctorStore()

    onMounted(()=>{
        department.fetchDepartmentById(departmentId)
        doctor.fetchDoctorsByDepartment(departmentId)
    })

    function openDoctorPage(id){
        router.push({
            name:'doctorProfile-patient',
            params:{
                id:id
            }
        })
    }

    const doctorsList=computed(()=>{
        return doctor.doctorsByDepartment
    })

</script>

<template>
    <div class="d-flex container-fluid">

        <div class="departmentDetail-page-left container-fluid bg-success">
            <div class="upper bg-warning">
                <h1>Speciallists</h1>

                <div class="bg-primary">
                    <div class="row">
                        <div class="col-4" v-for="doctor in doctorsList" :key="doctor.id" >
                            <ProfileCard :label="doctor.name"   @select="openDoctorPage(doctor.id)" class="doctor-profile-card" />
                        </div>
                    </div>
                    
                </div>
            </div>
        </div>
        <div class="departmentDetail-page-right container-fluid bg-danger">
            ss
        </div>
    </div>
</template>