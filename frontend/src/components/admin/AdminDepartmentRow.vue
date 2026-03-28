<script setup>
    import Badge from '../common/Badge.vue';
    import Btn from '../common/Btn.vue';
    import { computed } from 'vue';
    import { departmentIcons } from "@/utils/departmentIcons"
    const props=defineProps({
        department:Object,
        index:Number
    })
    const emit=defineEmits(['view'])
    const iconComponent = computed(() => {
        const icon = departmentIcons.find(i => i.key === props.department?.icon)
        return icon ? icon.component : null
    })
    
</script>
<template>
    <tr class="small">
        <th scope="row">{{ index+1 }}</th>
        <td>
            <component :is="iconComponent" class="text-primary " style="width:32px;height:32px"/>
            </td>
        <td>{{ department?.name }}</td>
        <td>{{ department?.email }}</td>
        <td class="small">{{ department?.phone }}</td>
        <td>
            <Badge :label="department.emergency_available ? 'Available' : 'Unavailable'"  :color="department.emergency_available ? 'success' : 'danger'"/>
        </td>
        <td>
            <Badge :label="department.is_active ? 'Available' : 'Unavailable'"  :color="department.is_active ? 'success' : 'danger'"/>
        </td>
        <td>
            <Btn label="View" class="btn-outline-secondary btn-sm" @click="emit('view')" />
        </td>
        
    </tr>
</template>