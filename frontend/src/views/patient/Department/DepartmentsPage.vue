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
  <div class="container-fluid px-4 py-3">

    
    <div class="d-flex justify-content-between align-items-center mb-4">
      <div>
        <h4 class="fw-semibold mb-0">Departments</h4>
        <small class="text-muted">Browse hospital departments</small>
      </div>

      <SearchInput  class="w-25"  v-model="searchQuery"  placeholder="Search departments..." 
      />
    </div>

    
    <LoadingState :loading="department.loading">

      <div v-if="filteredData.length === 0" class="text-center py-5">
        <h5 class="text-muted">No departments found</h5>
      </div>

      
      <div v-else class="row g-4">
        <div class="col-xl-2 col-lg-3 col-md-4 col-sm-6"v-for="dept in filteredData" :key="dept.id">
          <ProfileCard type="department" :profile="dept" @select="openDepartmentPage(dept.id)" />
        </div>
      </div>

    </LoadingState>
  </div>
</template>