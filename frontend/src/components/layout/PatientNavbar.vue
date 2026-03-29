<script setup>
    import NavLink from '../common/NavLink.vue';
    import NavProfile from '../common/NavProfile.vue';
</script>

<template>
  <nav class="navbar navbar-expand-lg custom-navbar px-3">
    <div class="container-fluid">
      <a class="navbar-brand fw-semibold py-0">
        <img src="../../../../public/logoHMS.png" alt="">
      </a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarMain">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarMain">
        <ul class="navbar-nav ms-3 gap-1">

          <li class="nav-item">
            <NavLink label="Home" route="/patient/dashboard"/>
          </li>

          <li class="nav-item">
            <NavLink label="Doctors" route="/patient/doctors"/>
          </li>

          <li class="nav-item">
            <NavLink label="Departments" route="/patient/departments"/>
          </li>

          <li class="nav-item dropdown">
            <a class="nav-link custom-link dropdown-toggle" data-bs-toggle="dropdown">
                Appointments
                <span class="fas fa-angle-down dropdown-arrow"></span>
            </a>
            <ul class="dropdown-menu custom-dropdown">
              <li>
                <NavLink label="Book Appointment" route="/patient/appointments/new" />
              </li>
              
              <li><hr class="dropdown-divider "></li>
              <li>
                <NavLink label="My Appointments" route="/patient/appointments"/>
              </li>
            </ul>
          </li>
        </ul>

        <div class="ms-auto d-flex align-items-center">
          <NavProfile/>
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

.nav-link,.custom-link {
  color: #495057;
  font-weight: 500;
  border-radius: 2px;
  padding: 6px 12px;
  transition: all 0.2s ease;
  font-size: 0.9rem;
}

.nav-link:hover,
.custom-link:hover {
  background-color:#2d3753 ;
  color: #FCFDFD;
}

.custom-link:hover span  {
  color: #FCFDFD;
}

.nav-link.active {
  background-color: #242E4C;
  color: #FCFDFD !important;
}


.custom-dropdown {
  border: 1px solid var(--hms-bg-canvas);
  border-radius: 10px;
  padding: 10px;
  background-color: #f0f2f4;
}


.custom-dropdown {
  border-radius: 2px;
}
</style>