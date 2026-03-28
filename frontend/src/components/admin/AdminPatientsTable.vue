<script setup>
    import BaseTable from '../layout/BaseTable.vue';
    import BaseTableHead from '../layout/BaseTableHead.vue';
    import DoctorDashTableCaption from '../Doctor/DoctorDashTableCaption.vue';
    import { useAdminStore } from '@/stores/admin.store';
    import AdminPatientsRow from './AdminPatientsRow.vue';
    import { onMounted } from 'vue';
    import { storeToRefs } from 'pinia';
    import { useSearchFilter } from '@/utils/useSearchFilter';
    import LoadingState from '@/components/common/LoadingState.vue';
    import Btn from '../common/Btn.vue';
    const tHead=["Email","Name","Age","Gender","Contact","Verified","Blood Group","Actions"]
    
    const adminStore=useAdminStore()

    defineProps({
        patients:{
            type: Array,
            default: () => []

        }
    })
    onMounted(async()=>{
        await adminStore.fetchPatients()
    })

    const emit = defineEmits(['view'])
    const { patientList } = storeToRefs(adminStore)
    const { searchQuery, filteredData } = useSearchFilter(
        patientList,
        ['name', 'email',],
    )
</script>

<template>
    <BaseTable>
        <template #caption>
            <DoctorDashTableCaption title="Registered Patients" placeholder="Search Patients..." v-model:search-query="searchQuery" class3="ms-12"/>
            <Btn  label="Clear" class="btn-primary btn-sm position-absolute right-10  top-0
            mt-4 me-6 "   @click="searchQuery = ''"/>
        </template>
        <template #head>
            <BaseTableHead :t-head="tHead"/>
        </template>
        <template #body>
            <LoadingState :loading="adminStore.loading" class="position-absolute start-50 ms-5 top-0 ">
                <h4 class="text-muted text-center mt-10 position-absolute start-50 top-1" v-if="filteredData.length == 0">No Registered Patient Found</h4>
                <AdminPatientsRow v-for="(patient,index) in filteredData" :key="index" :index="
            index" :patient="patient" @view="emit('view',patient)"/>
            </LoadingState>
        </template>
    
    </BaseTable>
</template>