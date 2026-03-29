<script setup>
    import Btn from '@/components/common/Btn.vue';
    import Badge from '@/components/common/Badge.vue';
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
        <td class="fw-bold">{{ appointment.date }}</td>
        <td ><mark>{{ appointment.time }}</mark></td>
        <td>
            <Badge :label="appointment.status" :color="appointment.status === 'cancelled' ? 'danger' : 
            appointment.status === 'confirm' ? 'success' : appointment.status === 'pending' ? 'warning' : 
            appointment.status === 'completed' ?'primary' : 'secondary'"/>
        </td>
        <td :class="appointment.type === 'emergency' ? 'text-danger' :''" class="text-uppercase">{{ appointment.type }}</td>
        <td>{{ appointment.patient.name }}</td>
        <td>{{ appointment.treatment?.diagnosis || 'No Diagnosis'}}</td>
        
        <td>{{ appointment.treatment?.follow_up_date || 'No Follow up Date'}}</td>
        <td>
            <Btn label="View" class="btn-sm btn-outline-secondary" @click="emit('view')"/>
        </td>
    </tr>
</template>