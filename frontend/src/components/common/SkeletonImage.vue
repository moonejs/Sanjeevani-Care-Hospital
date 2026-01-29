<script setup>
defineProps({
  size: { type: String, default: "100px" },
  circle: Boolean
})
</script>

<template>
  <span
    class="placeholder"
    :style="{
      width: size,
      height: size,
      borderRadius: circle ? '50%' : '6px',
      display: 'block'
    }"
  ></span>
</template>
