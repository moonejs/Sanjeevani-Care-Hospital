<script setup>
    import Btn from '@/components/common/Btn.vue'
    import Badge from '../common/Badge.vue';

    defineProps({
        appointment: Object,
        index: Number
    })

    const emit = defineEmits(['view'])
</script>

<template>
  <tr class="small">
    <th scope="row">{{ index+1 }}</th>
    <td>{{ appointment.date }}</td>
    <td>{{ appointment.time }}</td>
    <td>{{ appointment.doctor.name }}</td>
    <td>{{ appointment.department.name }}</td>
    <td class="text-uppercase">{{ appointment.type }}</td>
    <td>
      <Badge :label="appointment.status" :color="
        appointment.status === 'pending' ? 'warning' :
        appointment.status === 'confirmed' ? 'primary' :
        appointment.status === 'completed' ? 'success' :
        appointment.status === 'cancelled' ? 'danger' : 'secondary'
      "/>
    </td>
    <td>
      <Btn label="View" class="btn-outline-primary btn-sm" @click="emit('view')" />
    </td>
  </tr>
</template>
