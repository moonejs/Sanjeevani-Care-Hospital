<script setup>
    import { ref } from 'vue';
    import { useRouter } from 'vue-router';
    import AdminDepartmentTable from '@/components/admin/AdminDepartmentTable.vue';
    import Btn from '@/components/common/Btn.vue';
    import AdminDepartmentDetailsOffCanvas from '@/components/admin/AdminDepartmentDetailsOffCanvas.vue';
    
    const showDetails=ref(false)
    const selectedDepartmentDetails=ref(null)
    const router=useRouter()

    function openDepartmentDetails(dept){
        selectedDepartmentDetails.value=dept
        showDetails.value=true
        console.log(dept);
        
    }

    function openAddDepartment(){
        router.push('departments/create')
    }


</script>
<template>
    <div class="bg-info">
        <div class="">
            <Btn label="Add Department" class="btn-warning" @click="openAddDepartment"/>
        </div>
    </div>
    <div class="container-fluid">
        <AdminDepartmentTable @view="openDepartmentDetails"/>
        <AdminDepartmentDetailsOffCanvas :show="showDetails" :department="selectedDepartmentDetails" @close="showDetails=false"/>
    </div>

</template>