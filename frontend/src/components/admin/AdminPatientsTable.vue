<script setup>
    import BaseTable from '../layout/BaseTable.vue';
    import BaseTableHead from '../layout/BaseTableHead.vue';
    import DoctorDashTableCaption from '../Doctor/DoctorDashTableCaption.vue';
    import { useAdminStore } from '@/stores/admin.store';
    import AdminPatientsRow from './AdminPatientsRow.vue';
    import { onMounted } from 'vue';
    
    const tHead=["Photo","Email","Name","Age","Gender","Contact","Verified","Appointment Status","Actions"]
    
    const adminStore=useAdminStore()

    onMounted(async()=>{
        await adminStore.fetchPatients()
    })

    const emit = defineEmits(['view'])
</script>

<template>
    <BaseTable>
        <template #caption>
            <DoctorDashTableCaption title="Registered Patients"/>
        </template>
        <template #head>
            <BaseTableHead :t-head="tHead"/>
        </template>
        <template #body>
            <AdminPatientsRow v-for="(patient,index) in adminStore.patientList" :key="index" :index="
            index" :patient="patient" @view="emit('view',patient)"/>
        </template>
    
    </BaseTable>
</template>