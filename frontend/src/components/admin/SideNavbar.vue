<script setup>
    import NavTab from './NavTab.vue';
    import { ref } from 'vue';
    import { useRouter } from 'vue-router';

    const router=useRouter()
    const navs = ref([
        { label: "Dashboard", route: "/admin/dashboard" },
        { label: "Doctors", route: "/admin/doctors" },
        { label: "Appointments", route: "/admin/appointments" },
        { label: "Departments", route: "/admin/departments" },
        { label: "Patients", route: "/admin/patients" }
    ])
</script>
<template>
    
    <div class="collapse collapse-horizontal show" id="navbarToggleExternalContent" data-bs-theme="dark">
        <div class="list-group list-group-flush gap-4 px-4 pt-7" style="width: 300px;">
            <NavTab v-for="(nav,i) in navs" :label="nav.label" :key="i" :route="nav.route"/>
        </div>
    </div>
</template>