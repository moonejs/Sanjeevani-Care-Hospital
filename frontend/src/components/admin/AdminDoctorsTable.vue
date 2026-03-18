<script setup>
    import BaseTable from '../layout/BaseTable.vue';
    import BaseTableHead from '../layout/BaseTableHead.vue';
    import DoctorDashTableCaption from '../Doctor/DoctorDashTableCaption.vue';
    import AdminDoctorsRow from './AdminDoctorsRow.vue';

    const props = defineProps({
        doctors: {
            type: Array,
            default: () => []
        }
    })
    
    const tHead=["Photo","Registration No.","Name","Department","Email","Specialization","Appointment Status","Actions"]
    


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
            <AdminDoctorsRow v-for="(doctor,index) in doctors" :key="index" :index="
            index" :doctor="doctor" @view="emit('view',doctor)" @block="emit('block',doctor)" @unblock="emit('unblock',doctor)"/>
        </template>
    
    </BaseTable>
</template>