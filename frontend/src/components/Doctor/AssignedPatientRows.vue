<script setup>
    import Btn from '../common/Btn.vue';
    const props=defineProps({
        patient:Object,
        index:Number
    })
</script>
<template>
    <tr>
        <th scope="row">{{ index+1 }}</th>
        <td>{{ patient.name }}</td>
        <td>{{ patient.age }}</td>
        <td>{{ patient.gender }}</td>
        <td>{{ patient.last_visit }}</td>
        <td>{{ patient.visits }}</td>
        <td>
            <Btn label="View" class="btn-outline-tertiary btn-sm"/>
        </td>
    </tr>
</template>