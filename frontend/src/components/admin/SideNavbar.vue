<script setup>
    import NavTab from './NavTab.vue';
    import { ref } from 'vue';
    import { useRouter } from 'vue-router';
    import Btn from '../common/Btn.vue';
    import { useAuthStore } from '@/stores/auth.store';
    import { useToastStore } from '@/stores/toast.store';

    const router=useRouter()
    const auth=useAuthStore()
    const toast = useToastStore()
    const navs = ref([
        { label: "Dashboard", route: "/admin/dashboard" },
        { label: "Doctors", route: "/admin/doctors" },
        { label: "Appointments", route: "/admin/appointments" },
        { label: "Departments", route: "/admin/departments" },
        { label: "Patients", route: "/admin/patients" }
    ])

    function logout(){
        auth.logout()
        router.replace('/')
        toast.addToast({
            message: "Logout Successfully",
            type: 'success'
        })
    }
</script>
<template>
    
    <div class="collapse collapse-horizontal show" id="navbarToggleExternalContent" data-bs-theme="dark">
        <div class="list-group list-group-flush gap-4 px-4 pt-7" style="width: 300px;">
            <NavTab v-for="(nav,i) in navs" :label="nav.label" :key="i" :route="nav.route"/>
        </div>
        <div class=" text-center mt-10">
            <Btn label="Logout" class="btn-outline-danger px-5" @click="logout"/>
        </div>
    </div>
</template>