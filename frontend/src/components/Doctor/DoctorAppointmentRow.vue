<script setup>
  import Btn from '../common/Btn.vue';
  import Badge from '../common/Badge.vue';
  import { useAppointmentStore } from '@/stores/appointment.store';

  const aptStore=useAppointmentStore()
    const props=defineProps({
      appointment: Object,
      index:Number
    })
    const emit=defineEmits(['confirm','cancel','complete'])

    function confirm(){
      emit('confirm',props.appointment)
    }
    function cancel(){
      emit('cancel',props.appointment)
    }
    function complete(){
      emit('complete',props.appointment)
    }
    
</script>

<template>
  <tr class="small">
    <th scope="row">{{ index+1 }}</th>
    <td> <mark>{{ appointment.time }}</mark></td>
    <td v-if="aptStore.selectedRange==='week'" class="fw-bold"> {{ appointment.date }}</td>
    <td class="text-uppercase text-muted">{{ appointment.session }}</td>
    <td>{{ appointment.patient.name }}</td>
    <td class="text-muted small text-uppercase" :class="appointment.type === 'emergency' ? 'text-danger' : ''">{{ appointment.type }}</td>
    <td>
      <Badge :label="appointment.status" 
        :color="
          appointment.status === 'confirmed' ? 'success' :
          appointment.status === 'pending' ? 'warning' :
          appointment.status === 'cancelled' ? 'danger' :
          appointment.status === 'completed' ? 'primary' : 'secondary'
        "
      />
      
    </td>
    <td>
      <Btn v-if="appointment.status=='pending'" class="btn-outline-success btn-sm me-2" label="Confirm" @click="confirm"/>
      <Btn v-if="appointment.status=='confirmed' && aptStore.selectedRange==='today'" class="btn-outline-secondary btn-sm me-2" label="Complete" @click="complete"/>
      <Btn v-if="appointment.status=='pending'" class="btn-outline-danger btn-sm " label="Cancel" @click="cancel"/>
    </td>
  </tr>
</template>