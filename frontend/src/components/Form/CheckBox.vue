<script setup>
    defineProps({
        name:{
            type:String,
            required:true
        },
        id:{
            type:String,
            required:true
        }
    })
</script> 

<template >
    <input class="form-check-input" type="checkbox" :name="name" :id="id">
</template>