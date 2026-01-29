<script setup>
import SkeletonImage from "./SkeletonImage.vue"
import SkeletonText from "./SkeletonText.vue"

defineProps({
  image: Boolean,
  imageCircle: Boolean,
  lines: {
    type: Number,
    default: 3
  }
})
</script>

<template>
  <div class="d-flex gap-3 align-items-start">
    <SkeletonImage
      v-if="image"
      :circle="imageCircle"
      size="100px"
    />
    <div class="flex-grow-1">
      <SkeletonText :lines="lines" />
    </div>
  </div>
</template>
