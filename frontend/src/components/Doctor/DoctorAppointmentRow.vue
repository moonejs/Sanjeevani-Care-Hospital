<script setup>
  import Btn from '../common/Btn.vue';
    defineProps({
      appointment: Object,
      index:Number
    })
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
      <Btn class="btn-outline-success btn-sm" label="Confirm"/>
    </td>
  </tr>
</template>