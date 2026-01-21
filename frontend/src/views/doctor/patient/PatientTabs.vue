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
  <ul class="nav nav-tabs mb-3">
    <li class="nav-item">
      <button class="nav-link" :class="{active: activeTab==='current'}" @click="activeTab='current'">
        Current
      </button>
    </li>
    <li class="nav-item">
      <button class="nav-link" :class="{active: activeTab==='appointments'}" @click="activeTab='appointments'">
        Appointments
      </button>
    </li>
    
  </ul>

  <div v-if="activeTab==='current'">
    <CurrentAppointmentCard :appointment="currentAppointment" />
  </div>

  <div v-if="activeTab==='appointments'">
    <AppointmentHistoryTable :appointments="appointments" />
  </div>



</template>
