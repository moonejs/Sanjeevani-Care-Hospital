<script setup>
    import Btn from '../common/Btn.vue';
    import { useRouter } from 'vue-router';
    const props=defineProps({
        patient:Object,
        index:Number
    })
    const router=useRouter()
    function openPatientProfilePage(id){
        console.log("jjjjj"+id);
        
        router.push({
            name:'patientProfile-doctor',
            params:{
                id:id
            }
        })
    }
</script>
<template>
    <tr>
        <th scope="row">{{ index+1 }}</th>
        <td>{{ patient.name }}</td>
        <td>{{ patient.last_visit || 'Never Visited' }}</td>
        <td>{{ patient.visits }}</td>
        <td>
            <Btn label="View" class="btn-outline-tertiary btn-sm" @click="openPatientProfilePage(patient.patient_id)" />
        </td>
    </tr>
</template>