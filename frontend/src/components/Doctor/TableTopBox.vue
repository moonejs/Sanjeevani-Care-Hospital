<script setup>
    import { ref } from 'vue';
    import Btn from '../common/Btn.vue';
    import DateBox from '../common/DateBox.vue';
    
    import { useAppointmentStore } from '@/stores/appointment.store';
    const appointment=useAppointmentStore()

    defineProps({
        label:String
    })
    const emit=defineEmits(['selectedDate'])

    function selectToday() {
    const today = appointment.formatDate(appointment.today)
      appointment.selectedDate = today
      emit('selectedDate', today)
    }

    function selectDate(value){
      appointment.selectedDate = value.fullDate
      emit('selectedDate', value.fullDate)
    } 
</script>

<template>
  <div class="">
    <div class="sidebar-header">
      <Btn @click="selectToday" label="Jump to Today" class="btn-outline-primary  w-100 fw-semibold"/>
      <div class="sidebar-label">
        Select Date
      </div>

    </div>

    <div class="py-2 pb-3 date " >
       <div
    v-for="value in appointment.days" :key="value.fullDate" :class="{ active: appointment.selectedDate === value.fullDate }">

    <DateBox :day="value.day" :date="value.date" :fullDate="value.fullDate" @select="selectDate"/>

  </div>

    </div>

  </div>
</template>

<style scoped>


.sidebar-header{
  padding:16px;
  border-bottom:1px solid #e6e6e6;
}

.sidebar-label{
  font-size:10px;
  font-weight:600;
  letter-spacing:.8px;
  color:#5f6368;
  margin-top:12px;
  text-transform:uppercase;
}

.date :hover{
  background-color: #f1f3f5;
}
.active{
  background-color: #f1f3f5;
  border-left: 3px solid #242E4C;
}
</style>