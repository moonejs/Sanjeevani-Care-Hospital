<script setup>
    defineProps({
        label:String,
        color:String,
        cross:Boolean
    })

    const emit =defineEmits(['click'])
</script>

<template>
    <span class="badge" :class="`text-bg-${color}`" @click="emit('click')">{{ label }}
        <span v-if="cross" class="ms-2 pointer" @click="emit('click')">×</span>

    </span>
</template>