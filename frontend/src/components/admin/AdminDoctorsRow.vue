<script setup>
    import Badge from '../common/Badge.vue';
    import Btn from '../common/Btn.vue';
    defineProps({
        doctor:Object,
        index:Number
    })
    const emit=defineEmits(['view'])
</script>
<template>
    <tr>
        <th scope="row">{{ index+1 }}</th>
        <td>sss</td>
        <td>{{ doctor?.registration_number }}</td>
        <td>{{ doctor.name }}</td>
        <td>{{ doctor.department}}</td>
        <td>{{ doctor.email}}</td>
        <td>{{ doctor.specialization}}</td>
        <td>
            <Badge label="open" v-if="doctor?.is_bookable" class="text-bg-success"/>
            <Badge label="close" v-else class="text-bg-danger"/>
        </td>
        <td>
            <Btn label="View" class="btn-outline-primary btn-sm" @click="emit('view')" />
        </td>
        
    </tr>
</template>