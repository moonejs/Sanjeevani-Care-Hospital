<script setup>
    defineProps({
        label:String,
        for:String,
        required:Boolean
    })
</script>
<template>
    <label class="form-label" :for="for">{{ label }} <span v-if="required" class="text-danger">*</span></label>
</template>