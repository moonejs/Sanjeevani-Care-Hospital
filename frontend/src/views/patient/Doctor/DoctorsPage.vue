<script setup>
  import DoctorFilter from "./DoctorFilter.vue"
  import DoctorCard from "./DoctorCard.vue"
  import LoadingState from "@/components/common/LoadingState.vue"
  import DoctorCardSkeleton from "@/components/Patient/DoctorCardSkeleton.vue"
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
      list = list.filter(d => d.department === filters.value.department)
    }
    if (filters.value.specialization) {
      list = list.filter(d => d.specialization === filters.value.specialization)
    }
    return list
  })

  function openDoctor(id) {
    router.push({ name: "doctorProfile-patient", params: { id } })
  }
</script>

<template>
  <div class="container-fluid mt-3">
    <div class="row">

      <div class="col-3">
        <DoctorFilter
          :departments="['Neurology','Orthopedic','Cardiology']"
          :specializations="['Surgeon','Consultant','Physician']"
          v-model="filters"
        />
      </div>

      <div class="col-9 ">
        <LoadingState :loading="doctorStore.loading" type="skeleton" :count="4">
          
          <template #skeleton>
            <DoctorCardSkeleton />
          </template>

        
          <DoctorCard v-for="doc in filteredDoctors" :key="doc.id" :doctor="doc" @click="openDoctor(doc.id)" class="mb-3"/>

          <div v-if="!filteredDoctors.length" class="text-center text-muted">
            No doctors found
          </div>
        </LoadingState>
      </div>

    </div>
  </div>
</template>
