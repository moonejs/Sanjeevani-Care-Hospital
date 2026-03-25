  <script setup>
    import DoctorFilter from "./DoctorFilter.vue"
    import DoctorCard from "./DoctorCard.vue"
    import LoadingState from "@/components/common/LoadingState.vue"
    import DoctorCardSkeleton from "@/components/Patient/DoctorCardSkeleton.vue"
    import { useDoctorStore } from "@/stores/doctor.store"
    import { useAppointmentStore } from "@/stores/appointment.store"
    import { onMounted, ref, computed,nextTick } from "vue"
    import { useRouter,useRoute } from "vue-router"
    import { PersonStanding, PersonStandingIcon } from 'lucide-vue-next';

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
    <div class="row g-3">
      <div class="col-lg-3 col-md-4">

        <div class="filter-panel">
          <SearchInput v-model="searchQuery" placeholder="Search doctors..." class="mb-3"/>

          <div class="filter-group">
            <div class="filter-title">Gender</div>
            <CheckboxFilter  v-model="genderFilter" :options="[  { l: 'Male', v: 'male' },  { l: 'Female', v: 'female' }]" name="gender"/>
          </div>

          <div class="filter-group">
            <div class="filter-title">Booking</div>
            <CheckboxFilter  v-model="bookingFilter" :options="[  { l: 'Open', v: 'true' },  { l: 'Close', v: 'false' }]" name="booking"/>
          </div>
          <div class="filter-group">
            <div class="filter-title">Emergency</div>
            <CheckboxFilter  v-model="emergencyFilter" :options="[  { l: 'Emergency', v: 'true' },  { l: 'Non Emergency', v: 'false' }]" name="emergency"/>
          </div>

        </div>
      </div>
      <div class="col-lg-9 col-md-8">
        <LoadingState :loading="doctorStore.loading" type="skeleton" :count="4">
          
          <template #skeleton>
            <DoctorCardSkeleton />
          </template>

          <div class="doctors-list-div">

            <DoctorCard v-for="doc in filteredData" :key="doc.id" :doctor="doc"  :id="`doctor-${doc.id}`" class="mb-2":class="doc.id == route.query.focus ? 'bg-light border rounded' : ''"@doctor-appt="openDoctorApptPage(doc.id)"/>

          </div>
          <div v-if="!filteredData.length" class="text-center py-5">
            <div style="font-size: 24px;">
              <PersonStandingIcon :size="25"/>
            </div>
            <div class="fw-medium mt-2">No doctors found</div>
            <div class="text-muted small">
              Try adjusting filters or search query
            </div>
          </div>

        </LoadingState>

      </div>

    </div>
  </div>
</template>
