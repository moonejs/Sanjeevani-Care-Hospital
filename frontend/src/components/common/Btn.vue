<script setup>
    defineProps({
        type:String,
        label:String,
        disabled:Boolean,
        loader:Boolean
    })
    const emit=defineEmits(['click'])
</script>
<template>
    <button  class="btn"  :disabled="disabled" :type="type" @click="emit('click')">
         <span v-if="loader" class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
        {{ label }}
        </button>
</template>