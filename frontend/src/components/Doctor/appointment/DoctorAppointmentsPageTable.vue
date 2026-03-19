<script setup>
    import BaseTable from '@/components/layout/BaseTable.vue';
    import BaseTableHead from '@/components/layout/BaseTableHead.vue';
    import DoctorAppointmentsPageRow from './DoctorAppointmentsPageRow.vue';
    import DoctorDashTableCaption from '../DoctorDashTableCaption.vue';
    import { ref } from 'vue';
    import { useAppointmentStore } from '@/stores/appointment.store'
    import { useSearchFilter } from '@/utils/useSearchFilter';
    import { storeToRefs } from 'pinia';
    import Btn from '@/components/common/Btn.vue';

    const appointmentStore=useAppointmentStore()

    const dateFilter = ref('')

    const {appointmentHistory} = storeToRefs(appointmentStore)
    const { searchQuery, filteredData } = useSearchFilter(
        appointmentHistory,
        ['patient.name'],
        {
            date:dateFilter
        }
        
    )


    
    const emit=defineEmits(['view'])
    const tHead=ref(["Date","Time","Status","Type","Patient Name","Diagnosis","Follow_up_date","Actions"])
</script>
<template>
    <BaseTable>
        <template #caption>
            <DoctorDashTableCaption title="Appointment History" v-model:searchQuery="searchQuery" class1="ms-5 ps-5" class2="gap-12" :is-date="true" v-model:date-filter="dateFilter"/>
            <Btn  label="Clear" class="btn-primary "  @click="searchQuery = ''; statusFilter = '' ;dateFilter=''"/>
        </template>
        <template #head>
            <BaseTableHead :t-head="tHead"/>
        </template>
        <template #body>
            <DoctorAppointmentsPageRow v-for="(app,index) in filteredData" :key="app.id"
            :appointment="app" :index="index" @view="emit('view',app)"
            />
        </template>
    </BaseTable>
</template>