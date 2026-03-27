<script setup>
    import AdminDoctorsTable from '@/components/admin/AdminDoctorsTable.vue';
    import { ref } from 'vue';
    import { useRouter } from 'vue-router';
    import { useDoctorStore } from '@/stores/doctor.store';
    import AdminDoctorDetailsOffCanvas from '@/components/admin/AdminDoctorDetailsOffCanvas.vue';
    import Btn from '@/components/common/Btn.vue';

    import BlockModal from '@/components/admin/BlockModal.vue';
    import { onMounted } from 'vue';
    import { useAdminStore } from '@/stores/admin.store';
    import { useToastStore } from '@/stores/toast.store';

    const showDetails=ref(false)
    const selectedDoctorDetails=ref(null)
    const router=useRouter()
    const doctorStore=useDoctorStore()
    const adminStore=useAdminStore()
    const showModal = ref(false)
    const selectedDoctor=ref(null)
    const toast = useToastStore()
    

    

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
        try {
            const res = await adminStore.blockDoctor(selectedDoctor.value.id)
            showModal.value=false
            
            await doctorStore.fetchDoctors()

            toast.addToast({
                message: res.message,
                type: 'success'
            })
        } catch (error) {
            
        }

    }

    async function unblockDoctor(){
        console.log("hwl");
        try {
            const res = await adminStore.unblockDoctor(selectedDoctor.value.id)
            showModal.value=false
            await doctorStore.fetchDoctors()

            toast.addToast({
                message: res.message,
                type: 'success'
            })
        } catch (error) {
            toast.addToast({
                message: 'Some Error Occured',
                type: 'error'
            })
        }
        
    }


</script>
<template>
    <div class="">
        
        <div class="position-absolute  ms-4 mt-1 top-1">
            <Btn label="Add Doctor" class="btn-outline-secondary" @click="openAddDoctor"/>
        </div>
        

    </div>
        <div  class="container-fluid mt-5 v">
            <AdminDoctorsTable @view="openDoctorDetails" @block="openBlockDoctorModal" @unblock="openBlockDoctorModal"/>
            <AdminDoctorDetailsOffCanvas :show="showDetails" :doctor="selectedDoctorDetails" @close="showDetails=false"/>
        </div>
    <BlockModal @close="showModal = false" :show-modal="showModal" @block="blockDoctor" @unblock="unblockDoctor" :doctor="selectedDoctor"/>

</template>

<style scoped>
.v{
    height: 41rem;
    overflow-x: hidden;
    /* background-color: cadetblue; */
}
</style>

