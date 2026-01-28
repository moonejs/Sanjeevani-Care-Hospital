<script setup>
defineProps({
  departments: Array,
  specializations: Array,
  modelValue: Object
})

const emit = defineEmits(["update:modelValue"])

function update(key, value) {
  emit("update:modelValue", {
    ...modelValue,
    [key]: value
  })
}
</script>

<template>
  <div class="card p-3">
    <h6 class="mb-3">Narrow Your Search</h6>

    <div class="mb-3">
      <strong>By Department</strong>
      <div v-for="d in departments" :key="d">
        <input
          type="radio"
          :value="d"
          name="department"
          @change="update('department', d)"
        />
        {{ d }}
      </div>
    </div>

    <div>
      <strong>By Specialty</strong>
      <div v-for="s in specializations" :key="s">
        <input
          type="checkbox"
          :value="s"
          @change="update('specialization', s)"
        />
        {{ s }}
      </div>
    </div>
  </div>
</template>
