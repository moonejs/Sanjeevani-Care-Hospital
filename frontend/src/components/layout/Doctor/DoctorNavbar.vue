<script setup>
    import NavLink from '@/components/common/NavLink.vue';
    import NavProfile from '@/components/common/NavProfile.vue';
</script>

<template>
    <nav class="navbar navbar-expand-lg custom-navbar px-3">
        <div class="container-fluid">
            <a class="navbar-brand fw-semibold">
                HMS
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarMain">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarMain">
                <ul class="navbar-nav ms-3 gap-1">
                    <li class="nav-item">
                        <NavLink label="Dashboard" route="/doctor/dashboard"/>
                    </li>
                    <li class="nav-item">
                        <NavLink label="Schedule" route="/doctor/schedule"/>
                    </li>
                    <li class="nav-item">
                        <NavLink label="Appointments" route="/doctor/appointments"/>
                    </li>
                    <li class="nav-item">
                        <NavLink label="Patients" route="/doctor/patients"/>
                    </li>
                </ul>
                <div class="ms-auto d-flex align-items-center">
                    <NavProfile role="doctor"/>
                </div>
            </div>
        </div>
    </nav>
</template>

<style scoped>
.custom-navbar {
    background-color: var(--hms-bg-canvas);
    border-bottom: 2px solid #e9ecef;
}

.nav-link {
    color: #495057;
    font-weight: 500;
    border-radius: 2px;
    padding: 6px 12px;
    transition: all 0.2s ease;
    font-size: 0.9rem;
}

.nav-link:hover {
    background-color: #2d3753;
    color: #FCFDFD;
}

.nav-link.active {
    background-color: #242E4C;
    color: #FCFDFD !important;
}
</style>