<script setup>
    import Badge from '../common/Badge.vue';
    import Btn from '../common/Btn.vue';
    defineProps({
        doctor:Object,
        index:Number
    })
    const emit=defineEmits(['view','block','unblock'])
</script>
<template>
    <tr class="small">
        <th scope="row">{{ index+1 }}</th>
        <td>{{ doctor?.registration_number || 'SJVC45'+index*2+'87'+ index}}</td>
        <td>Dr. {{ doctor.name }}</td>
        <td>{{ doctor.department}}</td>
        <td>{{ doctor.email}}</td>
        <td>{{ doctor.specialization}}</td>
        <td>
            <Badge label="open" v-if="!doctor?.can_block" color="success" class="me-2"/>
            <Badge label="close" v-else color="danger" class="me-2"/>
            <Badge label="Blocked" v-if="doctor.is_blocked" color="danger"/>
            
        </td>
        <td>
            <Btn label="View" class="btn-outline-secondary btn-sm me-2" @click="emit('view')" />
            <Btn v-if="doctor?.is_blocked"  label="Unblock" class="btn-outline-danger btn-sm " @click="emit('block')" />
            <Btn v-else label="Block" class="btn-outline-danger btn-sm " :disabled="!doctor?.can_block" @click="emit('unblock')"  />
            
        </td>
        
    </tr>
</template>