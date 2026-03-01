<script setup>
    import { ref,onMounted } from 'vue';
    import { useRouter } from 'vue-router';
    import AdminDepartmentTable from '@/components/admin/AdminDepartmentTable.vue';
    import Btn from '@/components/common/Btn.vue';
    import AdminDepartmentDetailsOffCanvas from '@/components/admin/AdminDepartmentDetailsOffCanvas.vue';
    import LoadingState from '@/components/common/LoadingState.vue';
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
    <div class="bg-info">
        <div class="">
            <Btn label="Add Department" class="btn-warning" @click="openAddDepartment"/>
        </div>
    </div>
    <LoadingState :loading="departmentStore.loading">
        <h2 class="text-muted text-center mt-10" v-if="departmentStore.departmentList.length == 0">No Registered Department Found</h2>
        <div class="container-fluid" v-else>
            <AdminDepartmentTable @view="openDepartmentDetails"/>
            <AdminDepartmentDetailsOffCanvas :show="showDetails" :department="selectedDepartmentDetails" @close="showDetails=false"/>
        </div>
    </LoadingState>
        
</template>