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
<!-- <template>
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

</template> -->

<template>

    <!-- TOP CONTROL BAR -->
    <div class="container-fluid px-4 py-3">

        <div class="card border-0 shadow-sm mb-3">
            <div class="card-body d-flex flex-wrap align-items-center gap-2">

                <!-- LEFT: TITLE -->
                <h5 class="mb-0 me-auto">Doctors Management</h5>

                <!-- ADD BUTTON -->
                <Btn label="Add Doctor" class="btn-primary btn-sm" @click="openAddDoctor"/>

            </div>

            <!-- FILTER ROW -->
            <div class="card-body border-top d-flex flex-wrap gap-2">

                <!-- SEARCH -->
                <div class="flex-grow-1" style="min-width: 200px;">
                    <SearchInput  
                        v-model="searchQuery" 
                        placeholder="Search doctor, email, reg no..."
                    />
                </div>

                <!-- FILTER -->
                <div style="min-width: 180px;">
                    <FilterDropdown  
                        v-model="departmentFilter" 
                        :options="['Cardiology', 'Ent', 'Orthopedic']" 
                        label="All Departments"
                    />
                </div>

                <!-- CLEAR -->
                <Btn  
                    label="Clear" 
                    class="btn-outline-secondary btn-sm"
                    @click="searchQuery = ''; departmentFilter = ''"
                />

            </div>
        </div>

        <!-- TABLE SECTION -->
        <LoadingState :loading="doctorStore.loading">

            <!-- EMPTY STATE -->
            <div v-if="doctorStore.doctorsList.length == 0" 
                 class="text-center py-5 text-muted">
                <h5 class="fw-normal">No Registered Doctors Found</h5>
                <small>Add doctors to get started</small>
            </div>

            <!-- TABLE -->
            <div v-else class="card border-0 shadow-sm">
                <div class="card-body p-0">
                    <AdminDoctorsTable 
                        @view="openDoctorDetails" 
                        @block="openBlockDoctorModal" 
                        @unblock="openBlockDoctorModal" 
                        :doctors="filteredData"
                    />
                </div>
            </div>

        </LoadingState>

    </div>

    <!-- OFFCANVAS -->
    <AdminDoctorDetailsOffCanvas 
        :show="showDetails" 
        :doctor="selectedDoctorDetails" 
        @close="showDetails=false"
    />

    <!-- MODAL -->
    <BlockModal 
        @close="showModal = false" 
        :show-modal="showModal" 
        @block="blockDoctor" 
        @unblock="unblockDoctor" 
        :doctor="selectedDoctor"
    />

</template>