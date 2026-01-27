<script setup>
import { computed } from "vue"
import { useDoctorStore } from "@/stores/doctor.store"

const store = useDoctorStore()

const percentage = computed(() =>
  store.doctorProfile?.profile_completed ? 100 : 70
)
</script>

<template>
  <div class="mt-2">
    <strong>{{ percentage }}% Profile Complete</strong>
    <div class="progress">
      <div
        class="progress-bar bg-success"
        :style="{ width: percentage + '%' }"
      ></div>
    </div>
  </div>
</template>
