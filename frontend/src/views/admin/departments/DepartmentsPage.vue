<script setup>
    import { ref,onMounted } from 'vue';
    import { useRouter } from 'vue-router';
    import AdminDepartmentTable from '@/components/admin/AdminDepartmentTable.vue';
    import Btn from '@/components/common/Btn.vue';
    import AdminDepartmentDetailsOffCanvas from '@/components/admin/AdminDepartmentDetailsOffCanvas.vue';
    
    import { useDepartmentStore } from '@/stores/department.store';

    



    const showDetails=ref(false)
    const selectedDepartmentDetails=ref(null)
    const router=useRouter()
    const departmentStore=useDepartmentStore()


    


    onMounted(async()=>{
        await departmentStore.fetchDepartments()
    })


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
    <div class="ms-4 mt-2">
        <div class="">
            <Btn label="Add Department" class="btn-outline-secondary" @click="openAddDepartment"/>
        </div>
    </div>
    
        
        <div class="container-fluid" >
            <AdminDepartmentTable @view="openDepartmentDetails" />
            <AdminDepartmentDetailsOffCanvas :show="showDetails" :department="selectedDepartmentDetails" @close="showDetails=false"/>
        </div>
    
        
</template>