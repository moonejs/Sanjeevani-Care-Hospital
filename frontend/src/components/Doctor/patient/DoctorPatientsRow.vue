<script setup>
    import Btn from '@/components/common/Btn.vue'
    import { useRouter } from 'vue-router'
    import Badge from '@/components/common/Badge.vue'

    defineProps({
        patient: Object,
        index: Number
    })

    const router = useRouter()

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
  <tr class="small">
    <th scope="row">
          {{ index+1 }}
    </th>
    <td>{{ patient.name }}</td>
    <td>{{ patient.age }}</td>
    <td class="text-capitalize">{{ patient.gender }}</td>
    <td>{{ patient.last_visit || '—' }}</td>
    <td>{{ patient.total_visits }}</td>
    <td>
      <Badge :label="patient.has_active_appointment ? 'Yes' : 'No'" :color="patient.has_active_appointment ? 'success' : 'secondary'"/>
      
    </td>
    <td>
      <Btn label="View" class="btn-outline-secondary btn-sm" @click="openPatientProfilePage(patient.patient_id)"/>
    </td>
  </tr>
</template>
