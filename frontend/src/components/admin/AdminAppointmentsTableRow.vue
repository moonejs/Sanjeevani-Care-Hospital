<script setup>
    import Btn from '@/components/common/Btn.vue';
    import Badge from '../common/Badge.vue';
    const props=defineProps({
        appointment:Object,
        index:Number
    })
    const emit=defineEmits(['view'])
</script>
<template>
    <tr class="small">
        <th scope="row">
            {{ index+1 }}
        </th>
        <td>{{ appointment.date }}</td>
        <td>{{ appointment.start_time }}</td>
        <td>
            <Badge :label="appointment.status" :color="
            appointment.status === 'cancelled' ? 'danger':
            appointment.status === 'completed' ? 'success':
            appointment.status === 'cancelled_by_admin' ? 'secondary':'primary'
            "/>
        
        </td>
        <td>{{ appointment.doctor.name }}</td>
        <td>{{ appointment.patient.name }}</td>
        <td class="text-uppercase">{{ appointment.type }}</td>
        <td>{{ appointment.doctor.department || 'No Diagnosis'}}</td>
        
        <td>{{ appointment.treatment?.follow_up_date || 'No Follow up Date'}}</td>
        <td>
            <Btn label="View" class="btn-sm btn-outline-secondary" @click="emit('view')"/>
        </td>
    </tr>
</template>