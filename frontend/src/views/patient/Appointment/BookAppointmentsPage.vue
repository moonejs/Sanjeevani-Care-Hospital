<script setup>
    import { useAppointmentStore } from '@/stores/appointment.store';
    import DoctorAppointCard from '@/components/Patient/DoctorAppointCard.vue';
    import TableTopBox from '@/components/Doctor/TableTopBox.vue';
    import { onMounted,ref,nextTick } from 'vue';
    import { useRoute } from 'vue-router';
    import BookingModal from '@/components/Patient/BookingModal.vue';
    import LoadingState from "@/components/common/LoadingState.vue"
    import AppointmentCardSkeleton from '@/components/Patient/AppointmentCardSkeleton.vue';
    import { useToastStore } from '@/stores/toast.store';
    import { useSearchFilter } from '@/utils/useSearchFilter';
    import SearchInput from '@/components/common/SearchInput.vue';
    import { storeToRefs } from 'pinia';

    const appointment=useAppointmentStore()
    const route =useRoute()
    const toast = useToastStore()

    const {doctorsAvailability} = storeToRefs(appointment)
    const { searchQuery, filteredData } = useSearchFilter(
        doctorsAvailability,
        ['doctor.name'],
        
    )


    onMounted(async()=>{
        const today = appointment.formatDate(appointment.today)
        appointment.selectedDate = today
        await appointment.fetchAllDoctorsAvailability(today)
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

    async function fetchDoctorsByDate(date) {
        const res = await appointment.fetchAllDoctorsAvailability(date)
        
    }

    const showModal = ref(false)
    const selectedDoctor = ref(null)
    const selectedSlot = ref(null)
    const appointmentType = ref('opd')
    const slotSession = ref("")
    

    function onDateSelected(date){
        if (!date) return
        console.log(date);
        appointment.selectedDate = date
        fetchDoctorsByDate(date)
        
    }


    function openBookingModal({ doctor, slot }) {
        selectedDoctor.value = doctor
        selectedSlot.value = slot.slot
        showModal.value = true
        slotSession.value=slot.session
    }
    async function confirmBooking(){
      try {
        if (appointment.activeAppointment) {
            await appointment.rescheduleAppointment({appointment_id: appointment.activeAppointment.id,date: appointment.selectedDate,start_time: selectedSlot.value.time})
        }else{
            await appointment.bookAppointment({
                doctor_id:selectedDoctor.value.doctor.id,
                date:appointment.selectedDate,
                start_time:selectedSlot.value.time,
                type:appointmentType.value
            })
        }
        toast.addToast({
          message: 'Appointment booked successfully',
          type: 'success'
        })

        await appointment.fetchMyActiveAppointment()
        showModal.value = false
        selectedDoctor.value = null
        selectedSlot.value = null
        slotSession.value = ""
        appointmentType.value = "opd"

        await appointment.fetchAllDoctorsAvailability(appointment.selectedDate)
      } catch (error) {
        toast.addToast({
          title: 'Error',
          message: 'Failed to book appointment',
          type: 'error'
        })
      }
        
    }

    async function cancelMyAppointment() {
        if (!appointment.activeAppointment) return
        
        try {
          const confirmCancel = confirm("Are you sure you want to cancel?")
          if (!confirmCancel) return

          showModal.value = false
          await appointment.cancelBookedAppointment(appointment.activeAppointment.id,{reason:"Cancelled by patient"})
          toast.addToast({
            message: 'Appointment Canceled successfully',
            type: 'error'
          })

        } catch (error) {
          
        }

        
    }


</script>
<template>
  <div class="container-fluid">
    <div class="row">
      
      <div class="col-md-3 col-lg-2 bg-white border-end  sticky-top">
        <TableTopBox label="Today" @selected-date="onDateSelected"/>
      </div>
      
      <div class="col-lg-7 col-md-6 py-3">
        <div class="d-flex justify-content-between align-items-center mb-3 px-2">
          <div>
            <h4 class="fw-semibold mb-1">Book Appointment</h4>
            <div class="text-muted small">
              Choose a doctor and select a time slot
            </div>
          </div>
          <SearchInput  v-model="searchQuery" placeholder="Search Doctors..."/>

          <div class="date-context-card px-3 py-2 text-end">
            <div class="fw-bold">
              {{ appointment.selectedDate }}
            </div>
            <div class="small text-muted">
              {{
                new Date(appointment.selectedDate).toLocaleDateString('en-US', {
                  weekday: 'long'
                })
              }}
            </div>
          </div>
        </div>

        <div class="d-flex flex-column gap-2 px-2 doctors-list-div">
          <LoadingState :loading="appointment.loading" type="skeleton" :count="4">
            <template #skeleton>
              <AppointmentCardSkeleton/>
            </template>
            <DoctorAppointCard  v-for="doc in filteredData" :key="doc.doctor.id" :doctor="doc" @slot-selected="openBookingModal"/>
            <div v-if="!filteredData.length" >
              <h2 class="text-muted mt-6 text-center">No Appointments found</h2>
            </div>
          </LoadingState>
        </div>

      </div>

      

    </div>

    <BookingModal  :show-modal="showModal"  :selected-doctor="selectedDoctor"  :selected-slot="selectedSlot" :slot-session="slotSession" v-model:appointment-type="appointmentType"  @close="showModal = false"  @confirm="confirmBooking"  @cancelAppointment="cancelMyAppointment" 
    />

  </div>
</template>