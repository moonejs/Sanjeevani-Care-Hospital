<script setup>
    import Header from '@/components/layout/Header.vue';
    import ProfileCard from '@/components/layout/ProfileCard.vue';
    import { useDoctorStore } from '@/stores/doctor.store';
    import Loading from '@/components/common/Loading.vue';
    import { onMounted } from 'vue';
    import { useRouter } from 'vue-router';

    const doctor=useDoctorStore()
    const route=useRouter()

    onMounted(()=>{
        doctor.fetchDoctors()
    })

    function openDoctorPage(id){
        console.log(id);
        route.push({
            name:'doctorProfile-patient',
            params:{
                id:id
            }
        })
        
    }

    

</script>

<template>
    <div>
        <Header label="Doctors"/>
            <div v-if="doctor.loading" class="empty-state">
                <Loading :loading="true" />
            </div>
            <div
                v-else-if="!doctor.doctorsList.length"
                class="empty-state">
                <h2>No doctors yet</h2>
            </div>
            <div v-else class="main bg-danger-subtle container-fluid mt-3 ">
                <div  class="row mb-3">
                    <div class="col-2" v-for="dept in doctor.doctorsList" :key="dept.id">
                        <ProfileCard :label="dept.name" @select="openDoctorPage(dept.id)" />
                    </div>
                </div>
                
            </div>
    </div>
    
</template>