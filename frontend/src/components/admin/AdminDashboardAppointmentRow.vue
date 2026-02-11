<script setup>
    defineProps({
        appointment:Object,
        index:Number
    })
</script>
<template>
    <tr>
        <th scope="row">{{ index+1 }}</th>
        <td>{{ appointment?.department }}</td>
        <td>{{ appointment?.doctor_name }}</td>
        <td>{{ appointment?.patient_name }}</td>
        <td>{{ appointment.time }}</td>
        <td>{{ appointment.date }}</td>
        <td>{{ appointment.type }}</td>
        <td>{{ appointment.session }}</td>
        <td><span class="badge"
        :class="{
          'text-bg-success': appointment.status === 'confirmed',
          'text-bg-warning': appointment.status === 'pending',
          'text-bg-danger': appointment.status === 'cancelled',
          'text-bg-primary': appointment.status === 'completed'
        }"
      >
        {{ appointment.status }}
      </span></td>
    </tr>
</template>