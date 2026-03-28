<script setup>
    import Badge from '../common/Badge.vue';
    import Btn from '../common/Btn.vue';
    defineProps({
        patient:Object,
        index:Number
    })
    const emit=defineEmits(['view'])
</script>
<template>
    <tr class="small">
        <th scope="row">{{ index+1 }}</th>
        <td>{{ patient?.email }}</td>
        <td>{{ patient?.name }}</td>
        <td>{{ patient?.age }}</td>
        <td>{{ patient?.gender }}</td>
        <td>{{ patient?.contact }}</td>
        <td>
            <Badge :label="patient.profile_completed ? 'Verified' : 'Not Verified'" :color="patient.profile_completed ? 'success' : 'danger'"/>
            
        </td>
        <td>{{patient.blood_group}}</td>
        <td>
            <Btn label="View" class="btn-outline-secondary btn-sm" @click="emit('view')" />
        </td>
        
    </tr>
</template>