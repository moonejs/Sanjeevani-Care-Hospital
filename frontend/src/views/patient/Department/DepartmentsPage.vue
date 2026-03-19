<script setup>
    import Header from '@/components/layout/Header.vue';
    import ProfileCard from '@/components/layout/ProfileCard.vue';
    import { useDepartmentStore } from '@/stores/department.store';
    import Loading from '@/components/common/Loading.vue';
    import LoadingState from '@/components/common/LoadingState.vue';
    import { onMounted } from 'vue';
    import { useRouter } from 'vue-router';
    import SearchInput from '@/components/common/SearchInput.vue';
    import { useSearchFilter } from '@/utils/useSearchFilter';
    import { storeToRefs } from 'pinia';


    const department=useDepartmentStore()
    const route=useRouter()

    const {departmentList}=storeToRefs(department)
    const { searchQuery, filteredData } = useSearchFilter(
        departmentList,
        ['name'],
        
    )


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
        <div class="container ms-12 ps-10">
            <SearchInput class="w-25"  v-model="searchQuery" placeholder="Search Departments..."/>
        </div>
            <LoadingState :loading="department.loading">
            <div v-if="department.departmentList.length == 0" class="empty-state">
                <h2>No departments Found</h2>
            </div>
            <div v-else class="main bg-danger-subtle container-fluid mt-3 ">
                <div  class="row mb-3">
                    <div class="col-2" v-for="dept in filteredData" :key="dept.id">
                        <ProfileCard type="department" :profile="dept" @select="openDepartmentPage(dept.id)" />
                    </div>
                </div>
            </div>
            </LoadingState>
            
    </div>
    
</template>