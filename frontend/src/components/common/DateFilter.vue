<script setup>
const props = defineProps({
    modelValue: String,
    label: {
        type: String,
        default: "Select Date"
    }
})

const emit = defineEmits(['update:modelValue'])
</script>

<template>
    <div class="mb-3">
        <label class="form-label">{{ label }}</label>
        <input 
            type="date"
            class="form-control"
            :value="modelValue"
            @input="emit('update:modelValue', $event.target.value)"
        />
    </div>
</template>