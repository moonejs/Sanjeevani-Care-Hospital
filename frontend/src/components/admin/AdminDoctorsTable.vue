<script setup>
    import BaseTable from '../layout/BaseTable.vue';
    import BaseTableHead from '../layout/BaseTableHead.vue';
    import DoctorDashTableCaption from '../Doctor/DoctorDashTableCaption.vue';
    import { useDoctorStore } from '@/stores/doctor.store';
    import AdminDoctorsRow from './AdminDoctorsRow.vue';
    import { onMounted } from 'vue';
    const tHead=["Photo","Registration No.","Name","Department","Email","Specialization","Appointment Status","Actions"]
    
    const doctorStore=useDoctorStore()

    onMounted(async()=>{
        await doctorStore.fetchDoctors()
    })
</script>

<template>
    <BaseTable>
        <template #caption>
            <DoctorDashTableCaption title="Registered Doctors"/>
        </template>
        <template #head>
            <BaseTableHead :t-head="tHead"/>
        </template>
        <template #body>
            <AdminDoctorsRow v-for="(doctor,index) in doctorStore.doctorsList" :key="index" :index="
            index" :doctor="doctor"/>
        </template>
    
    </BaseTable>
</template>