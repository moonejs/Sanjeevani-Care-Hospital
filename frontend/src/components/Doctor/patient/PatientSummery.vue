<script setup>
    defineProps({
        patient:Object
    })
</script>
<template>
  <div class="">
    
    <h4>Patient Name : {{ patient.name }}</h4>
    <h4>Age : {{ patient.age }}</h4>
    <h4>Gender :{{ patient.gender}}</h4>
    
  </div>
</template>
