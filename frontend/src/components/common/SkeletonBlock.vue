<script setup>
  defineProps({
    width: { type: String, default: "100%" },
    height: { type: String, default: "1rem" },
    radius: { type: String, default: "4px" }
  })
</script>

<template>
  <div class="placeholder-glow">
    <span
      class="placeholder"
      :style="{ width, height, borderRadius: radius }"
    ></span>
  </div>
</template>
