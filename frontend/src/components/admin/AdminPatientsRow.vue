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
    <tr>
        <th scope="row">{{ index+1 }}</th>
        <td>
            img
        </td>
        <td>{{ patient?.email }}</td>
        <td>{{ patient?.name }}</td>
        <td>{{ patient?.age }}</td>
        <td>{{ patient?.gender }}</td>
        <td>{{ patient?.contact }}</td>
        <td>
            <Badge label="Verified" v-if="patient?.profile_completed" class="text-bg-success"/>
            <Badge label="Not Verified" v-else class="text-bg-danger"/>
        </td>
        <td>null</td>
        <td>
            <Btn label="View" class="btn-outline-primary btn-sm" @click="emit('view')" />
        </td>
        
    </tr>
</template>