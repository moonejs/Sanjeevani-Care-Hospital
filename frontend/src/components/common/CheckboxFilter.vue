<script setup>
const props = defineProps({
    modelValue: Array,
    options: Array,
    label: String,
    name: String 
    
})

const emit = defineEmits(['update:modelValue'])

function toggle(option) {
    let updated = [...props.modelValue]

    if (updated.includes(option)) {
        updated = updated.filter(item => item !== option)
    } else {
        updated.push(option)
    }

    emit('update:modelValue', updated)
}
</script>

<template>
    <div class="mb-3">
        <label class="form-label">{{ label }}</label>

        <div class="form-check" v-for="option in options" :key="option">
            <input 
                :id="`${name}-${option.v}`"
                class="form-check-input"
                type="checkbox"
                :checked="modelValue.includes(option.v)"
                @change="toggle(option.v)""
            />
            <label class="form-check-label" :for="`${name}-${option.v}`">
                {{ option.l }}
            </label>
        </div>
    </div>
</template>