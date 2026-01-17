<script setup>
    import { RouterView } from 'vue-router';
    import DoctorNavbar from '@/components/layout/Doctor/DoctorNavbar.vue';
    import Time from '@/components/Doctor/Time.vue';
</script>

<template>
    <DoctorNavbar/>
    <Time/>
    <RouterView/>
</template>