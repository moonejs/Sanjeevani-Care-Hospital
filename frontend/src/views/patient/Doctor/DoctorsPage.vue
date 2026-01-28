<script setup>
    import DoctorFilter from "./DoctorFilter.vue"
    import DoctorCard from "./DoctorCard.vue"
    import Loading from "@/components/common/Loading.vue"

    import { useDoctorStore } from "@/stores/doctor.store"
    import { onMounted, ref, computed } from "vue"
    import { useRouter } from "vue-router"

    const doctorStore = useDoctorStore()
    const router = useRouter()

    const filters = ref({
        department: null,
        specialization: null
    })

    onMounted(() => {
        doctorStore.fetchDoctors()
    })

    const filteredDoctors = computed(() => {
        let list = doctorStore.doctorsList

        if (filters.value.department) {
            list = list.filter(
            d => d.department_name === filters.value.department
            )
        }

        if (filters.value.specialization) {
            list = list.filter(
            d => d.specialization === filters.value.specialization
            )
        }return list})

    function openDoctor(id) {
        router.push({ name: "doctorProfile-patient", params: { id } })
    }
</script>

<template>


  <div class="container-fluid mt-3">
    <div v-if="doctorStore.loading">
      <Loading :loading="true" />
    </div>

    <div v-else class="row">
      <div class="col-3">
        <DoctorFilter :departments="['Neurology','Orthopedic','Cardiology']" :specializations="['Surgeon','Consultant','Physician']" v-model="filters"
        />
      </div>

      <div class="col-9">
        <div class="doctors-list-div" >
          <div class="row g-3">
            <div v-for="doc in filteredDoctors" :key="doc.id" class="col-12" 
            >
              <DoctorCard :doctor="doc"  />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
