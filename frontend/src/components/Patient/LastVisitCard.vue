<script setup>
    import Btn from '@/components/common/Btn.vue'
    import { useRouter } from 'vue-router';

    const router=useRouter()

    function viewAppointments(){
      router.push({
        name: "my-appointments"
      })
    }
    const props=defineProps({
        visit: Object,
        loading: Boolean
    })
</script>
<template>
  <div class="border-top rounded-start-2 border-bottom border-end visit-card p-3">

    <div v-if="loading" class="text-muted small">
      Loading...
    </div>

    <div v-else-if="visit">

      <div class="mb-2">
        <span class="text-muted small">Diagnosis:</span><br/>
        <span>{{ visit.diagnosis }}</span>
      </div>

      <div v-if="visit.medicines?.length" class="mb-2">
        <span class="text-muted small">Medicines:</span><br/>
        <span>
          {{ visit.medicines.map(m => m.name).join(', ') }}
        </span>
      </div>

      <div v-if="visit.follow_up_date" class="mb-2">
        <span class="text-muted small">Follow-up:</span><br/>
        <span>{{ visit.follow_up_date }}</span>
      </div>

      <Btn label="View all records" class="btn-outline-secondary btn-sm mt-2"@click="viewAppointments"/>

    </div>

    <div v-else class="text-muted small">
      No previous visits found
    </div>

  </div>
</template>

<style scoped>
.visit-card {
  border-left: 4px solid #151616;
  background-color: #f0f2f4;
}

</style>