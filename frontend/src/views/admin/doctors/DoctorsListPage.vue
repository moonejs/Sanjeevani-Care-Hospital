<script setup>
    import AdminDoctorsTable from '@/components/admin/AdminDoctorsTable.vue';
    import { ref } from 'vue';
    import { useRouter } from 'vue-router';
    import { useDoctorStore } from '@/stores/doctor.store';
    import AdminDoctorDetailsOffCanvas from '@/components/admin/AdminDoctorDetailsOffCanvas.vue';
    import Btn from '@/components/common/Btn.vue';
    import LoadingState from '@/components/common/LoadingState.vue';
    import BlockModal from '@/components/admin/BlockModal.vue';
    import { onMounted } from 'vue';
    import { useAdminStore } from '@/stores/admin.store';
    import { useSearchFilter } from '@/utils/useSearchFilter';
    import { storeToRefs } from 'pinia';
    import SearchInput from '@/components/common/SearchInput.vue';
    import FilterDropdown from '@/components/common/FilterDropdown.vue';
    

    const showDetails=ref(false)
    const selectedDoctorDetails=ref(null)
    const router=useRouter()
    const doctorStore=useDoctorStore()
    const adminStore=useAdminStore()
    const showModal = ref(false)
    const selectedDoctor=ref(null)
    
    const departmentFilter = ref('')
    const { doctorsList } = storeToRefs(doctorStore)
    const { searchQuery, filteredData } = useSearchFilter(
        doctorsList,
        ['name', 'email', 'department','registration_number'],
        {
            department: departmentFilter
        }
    )

    

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

    function openBlockDoctorModal(doctor){
        selectedDoctor.value=doctor
        showModal.value=true
    }
    async function blockDoctor(){
        await adminStore.blockDoctor(selectedDoctor.value.id)
        showModal.value=false
        await doctorStore.fetchDoctors()

    }

    async function unblockDoctor(){
        console.log("hwl");
        await adminStore.unblockDoctor(selectedDoctor.value.id)
        showModal.value=false
        await doctorStore.fetchDoctors()
        
    }


</script>
<template>
    <div class="bg-info">
        
        <div class="">
            <Btn label="Add Doctor" class="btn-warning" @click="openAddDoctor"/>
        </div>
        <SearchInput  v-model="searchQuery" placeholder="Search doctors..."/>

        <FilterDropdown  v-model="departmentFilter" :options="['Cardiology', 'Ent', 'Orthopedic']" label="Departments"/>
        <Btn  label="Clear" class="btn-primary "  @click="searchQuery = ''; departmentFilter = ''"/>

    </div>
    <LoadingState :loading="doctorStore.loading">
        <h2 v-if="doctorStore.doctorsList.length == 0" class="text-muted d-flex justify-content-center mt-10">No Registered Doctors Found</h2>

        <div v-else class="container-fluid">
            <AdminDoctorsTable @view="openDoctorDetails" @block="openBlockDoctorModal" @unblock="openBlockDoctorModal" :doctors="filteredData"/>
            <AdminDoctorDetailsOffCanvas :show="showDetails" :doctor="selectedDoctorDetails" @close="showDetails=false"/>
        </div>
    </LoadingState>
    <BlockModal @close="showModal = false" :show-modal="showModal" @block="blockDoctor" @unblock="unblockDoctor" :doctor="selectedDoctor"/>

</template>