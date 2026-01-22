<script setup>
defineProps({
  pagination: Object
})
const emit = defineEmits(['change'])
</script>

<template>
  <nav class="d-flex justify-content-end mt-3 me-5">
    <ul class="pagination">
      <li class="page-item" :class="{ disabled: pagination.page === 1 }">
        <button class="page-link" @click="emit('change', pagination.page - 1)">
          Prev
        </button>
      </li>

      <li class="page-item disabled">
        <span class="page-link">
          Page {{ pagination.page }} of {{ pagination.pages }}
        </span>
      </li>

      <li class="page-item" :class="{ disabled: pagination.page === pagination.pages }">
        <button class="page-link" @click="emit('change', pagination.page + 1)">
          Next
        </button>
      </li>

    </ul>
  </nav>
</template>
