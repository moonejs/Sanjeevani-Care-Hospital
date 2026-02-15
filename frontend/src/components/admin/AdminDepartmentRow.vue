<script setup>
    import Badge from '../common/Badge.vue';
    import Btn from '../common/Btn.vue';
    defineProps({
        department:Object,
        index:Number
    })
    const emit=defineEmits(['view'])
</script>
<template>
    <tr>
        <th scope="row">{{ index+1 }}</th>
        <td>{{ department?.icon }}</td>
        <td>{{ department?.name }}</td>
        <td>{{ department?.email }}</td>
        <td>{{ department?.phone }}</td>
        <td>
            <Badge label="Available" v-if="department?.emergency_available" class="text-bg-success"/>
            <Badge label="Unavailable" v-else class="text-bg-danger"/>
        </td>
        <td>
            <Badge label="Active" v-if="department?.is_active" class="text-bg-success"/>
            <Badge label="Close" v-else class="text-bg-danger"/>
        </td>
        <td>
            <Btn label="View" class="btn-outline-primary btn-sm" @click="emit('view')" />
        </td>
        
    </tr>
</template>