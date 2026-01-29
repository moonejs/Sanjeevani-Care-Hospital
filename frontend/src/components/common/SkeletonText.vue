<script setup>
defineProps({
  lines: { type: Number, default: 3 }
})
</script>

<template>
  <div class="placeholder-glow">
    <span
      v-for="i in lines"
      :key="i"
      class="placeholder col-12 mb-2"
    ></span>
  </div>
</template>
