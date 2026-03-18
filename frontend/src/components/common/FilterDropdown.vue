<script setup>
const props = defineProps({
    modelValue: String,
    options: Array,
    label: String
})

const emit = defineEmits(['update:modelValue'])
</script>

<template>
    <div class="mb-3">
        <select 
            class="form-select"
            :value="modelValue"
            @change="emit('update:modelValue', $event.target.value)"
        >
            <option value="">All {{ label }}</option>
            <option 
                v-for="option in options" 
                :key="option" 
                :value="option"
            >
                {{ option }}
            </option>
        </select>
    </div>
</template>