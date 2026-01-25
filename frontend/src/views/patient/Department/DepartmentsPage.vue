<script setup>
    import Header from '@/components/layout/Header.vue';
    import ProfileCard from '@/components/layout/ProfileCard.vue';
    import { useDepartmentStore } from '@/stores/department.store';
    import Loading from '@/components/common/Loading.vue';
    import { onMounted } from 'vue';
    import { useRouter } from 'vue-router';


    const department=useDepartmentStore()
    const route=useRouter()

    onMounted(()=>{
        department.fetchDepartments()
    })

    function openDepartmentPage(id){
        console.log(id);
        route.push({
            name:'departmentDetail-patient',
            params:{
                id:id
            }
        })
        
    }

</script>

<template>
    <div>
        <Header label="Departments"/>
            <div v-if="department.loading" class="empty-state">
                <Loading :loading="true" />
            </div>
            <div
                v-else-if="!department.departmentList.length"
                class="empty-state">
                <h2>No departments yet</h2>
            </div>
            <div v-else class="main bg-danger-subtle container-fluid mt-3 ">
                <div  class="row mb-3">
                    <div class="col-2" v-for="dept in department.departmentList" :key="dept.id">
                        <ProfileCard type="department" :profile="dept" @select="openDepartmentPage(dept.id)" />
                    </div>
                </div>
                
            </div>
    </div>
    
</template>