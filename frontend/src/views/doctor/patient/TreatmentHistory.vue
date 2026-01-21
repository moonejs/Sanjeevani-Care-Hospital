<script setup>
    defineProps({
    treatments: Array
    })
</script>

<template>
  <div class="">
    <h5 class="mb-2">Treatment History</h5>

    <div v-for="t in treatments" :key="t.appointment_id" class="bg-info-subtle  p-2 mb-2">
      <p><b>Diagnosis:</b> {{ t.diagnosis }}</p>
      <p><b>Notes:</b> {{ t.notes || '—' }}</p>

      <div v-if="t.medicines?.length">
        <b>Medicines:</b>
        <ul class="mb-1">
          <li v-for="(m,i) in t.medicines" :key="i">
            {{ m.name }} – {{ m.dose }} – {{ m.frequency }}
          </li>
        </ul>
      </div>

      <p v-if="t.follow_up_date">
        <b>Follow-up:</b> {{ t.follow_up_date }}
      </p>
    </div>

    <p v-if="!treatments.length" class="text-muted">
      No treatment records
    </p>
  </div>
</template>
