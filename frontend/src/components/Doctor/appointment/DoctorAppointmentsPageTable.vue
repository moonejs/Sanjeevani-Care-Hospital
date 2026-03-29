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
            <DoctorDashTableCaption title="Appointment History" v-model:searchQuery="searchQuery" class1="" class2="gap-12 " :is-date="true" v-model:date-filter="dateFilter" class3="d-flex ms-11 gap-4 "/>
            <Btn  label="Clear" class="btn-secondary position-absolute top-6 right-7 me-2  mt-3 btn-sm"  @click="searchQuery = ''; statusFilter = '' ;dateFilter=''"/>
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