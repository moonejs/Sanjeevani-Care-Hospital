<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import { RouterLink } from 'vue-router';

const scrollY = ref(0);

const handleScroll = () => {
  scrollY.value = window.scrollY;
};


const scrollTo = (id, event) => {
  event.preventDefault();
  const el = document.getElementById(id);
  if (el) {
    el.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
};

onMounted(() => window.addEventListener('scroll', handleScroll));
onUnmounted(() => window.removeEventListener('scroll', handleScroll));
</script>

<template>
  <nav class="sc-nav" :class="{ 'sc-nav--scrolled': scrollY > 60 }">
    <div class="container-xl d-flex align-items-center justify-content-between py-2">


      <RouterLink to="/" class="sc-logo d-flex align-items-center gap-2 text-decoration-none">
        <img src="../../../../public/logoHMS.png" alt="Sanjeevani Logo" height="42" width="42" />
        <div>
          <div class="logo-name">Sanj<span class="text-instagram">ee</span>vani</div>
          <div class="logo-sub">Care Hospital</div>
        </div>
      </RouterLink>

     
      <ul class="d-none d-lg-flex list-unstyled mb-0 gap-4 align-items-center">
        <li><a href="#about"        class="sc-nav-link" @click="scrollTo('about', $event)">About</a></li>
        <li><a href="#departments"  class="sc-nav-link" @click="scrollTo('departments', $event)">Departments</a></li>
        <li><a href="#doctors"      class="sc-nav-link" @click="scrollTo('doctors', $event)">Doctors</a></li>
        <li><a href="#services"     class="sc-nav-link" @click="scrollTo('services', $event)">Services</a></li>
        <li><a href="#contact"      class="sc-nav-link" @click="scrollTo('contact', $event)">Contact</a></li>
      </ul>


      <div class="d-flex gap-2 align-items-center">
        <RouterLink to="/login"    class="btn btn-outline-secondary btn-sm px-4 py-2">Login</RouterLink>
        <RouterLink to="/register" class="btn btn-secondary btn-sm px-3 py-2">Book Appointment</RouterLink>
      </div>

    </div>
  </nav>
</template>

<style scoped>
.sc-nav {
  position: fixed;
  top: 0; left: 0; right: 0;
  z-index: 1000;
  padding: 4px 0;

  border-bottom: 1px solid transparent;
  transition: background 0.3s ease, backdrop-filter 0.3s ease,
              border-color 0.3s ease, box-shadow 0.3s ease;
}


.sc-nav--scrolled {
  background: rgba(255, 255, 255, 0.85);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border-bottom-color: rgba(0, 0, 0, 0.08);
  box-shadow: 0 2px 16px rgba(0, 0, 0, 0.06);
}

.sc-logo { color: inherit; }

.logo-name {
  font-weight: 900;
  font-size: 1.1rem;
  line-height: 1;
  color: #0d0d0d;
}

.logo-sub {
  font-size: 0.65rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: #6b7280;
}

.sc-nav-link {
  font-size: 0.88rem;
  font-weight: 500;
  text-decoration: none;
  letter-spacing: 0.02em;
  color: #374151;
  transition: color 0.2s;
  cursor: pointer;
}

.sc-nav-link:hover {
  color: #000;
}
</style>