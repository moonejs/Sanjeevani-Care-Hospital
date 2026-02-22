<script setup>
    
    const props = defineProps({
      showModal: Boolean,
      patient:Object
    })

    const emit = defineEmits(['close'])
</script>

<template>
  <div v-if="showModal">
    <div class="modal show" style="display: block;">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">

          <div class="modal-header">
            <h5 class="modal-title">{{ patient?.name }}</h5>
            <button class="btn-close" @click="emit('close')"></button>
          </div>

          <div class="modal-body">
            {{ patient }}
          </div>

          <div class="modal-footer"></div>

        </div>
      </div>
    </div>

    <div class="modal-backdrop fade show"></div>
  </div>
</template>
