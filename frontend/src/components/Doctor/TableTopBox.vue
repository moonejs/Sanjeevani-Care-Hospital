<script setup>
    import { ref } from 'vue';

    import DateBox from '../common/DateBox.vue';
    
    import { useAppointmentStore } from '@/stores/appointment.store';
    const appointment=useAppointmentStore()

    defineProps({
        label:String
    })
    const emit=defineEmits(['selectedDate'])

    function selectToday() {
        emit('selectedDate', appointment.formatDate(appointment.today))
    }

    function selectDate(value){
        emit('selectedDate',value.fullDate)
    }
</script>

<template>
    <div class="d-flex align-items-end gap-6" >
        <div  class="table-top-box bg-info d-flex justify-content-center align-items-center" @click="selectToday">
            <h2>Today</h2>
            
        </div>
        <div class="d-flex gap-4">
            <DateBox  v-for="value in appointment.days" :day="value.day" @select="selectDate"  :date="value.date" :fullDate="value.fullDate"/>
        </div>
    </div>

</template>