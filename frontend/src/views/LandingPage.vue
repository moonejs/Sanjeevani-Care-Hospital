<script setup>
    import { RouterLink } from 'vue-router';
</script>

<template>
    <div class="container text-center">
        <h1>Ladning Page</h1>
        <RouterLink class="btn-primary btn" to="/login" > Login </RouterLink>
        <RouterLink class="btn-info mx-2 btn" to="/register"> Register </RouterLink>

    </div>
</template>
