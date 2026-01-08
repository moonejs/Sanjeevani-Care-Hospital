<script setup>
    import { ref } from 'vue';
    import NavLink from '../common/NavLink.vue';
    import Profile from '../common/NavProfile.vue';
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
                    <NavLink label="Home" route="/patient/dashboard"/>
                </div>
                <div class="nav-item">
                    <NavLink label="Departments" route="/patient/departments"/>
                </div>
                <div class="nav-item">
                    <NavLink label="Doctors" route="/patient/doctors"/>
                </div>
                <div class="dropdown">
                    <NavLink class="dropdown-toggle" label="Appointment" route="/patient/appointments" role="button" data-bs-toggle="dropdown" aria-expanded="false"/>
                    <ul class="dropdown-menu">
                        <li>
                            <NavLink label="Book Appointment" route="/patient/appointments/new"/>
                        </li>
                        <li><hr class="dropdown-divider"></li>
                        <li>
                            <NavLink label="My Appointments " route="/patient/appointments"/>
                        </li>
                        
                    </ul>
                </div>
                <div class="dropdown">
                    <NavLink class="dropdown-toggle" label="Medical Records" route="/patient/history" role="button" data-bs-toggle="dropdown" aria-expanded="false"/>
                    <ul class="dropdown-menu">
                        <li>
                            <NavLink label="Medical History" route="/patient/medical-records/history"/>
                        </li>
                        <li><hr class="dropdown-divider"></li>
                        <li>
                            <NavLink label="Bills & Payments" route="/patient/medical-records/billing"/>
                        </li>
                        
                    </ul>
                </div>
                
            </div>
            <div>
                <Profile/>
            </div>
        </div>
    </nav>
</template>