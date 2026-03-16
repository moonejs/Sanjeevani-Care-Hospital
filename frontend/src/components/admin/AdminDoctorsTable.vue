<script setup>
    import BaseTable from '../layout/BaseTable.vue';
    import BaseTableHead from '../layout/BaseTableHead.vue';
    import DoctorDashTableCaption from '../Doctor/DoctorDashTableCaption.vue';
    import { useDoctorStore } from '@/stores/doctor.store';
    import AdminDoctorsRow from './AdminDoctorsRow.vue';

    
    const tHead=["Photo","Registration No.","Name","Department","Email","Specialization","Appointment Status","Actions"]
    
    const doctorStore=useDoctorStore()


    const emit = defineEmits(['view','block','unblock'])
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
            index" :doctor="doctor" @view="emit('view',doctor)" @block="emit('block',doctor)" @unblock="emit('unblock',doctor)"/>
        </template>
    
    </BaseTable>
</template>