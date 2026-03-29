<script setup>
    import CurrentAppointmentCard from './CurrentAppointmentCard .vue';
    import AppointmentHistoryTable from './AppointmentHistoryTable.vue';

    import { ref } from 'vue'

    defineProps({
        currentAppointment: Object,
        appointments: Array,
        treatments: Array,
        
    })

    const activeTab = ref('current')
</script>

<template>
  <div class="nav nav-tabs">
    <li class="nav-item">
      <button class="nav-link rounded-top-1" :class="{active: activeTab==='current'}" @click="activeTab='current'">
        Current Appointments
      </button>
    </li>
    <li class="nav-item">
      <button class="nav-link rounded-top-1" :class="{active: activeTab==='appointments'}" @click="activeTab='appointments'">
        Appointments History
      </button>
    </li>
    
  </div>
  

  <div v-if="activeTab==='current'">
    <CurrentAppointmentCard :appointment="currentAppointment" />
  </div>

  <div v-if="activeTab==='appointments'" class="d">
    <AppointmentHistoryTable :appointments="appointments" />
  </div>

</template>

<style scoped>
.d{
  height: 36rem;
  overflow-y: auto;
}
</style>
