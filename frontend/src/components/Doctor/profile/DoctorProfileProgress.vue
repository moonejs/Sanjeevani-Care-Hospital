<script setup>
import { computed , ref,watch } from "vue"
import { useDoctorStore } from "@/stores/doctor.store"

const store = useDoctorStore()


const percentage = computed(() => {
  if (!store.doctorProfile) return 0
  return store.doctorProfile.completion_percentage || 0
})

const color = ref('bg-danger')

const updateColor = () => {
  if (percentage.value <= 25) {
    color.value = 'bg-danger'
  } else if (percentage.value < 100) {
    color.value = 'bg-warning'
  } else {
    color.value = 'bg-success'
  }
}

watch(percentage, updateColor)

</script>

<template>
  <div class="mt-2">
    <div class="progress-wrapper">
      <div class="progress-info">
        <span class="h4 progress-tooltip " :class="color">Profile Complete</span>
        <div class="progress-percentage">
            <strong>{{ percentage }}%</strong>
        </div>
      </div>
      <div class="progress" style="height: 0.6rem">
            <div class="progress-bar progress-bar-striped progress-bar-animated" :class="color"
            :style="{ width: percentage + '%' } " >
            </div>
      </div>
    </div>
    
   
  </div>
</template>
