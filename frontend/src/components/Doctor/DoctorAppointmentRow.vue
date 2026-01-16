<script setup>
  import Btn from '../common/Btn.vue';
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
  <tr>
    <th scope="row">{{ index+1 }}</th>
    <td>{{ appointment.time }}</td>
    <td>{{ appointment.session }}</td>
    <td>{{ appointment.patient.name }}</td>
    <td>
      <span class="badge"
        :class="{
          'text-bg-success': appointment.status === 'confirmed',
          'text-bg-warning': appointment.status === 'pending',
          'text-bg-danger': appointment.status === 'cancelled'
        }"
      >
        {{ appointment.status }}
      </span>
    </td>
    <td>{{ appointment.type }}</td>
    <td>
      <Btn v-if="appointment.status=='pending'" class="btn-outline-success btn-sm me-2" label="Confirm" @click="confirm"/>
      <Btn v-if="appointment.status=='confirmed'" class="btn-outline-primary btn-sm me-2" label="Complete" @click="complete"/>
      <Btn v-if="appointment.status=='pending'" class="btn-outline-danger btn-sm " label="Cancel" @click="cancel"/>
    </td>
  </tr>
</template>