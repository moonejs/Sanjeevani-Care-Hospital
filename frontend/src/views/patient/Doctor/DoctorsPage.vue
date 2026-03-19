  <script setup>
    import DoctorFilter from "./DoctorFilter.vue"
    import DoctorCard from "./DoctorCard.vue"
    import LoadingState from "@/components/common/LoadingState.vue"
    import DoctorCardSkeleton from "@/components/Patient/DoctorCardSkeleton.vue"
    import { useDoctorStore } from "@/stores/doctor.store"
    import { useAppointmentStore } from "@/stores/appointment.store"
    import { onMounted, ref, computed,nextTick } from "vue"
    import { useRouter,useRoute } from "vue-router"

    import { useSearchFilter } from '@/utils/useSearchFilter';
    import { storeToRefs } from 'pinia';
    import SearchInput from '@/components/common/SearchInput.vue';
    import CheckboxFilter from "@/components/common/CheckboxFilter.vue"


    const doctorStore = useDoctorStore()
    const router = useRouter()
    const route =useRoute()
    const appointment=useAppointmentStore()
 
    const {doctorsList}=storeToRefs(doctorStore)
    const genderFilter = ref(['male', 'female'])
    const bookingFilter =ref(['true','false'])
    const emergencyFilter =ref(['true','false'])

    const { searchQuery, filteredData } = useSearchFilter(
        doctorsList,
        ['name','room_number','specialization'],
        {
          gender: genderFilter,
          is_bookable:bookingFilter,
          emergency_available:emergencyFilter

        }
        
    )



    onMounted(async() => {
      await doctorStore.fetchDoctors()
      await appointment.fetchMyActiveAppointment()
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
    function openDoctorApptPage(id){
      router.push({
            name: "book-appointments",
            query: { focus: id }
        })
    }
  </script>

  <template>
    <div class="container-fluid mt-3">
      <div class="row">

        <div class="col-3">
          <SearchInput  v-model="searchQuery" placeholder="Search Doctors..."/>
          <CheckboxFilter  v-model="genderFilter" :options="[{ l: 'Male', v: 'male' },{ l: 'Female', v: 'female' }]" label="Filter by Gender" name="gender"/>
          <CheckboxFilter  v-model="bookingFilter" :options="[{ l: 'Open', v: 'true' },{ l: 'Close', v: 'false' }]" label="Filter by booking" name="booking"/>
          <CheckboxFilter  v-model="emergencyFilter" :options="[{ l: 'Emergency', v: 'true' },{ l: 'Non Emergency', v: 'false' }]" label="Filter by Emergency" name="emergency" />
        </div>

        <div class="col-9 ">
          <LoadingState :loading="doctorStore.loading" type="skeleton" :count="4">
            
            <template #skeleton>
              <DoctorCardSkeleton />
            </template>

          
            <DoctorCard v-for="doc in filteredData" :key="doc.id" :doctor="doc"  :id="`doctor-${doc.id}`" class="mb-3 " :class="doc.id == route.query.focus ? 'bg-secondary-subtle' :''" @doctor-appt="openDoctorApptPage(doc.id)"/>

            <div v-if="!filteredData.length" >
              <h2 class="text-muted mt-6 text-center">No doctors found</h2>
            </div>
          </LoadingState>
        </div>

      </div>
    </div>
  </template>
