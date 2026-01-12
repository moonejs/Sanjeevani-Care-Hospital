<script setup>
    defineProps({
        name:String,
        id:String,
        type:String
    })
</script>
<template>
    <input :type="type" :name="name"  :id="id"class="form-control">
</template>