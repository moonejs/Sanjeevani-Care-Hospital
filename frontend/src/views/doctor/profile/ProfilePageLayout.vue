<script setup>
    import { ref, computed, onMounted } from "vue"
    import { useDoctorStore } from "@/stores/doctor.store"

    import DoctorProfileSidebar from "@/components/Doctor/profile/DoctorProfileSidebar.vue"
    import DoctorProfileHeader from "@/components/Doctor/profile/DoctorProfileHeader.vue"
    import DoctorProfileProgress from "@/components/Doctor/profile/DoctorProfileProgress.vue"

    import PersonalDetails from "./section/PersonalDetails.vue"
    import EducationDetails from "./section/EducationDetails.vue"
    import RegistrationDocuments from "./section/RegistrationDocuments.vue"
    import ClinicsTiming from "./section/ClinicsTiming.vue"
    import ServicesExperience from "./section/ServicesExperience.vue"
    import AwardsMemberships from "./section/AwardsMemberships.vue"

    const doctorStore = useDoctorStore()
    const activeSection = ref("personal")

    onMounted(() => {
        doctorStore.fetchCurrrentDoctorDetails()
    })

    const sectionComponent = computed(() => ({
        personal: PersonalDetails,
        education: EducationDetails,
        registration: RegistrationDocuments,
        clinics: ClinicsTiming,
        services: ServicesExperience,
        awards: AwardsMemberships
    }))

    function changeActiveSection(newSection){
        console.log(newSection);
        
        activeSection.value=newSection
    }
    
</script>

<template>
  <div class="container-fluid mt-3">
    <DoctorProfileHeader />

    <DoctorProfileProgress />

    <div class="row mt-3">
      <div class="col-3">
        <DoctorProfileSidebar @select="changeActiveSection" :section="activeSection"/>
      </div>

      <div class="col-9">
        <component :is="sectionComponent[activeSection]" />
      </div>
    </div>
  </div>
</template>
