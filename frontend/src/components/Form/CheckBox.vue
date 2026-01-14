<script setup>
    defineProps({
        id:String,
        disabled:Boolean
    })
    const model=defineModel()
</script> 

<template >
    <input class="form-check-input" type="checkbox" v-model="model" :id="id" :disabled="disabled">
</template>