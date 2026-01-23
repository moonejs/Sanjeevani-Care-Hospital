<script setup>
    import Btn from '@/components/common/Btn.vue'

    defineProps({
        visit: Object,
        loading: Boolean
    })
</script>

<template>
  <div class="bg-danger-subtle shadow-sm">
    <div class="card-body">

      <h5 class="card-title mb-3">Last Visit Summary</h5>

      <div v-if="loading" class="text-muted">
        Loading...
      </div>

      <div v-else-if="visit">
        <p><b>Diagnosis:</b> {{ visit.diagnosis }}</p>

        <p v-if="visit.medicines?.length">
          <b>Medicines:</b>
          <span v-for="(m, i) in visit.medicines" :key="i">
            {{ m.name }}{{ i < visit.medicines.length - 1 ? ', ' : '' }}
          </span>
        </p>

        <p v-if="visit.follow_up_date">
          <b>Follow-up:</b> {{ visit.follow_up_date }}
        </p>

        <Btn label="View all records" class="btn-outline-secondary btn-sm mt-2"
        />
      </div>

      <div v-else class="text-muted">
        No previous visits found
      </div>

    </div>
  </div>
</template>
