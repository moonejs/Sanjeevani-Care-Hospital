<script setup>
    import Btn from '@/components/common/Btn.vue';
    const props=defineProps({
        appointment:Object,
        index:Number
    })
    const emit=defineEmits(['view'])
</script>
<template>
    <tr>
        <th scope="row">
            {{ index+1 }}
        </th>
        <td>{{ appointment.date }}</td>
        <td>{{ appointment.start_time }}</td>
        <td>{{ appointment.status }}</td>
        <td>{{ appointment.type }}</td>
        <td>{{ appointment.patient.name }}</td>
        <td>{{ appointment.treatment?.diagnosis || 'No Diagnosis'}}</td>
        
        <td>{{ appointment.treatment?.follow_up_date || 'No Follow up Date'}}</td>
        <td>
            <Btn label="View" class="btn-sm btn-primary" @click="emit('view')"/>
        </td>
    </tr>
</template>