<script setup>
    import BaseTable from '../layout/BaseTable.vue';
    import BaseTableHead from '../layout/BaseTableHead.vue';
    import DoctorDashTableCaption from '../Doctor/DoctorDashTableCaption.vue';
    import AdminDepartmentRow from './AdminDepartmentRow.vue';
    import { useDepartmentStore } from '@/stores/department.store';
    
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

    const emit = defineEmits(['view'])
</script>

<template>
    <BaseTable>
        <template #caption>
            <DoctorDashTableCaption title="Registered Departments"/>
        </template>
        <template #head>
            <BaseTableHead :t-head="tHead"/>
        </template>
        <template #body>
            <AdminDepartmentRow v-for="(dep,index) in departments" :key="index" :index="
            index" :department="dep" @view="emit('view',dep)"/>
        </template>
    
    </BaseTable>
</template>