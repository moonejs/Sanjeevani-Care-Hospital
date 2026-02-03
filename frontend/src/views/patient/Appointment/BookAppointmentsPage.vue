<script setup>
    import DateBox from '@/components/common/DateBox.vue';
    import { useAppointmentStore } from '@/stores/appointment.store';
    import DoctorAppointCard from '@/components/Patient/DoctorAppointCard.vue';
    import TableTopBox from '@/components/Doctor/TableTopBox.vue';
    import { onMounted,ref,nextTick } from 'vue';
    import { useRoute } from 'vue-router';
    import BookingModal from '@/components/Patient/BookingModal.vue';

    const appointment=useAppointmentStore()
    const route =useRoute()

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
        await appointment.fetchMyActiveAppointment()
        showModal.value = false
        selectedDoctor.value = null
        selectedSlot.value = null
        slotSession.value = ""
        appointmentType.value = "opd"

        await appointment.fetchAllDoctorsAvailability(appointment.selectedDate)
    }

    async function cancelMyAppointment() {
        if (!appointment.activeAppointment) return

        const confirmCancel = confirm("Are you sure you want to cancel?")
        if (!confirmCancel) return

        await appointment.cancelBookedAppointment(appointment.activeAppointment.id,{reason:"Cancelled by patient"})
        showModal.value = false
    }


</script>

<template>
    <div class="">
        
        <div class="search-box bg-success">
            
        </div>
        <div class="date-section bg-warning">
            <TableTopBox label="Today" @selected-date="onDateSelected"/>
        </div>
        <div class="appointment-section py-2 bg-info">
            <h2 v-if="!appointment.doctorsAvailability.length">No Doctor Available</h2>
            <DoctorAppointCard v-for="doc in appointment.doctorsAvailability" :id="`doctor-${doc.doctor.id}`" :key="doc.doctor.id" :doctor="doc" @slot-selected="openBookingModal" :class="doc.doctor.id == route.query.focus ? 'bg-secondary-subtle' :''"/>
        </div>
        <BookingModal :show-modal="showModal" :selected-doctor="selectedDoctor" :selected-slot="selectedSlot",
        :slot-session="slotSession"
         v-model:appointment-type="appointmentType" @close="showModal = false" @confirm="confirmBooking" @cancelAppointment="cancelMyAppointment" />

    </div>
</template> 