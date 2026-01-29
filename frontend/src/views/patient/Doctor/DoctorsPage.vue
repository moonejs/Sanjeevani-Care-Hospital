  <script setup>
    import DoctorFilter from "./DoctorFilter.vue"
    import DoctorCard from "./DoctorCard.vue"
    import LoadingState from "@/components/common/LoadingState.vue"
    import DoctorCardSkeleton from "@/components/Patient/DoctorCardSkeleton.vue"
    import { useDoctorStore } from "@/stores/doctor.store"
    import { onMounted, ref, computed,nextTick } from "vue"
    import { useRouter,useRoute } from "vue-router"

    const doctorStore = useDoctorStore()
    const router = useRouter()
    const route =useRoute()

    const filters = ref({
      department: null,
      specialization: null
    })

    onMounted(async() => {
      await doctorStore.fetchDoctors()

      if(route.query.focus){
        await nextTick()
        const el = document.getElementById(
          `doctor-${route.query.focus}`
        )

        el?.scrollIntoView({
          behavior: "smooth",
          block: "center"
        })
      }
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

          
            <DoctorCard v-for="doc in filteredDoctors" :key="doc.id" :doctor="doc"  :id="`doctor-${doc.id}`" class="mb-3 " :class="doc.id == route.query.focus ? 'bg-secondary-subtle' :''"/>

            <div v-if="!filteredDoctors.length" class="text-center text-muted">
              No doctors found
            </div>
          </LoadingState>
        </div>

      </div>
    </div>
  </template>
