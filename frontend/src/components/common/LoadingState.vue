<script setup>
  defineProps({
    loading: Boolean,

    type: {
      type: String,
      default: "spinner"
    },

    count: {
      type: Number,
      default: 3
    }
  })
</script>

<template>
    <template v-if="loading">
      <div v-if="type === 'spinner'" class="text-center py-5">
        <div class="spinner-border text-primary" role="status"></div>
      </div>

      <template v-else>
        <slot name="skeleton" v-for="i in count" :key="i" />
      </template>

    </template>

    <template v-else>
      <slot />
    </template>
</template>
