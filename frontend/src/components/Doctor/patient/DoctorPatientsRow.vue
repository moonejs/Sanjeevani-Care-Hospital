<script setup>
    import Btn from '@/components/common/Btn.vue'
    import { useRouter } from 'vue-router'

    defineProps({
        patient: Object,
        index: Number
    })

    const router = useRouter()

    function viewProfile() {
        router.push({
            name: 'patientProfile-doctor',
            params: { id: patient.patient_id }
        })
    }
</script>

<template>
  <tr>
    <th scope="row">
          {{ index+1 }}
    </th>
    <td>{{ patient.name }}</td>
    <td>{{ patient.age }}</td>
    <td>{{ patient.gender }}</td>
    <td>{{ patient.last_visit || '—' }}</td>
    <td>{{ patient.total_visits }}</td>
    <td>
      <span class="badge" :class="patient.has_active_appointment ? 'bg-success' : 'bg-secondary'">
        {{ patient.has_active_appointment ? 'Yes' : 'No' }}
      </span>
    </td>
    <td>
      <Btn label="View" class="btn-outline-primary btn-sm" @click="viewProfile"/>
    </td>
  </tr>
</template>
