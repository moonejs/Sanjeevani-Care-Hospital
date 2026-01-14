<script setup>
    defineProps({
        id:String,
        type:String,
        placeholder:String,
        disabled:Boolean
    })
    const model=defineModel()
</script>
<template>
    <input :type="type" v-model="model" :placeholder="placeholder" :id="id"class="form-control" :disabled="disabled">
</template>