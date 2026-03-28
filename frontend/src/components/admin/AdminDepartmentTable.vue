<script setup>
    import BaseTable from '../layout/BaseTable.vue';
    import BaseTableHead from '../layout/BaseTableHead.vue';
    import DoctorDashTableCaption from '../Doctor/DoctorDashTableCaption.vue';
    import AdminDepartmentRow from './AdminDepartmentRow.vue';
    import { useDepartmentStore } from '@/stores/department.store';
    import { useSearchFilter } from '@/utils/useSearchFilter';
    import { storeToRefs } from 'pinia';
    import LoadingState from '@/components/common/LoadingState.vue';
    import Btn from '../common/Btn.vue';
    
    import { onMounted } from 'vue';

    defineProps({
        departments:{
            type: Array,
            default: () => []
        }
    })


    const tHead=["Photo","Department Name","Email","Phone","Emergency Available","Appointment Status","Actions"]
    
    const departmentStore=useDepartmentStore()

    onMounted(async()=>{
        await departmentStore.fetchDepartments()
    })

    
    const { departmentList } = storeToRefs(departmentStore)
    const { searchQuery, filteredData } = useSearchFilter(
        departmentList,
        ['name', 'email',],
    )

    const emit = defineEmits(['view'])
</script>

<template>
    <BaseTable>
        <template #caption>
            <DoctorDashTableCaption title="Registered Departments" class3="ms-12" v-model:search-query="searchQuery"
            placeholder="Search departments..."
            />
            <Btn  label="Clear" class="btn-primary btn-sm position-absolute right-8 top-5
            mt-4 me-6 "   @click="searchQuery = ''"/>
        </template>
        <template #head>
            <BaseTableHead :t-head="tHead"/>
        </template>
        <template #body>
            <LoadingState :loading="departmentStore.loading" class="position-absolute start-50 ms-5 top-1 ">
                <h4 class="text-muted text-center mt-10 position-absolute start-50 top-1" v-if="filteredData.length == 0">No Registered Department Found</h4>

                <AdminDepartmentRow v-else v-for="(dep,index) in filteredData" :key="index" :index="
            index" :department="dep" @view="emit('view',dep)"/>
        </LoadingState>
        </template>
    
    </BaseTable>
</template>