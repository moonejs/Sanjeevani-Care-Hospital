<script setup>
    import Badge from '../common/Badge.vue';
    import Btn from '../common/Btn.vue';
    defineProps({
        appointment:Object,
        index:Number
    })
    const emit=defineEmits(['cancel'])

</script>
<template>
    <tr class="small">
        <th scope="row">{{ index+1 }}</th>
        <td>{{ appointment?.department }}</td>
        <td>{{ appointment?.doctor_name }}</td>
        <td>{{ appointment?.patient_name }}</td>
        <td class="fw-bold">{{ appointment.time }}</td>
        <td>{{ appointment.date }}</td>
        <td class="text-uppercase " :class="appointment.type === 'emergency' ? 'text-danger' :'text-primary'"> {{ appointment.type }}</td>
        <td class="text-capitalize">{{ appointment.session }}</td>
        <td>
          <Badge :label="appointment.status" :color="
            appointment.status === 'confirmed' ? 'success' :
            appointment.status === 'pending' ? 'warning' :
            appointment.status === 'cancelled' ? 'danger' :
            appointment.status === 'completed' ? 'primary' :
            appointment.status === 'cancelled_by_admin' ? 'danger' : 'primary'
          " />
        </td>
        <td>
            <Btn v-if="['pending','confirmed'].includes(appointment.status)" label="Cancel" class="btn-sm btn-outline-danger " @click="emit('cancel',appointment.id)"/>
        </td>
        
    </tr>
</template>