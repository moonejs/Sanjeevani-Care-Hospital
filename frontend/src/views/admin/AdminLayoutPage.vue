<script setup>
import { RouterView } from 'vue-router';
import SideNavbar from '@/components/admin/SideNavbar.vue';
</script>
<template>
    <div class="bg-secondary-subtle container-fluid admin-dashboard d-flex position-relative px-0">
        <nav class="navbar  position-absolute z-1">
            <div class="container-fluid">
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarToggleExternalContent" aria-controls="navbarToggleExternalContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
                </button>
            </div>
        </nav>
        <div class="bg-success admin-navbar">
            <SideNavbar/>
            
        </div>
        <div class="admin-main-dashboard-container bg-danger-subtle">
            <RouterView/>
        </div>
    </div>
    
</template>