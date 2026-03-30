<script setup>
import { RouterLink } from 'vue-router';
import { ref, onMounted, onUnmounted } from 'vue';
import { Hospital,Phone,Ambulance,Clock,MapPin,Mail  } from 'lucide-vue-next';
import LandingPageNav from '@/components/layout/Landing/LandingPageNav.vue';

const scrollY = ref(0);
const statsVisible = ref(false);
const statsSection = ref(null);

const handleScroll = () => {
  scrollY.value = window.scrollY;
};

const testimonials = [
  { name: 'Ananya R.', text: 'The care I received at Sanjeevani was exceptional. The doctors took time to explain everything clearly and made me feel at ease throughout my treatment.', rating: 5, dept: 'Cardiology' },
  { name: 'Vikram S.', text: 'World-class facilities and a compassionate team. My father\'s recovery after the surgery was remarkable. Forever grateful to the entire staff.', rating: 5, dept: 'Orthopedics' },
  { name: 'Meera P.', text: 'The OPD system is seamless, staff is courteous, and the doctors are brilliant. Sanjeevani truly lives up to its name — a life-giving hospital.', rating: 5, dept: 'Gynecology' },
];

onMounted(() => {
  window.addEventListener('scroll', handleScroll);
  const observer = new IntersectionObserver(
    ([entry]) => { if (entry.isIntersecting) statsVisible.value = true; },
    { threshold: 0.3 }
  );
  if (statsSection.value) observer.observe(statsSection.value);
});

onUnmounted(() => window.removeEventListener('scroll', handleScroll));
</script>

<template>
  <div class="sc-root">
    <LandingPageNav/>
    <section class="main-content ">

      <div class="sc-marquee-wrap  py-0">
        <div class="sc-marquee">
          <span v-for="i in 3" :key="i">
            ✚ Cardiology &nbsp;&nbsp; ✚ Neurology &nbsp;&nbsp; ✚ Oncology &nbsp;&nbsp; ✚ Orthopedics &nbsp;&nbsp; ✚ Maternity &nbsp;&nbsp; ✚ Dental &nbsp;&nbsp; ✚ Emergency &amp; Trauma &nbsp;&nbsp; ✚ Diagnostics &nbsp;&nbsp; ✚ Pharmacy &nbsp;&nbsp; ✚ Gastroenterology &nbsp;&nbsp; ✚ Pulmonology &nbsp;&nbsp; ✚ Nephrology &nbsp;&nbsp; ✚ Endocrinology &nbsp;&nbsp; ✚ Rheumatology &nbsp;&nbsp; ✚ Dermatology &nbsp;&nbsp; ✚ ENT &nbsp;&nbsp; ✚ Ophthalmology &nbsp;&nbsp; ✚ Psychiatry &nbsp;&nbsp; ✚ Urology &nbsp;&nbsp;
          </span>
        </div>
      </div>

      <div class="container">
        <div class="row align-items-center  mt-4">
          <div class="col-lg-6 main-content-text">
            <div class="small mb-2"><Hospital size="1rem" class="me-2"/> <span class="">Est. 2005 · NABH Accredited</span></div>
            <h1 class="main-content-h1">
              Healing with<br/>
              <span class="text-italic">Compa<span class="text-instagram">ss</span>ion,</span><br/>
              <span class="text-underline">Excellence</span> &amp;<br/>
              <span class="">Modern <span>Science</span></span>
            </h1>
            <p class="main-content-sub mt-4">
              <span class="fw-semibold">Sanj<span class="text-instagram">ee</span>vani</span> Care Hospital — where cutting-edge medical technology meets the warmth of personalised care.
              Trusted by <strong>2 lakh+ patients</strong> across Central India.
            </p>

            <div class="d-flex flex-wrap gap-3 mt-4">
              <div class="sc-pill"><span class="sc-pill-num">500+</span><span class="sc-pill-lbl">Specialists</span></div>
              <div class="sc-pill"><span class="sc-pill-num text-instagram">50+</span><span class="sc-pill-lbl">Departments</span></div>
              <div class="sc-pill"><span class="sc-pill-num">24/7</span><span class="sc-pill-lbl">Emergency</span></div>
            </div>

            <div class="d-flex flex-wrap gap-3 mt-4">
              <RouterLink to="/register" class="btn btn-dark animate-right-2">
                Book Appointment →
              </RouterLink>
              <a href="tel:+911800000000" class="btn btn-outline-dark ">
                <Phone size="1.2rem" color="red"/> Emergency Helpline
              </a>
            </div>
          </div>

          <div class="col-lg-6 d-flex justify-content-center mt-5 mt-lg-0 ">
            <div class="right-content-img" height="500px" width="400px">
              <img src="../assets/images/img-3.png" alt="" class="ms-6 mb-5" style="">
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class=" py-5" id="about" >
      <div class="container">
        <div class="row gap-7">
          <div class="col-lg-5  ">
            <img src="../assets/images/img-4.png" alt="">
          </div>
          <div class="col-lg-5 ">
            <div class="small ">Our Legacy</div>
            <h2 class="sc-section-h2">Two Decades of <em>Saving Lives</em></h2>
            <p class=" mt-3">
              Since 2005, Sanjeevani Care Hospital has been a beacon of hope for patients across Madhya Pradesh and beyond.
              Our state-of-the-art 800-bed facility houses 50+ specialities under one roof, powered by <b>500+</b> empanelled specialists and a support staff of <b>2,000+</b>.
            </p>
            <p class="">
              We combine the precision of modern medical science with the empathy of traditional Indian care — treating not just the disease, but the whole person.
            </p>
          </div>
        </div>
      </div>
    </section>


    <section class="py-5" id="departments">
      <div class="container">
        <div class="text-center mb-5">
          <div class="text-uppercase small">Specialities</div>
          <h2 class="sc-section-h2">50+ Departments, <em>One Destination</em></h2>
          <p class=" sc-section-body--center">
            From routine check-ups to complex surgeries — every speciality, every need, all under one roof.
          </p>
        </div>

        <div class="row g-6">
          <div class="col">
            <img src="../assets/images/img-5.png" height="370px" width="450px" alt="">
          </div>
          <div class="col">
            <img src="../assets/images/img-2.png" alt="">
          </div>
        </div>

        <div class="text-center mt-5">
          <a href="#" class="btn btn-outline-secondary sc-btn-outline sc-btn-lg">View All 50+ Departments →</a>
        </div>
      </div>
    </section>

    

    <section class="py-4">
      <div class="container">
        <div class="text-center mb-5">
          <div class="small text-uppercase">Patient Stories</div>
          <h2 class="sc-section-h2">Thousands Healed, <em>Mi<span class="text-instagram">ll</span>ions Grateful</em></h2>
        </div>
        <div class="row g-4">
          <div v-for="(t, i) in testimonials" :key="i" class="col-lg-4">
            <div class="sc-testi-card">
              <div class="sc-testi-quote">"</div>
              <p class="sc-testi-text">{{ t.text }}</p>
              <div class="d-flex align-items-center gap-3 mt-4">
                <div class="sc-testi-avatar">{{ t.name.charAt(0) }}</div>
                <div>
                  <div class="sc-testi-name">{{ t.name }}</div>
                  <div class="sc-testi-dept">{{ t.dept }} Patient</div>
                </div>
                <div class="ms-auto sc-testi-stars">{{ '★'.repeat(t.rating) }}</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>


    <section class="sc-emergency py-5">
      <div class="container">
        <div class="sc-emergency-card">
          <div class="row align-items-center g-4">
            <div class="col-lg-7">
              <h3 class="sc-emergency-h3">Medical <span class="text-instagram">Emergency?</span> <em>We're Here 24/7</em></h3>
              <p class="sc-emergency-sub">Our trauma and emergency department is fully equipped and staffed round-the-clock. Ambulance services available across the city with GPS tracking.</p>
            </div>
            <div class="col-lg-3 text-lg-end">
              <a href="tel:+911800000000" class="btn btn-secondary sc-btn-primary sc-btn-lg d-block mb-2">
                <Phone size="1rem"/> Call Emergency
              </a>
              <a href="#" class="btn btn-outline-secondary sc-btn-outline sc-btn-lg d-block">
                <Ambulance size="1rem"/> Book Ambulance
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <footer class="sc-footer pt-5 pb-3 border-top" id="contact">
      <div class="container">
        <div class="row g-5">
          <div class="col-lg-4">
            <div class="d-flex align-items-center gap-2 mb-3">
              <img src="../../public/logoHMS.png" height="45rem" width="47rem" alt="">
              <div>
                <div class="logo-name">Sanjeevani</div>
                <div class="logo-sub">Care Hospital</div>
              </div>
            </div>
            <p class="sc-footer-about">
              Sanjeevani Care Hospital is a multi-speciality tertiary care centre committed to providing world-class healthcare with compassion, integrity, and innovation.
            </p>
            <div class="d-flex gap-3 mt-3">
              <i class="fab fa-facebook me-2"></i>
              <i class="fab fa-dribbble me-2"></i>
              <i class="fab fa-reddit me-2"></i>
              <i class="fab fa-twitter"></i>
            </div>
          </div>

          <div class="col-sm-6 col-lg-2">
            <h6 class="sc-footer-heading">Hospital</h6>
            <ul class="list-unstyled sc-footer-links">
              <li><a href="#">About Us</a></li>
              <li><a href="#">Our Doctors</a></li>
              <li><a href="#">Departments</a></li>
              <li><a href="#">Facilities</a></li>
              <li><a href="#">Careers</a></li>
            </ul>
          </div>

          <div class="col-sm-6 col-lg-2">
            <h6 class="sc-footer-heading">Services</h6>
            <ul class="list-unstyled sc-footer-links">
              <li><a href="#">OPD Consultation</a></li>
              <li><a href="#">Emergency</a></li>
              <li><a href="#">Tele-Medicine</a></li>
              <li><a href="#">Diagnostics</a></li>
              <li><a href="#">Health Packages</a></li>
            </ul>
          </div>

          <div class="col-lg-4">
            <h6 class="sc-footer-heading">Get in Touch</h6>
            <div class="sc-contact-item"><MapPin size="1rem" /> 123, Medical Zone, Bhopal, MP — 462001</div>
            <div class="sc-contact-item"><Phone size="1rem"/> 1800-000-0000 (Toll Free)</div>
            <div class="sc-contact-item"><Mail  size="1rem"/> care@sanjeevani.in</div>
            <div class="sc-contact-item"><Clock  size="1rem"/> OPD: Mon–Sat, 8 AM – 8 PM</div>
            <RouterLink to="/register" class="btn btn-secondary sc-btn-primary w-100 mt-4">
              Book an Appointment
            </RouterLink>
          </div>
        </div>

        <hr class="sc-footer-hr mt-5" />
        <div class="d-flex flex-wrap justify-content-between align-items-center gap-2 py-3">
          <small class="sc-footer-copy">© 2025 Sanjeevani Care Hospital. All rights reserved.</small>
          <div class="d-flex gap-3">
            <a href="#" class="sc-footer-legal">Privacy Policy</a>
            <a href="#" class="sc-footer-legal">Terms of Service</a>
            <a href="#" class="sc-footer-legal">NABH Certificate</a>
          </div>
        </div>
      </div>
    </footer>

  </div>
</template>

<style scoped>

.main-content {
  min-height: 100vh;
  padding-top: 65px;
  position: relative;
  overflow: hidden;
}

.main-content-h1 {
  font-size: clamp(2.4rem, 5vw, 4rem);
  font-weight: 900;
  line-height: 1.1;
}

.main-content-sub {
  font-size: 1.05rem;
  max-width: 500px;
  line-height: 1.7;
}

.sc-pill {
  display: flex; align-items: center; gap: 8px;
  padding: 8px 16px;
}
.sc-pill-num {
  font-weight: 900; font-size: 1.3rem;
}

.sc-pill-lbl { 
  font-size: 0.8rem; 
}

.sc-marquee-wrap {
  overflow: hidden; padding: 14px 0;
}

.sc-marquee {
  display: flex; white-space: nowrap;
  animation: marquee 30s linear infinite;
  font-size: 0.8rem; font-weight: 600;
  letter-spacing: 0.08em; text-transform: uppercase;
  color: var(--sc-text-muted);
}

@keyframes marquee { 
  from{
    transform:translateX(0)
  } 
  to{
    transform:translateX(-33.33%)
  }
}


.sc-section-h2 {
  font-size: clamp(1.8rem, 3.5vw, 2.8rem);
  font-weight: 900; line-height: 1.15;
}
.sc-section-h2 em { font-style: italic;  }
.sc-section-body { line-height: 1.8; }
.sc-section-body--center { max-width: 600px; margin: 0 auto; }


.sc-testi-card {
  padding: 28px 24px;
  height: 100%;
  transition: box-shadow 0.2s;
  position: relative;
}
.sc-testi-card:hover { box-shadow: 0 12px 40px rgba(0,0,0,0.06); }
.sc-testi-quote {
  font-size: 5rem; line-height: 0.5;
  margin-bottom: 16px;
  font-weight: 900;
}
.sc-testi-text { font-size: 0.9rem; line-height: 1.75; }
.sc-testi-avatar {
  width: 40px; height: 40px;
  background: var(--bs-secondary);
  color: #fff; font-weight: 700;
  display: flex; align-items: center; justify-content: center;
  flex-shrink: 0;
}
.sc-testi-name { font-weight: 700; font-size: 0.9rem; }
.sc-testi-dept { font-size: 0.75rem; }
.sc-testi-stars { color: #f5a623; font-size: 0.85rem; }


.sc-emergency-card {
  padding: 40px;
  position: relative;
  overflow: hidden;
}
.sc-emergency-deco {
  position: absolute; right: -20px; top: -20px;
  font-size: 8rem; opacity: 0.04;
  pointer-events: none; user-select: none;
}
.sc-emergency-h3 {
  font-size: clamp(1.3rem, 2.5vw, 1.8rem);
  font-weight: 900; margin-bottom: 8px;
}
.sc-emergency-h3 em { font-style: italic; color: var(--bs-secondary); }
.sc-emergency-sub { font-size: 0.9rem;  line-height: 1.7; margin: 0; }



.sc-footer{
  background-color: #F0F2F4;
}

.sc-footer-about { font-size: 0.85rem;  line-height: 1.7; }
.sc-footer-heading {
  font-size: 0.72rem; text-transform: uppercase;
  letter-spacing: 0.15em; font-weight: 500;
  margin-bottom: 16px;
}
.sc-footer-links li { margin-bottom: 8px; }
.sc-footer-links a {
  font-size: 0.85rem;
  text-decoration: none; transition: color 0.2s;
}

.sc-contact-item { font-size: 0.85rem;margin-bottom: 8px; }


.sc-footer-legal { font-size: 0.78rem; text-decoration: none; }

</style>