<script setup>
    import Btn from '@/components/common/Btn.vue'

    defineProps({
        appointment: Object,
        index: Number
    })

    const emit = defineEmits(['view'])
</script>

<template>
  <tr>
    <th scope="row">{{ index+1 }}</th>
    <td>{{ appointment.date }}</td>
    <td>{{ appointment.time }}</td>
    <td>{{ appointment.doctor.name }}</td>
    <td>{{ appointment.department.name }}</td>
    <td>{{ appointment.type }}</td>
    <td>
      <span
        class="badge"
        :class="{
          'bg-warning': appointment.status === 'pending',
          'bg-primary': appointment.status === 'confirmed',
          'bg-success': appointment.status === 'completed',
          'bg-danger': appointment.status === 'cancelled'
        }"
      >
        {{ appointment.status }}
      </span>
    </td>
    <td>
      <Btn label="View" class="btn-outline-primary btn-sm" @click="emit('view')" />
    </td>
  </tr>
</template>
