<script setup>
    import NavLink from '@/components/common/NavLink.vue';
    import NavProfile from '@/components/common/NavProfile.vue';
</script>

<template>
        <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">Navbar</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse container bg-warning d-flex justify-content-center" id="navbarSupportedContent">
                <div class="nav-item">
                    <NavLink label="Dashboard" route="/doctor/dashboard"/>
                </div>
                <div class="nav-item">
                    <NavLink label="Schedule" route="/doctor/schedule"/>
                </div>
                <div class="nav-item">
                    <NavLink label="Appointments" route="/doctor/appointments"/>
                </div>
                <div class="nav-item">
                    <NavLink label="Patients" route="/doctor/patients"/>
                </div>
                
            </div>
            <div>
                <NavProfile role="doctor"/>
            </div>
        </div>
    </nav>
</template>