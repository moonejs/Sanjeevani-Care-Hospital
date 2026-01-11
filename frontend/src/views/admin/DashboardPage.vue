<script setup>
    import { useAuthStore } from '@/stores/auth.store';
    import { ref } from 'vue';

    const auth = useAuthStore()
    const role = auth.role
</script>

<template>
    <h1>Hello {{role}}</h1>
</template>