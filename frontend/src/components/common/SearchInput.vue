<script setup>
const props = defineProps({
    modelValue: String,
    placeholder: {
        type: String,
        default: "Search..."
    }
})

const emit = defineEmits(['update:modelValue'])
</script>

<template>
    <div class="mb-3 position-relative">
        <input 
            :value="modelValue"
            @input="emit('update:modelValue', $event.target.value)"
            type="text"
            class="form-control ps-5"
            :placeholder="placeholder"
        />
        <i class="bi bi-search position-absolute top-50 start-0 translate-middle-y ms-3"></i>
    </div>
</template>