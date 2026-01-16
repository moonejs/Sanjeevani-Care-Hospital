<script setup>
    import DateBox from '@/components/common/DateBox.vue';
    import { useAppointmentStore } from '@/stores/appointment.store';
    import DoctorAppointCard from '@/components/Patient/DoctorAppointCard.vue';
    import TableTopBox from '@/components/Doctor/TableTopBox.vue';
    import { onMounted,ref } from 'vue';
    import BookingModal from '@/components/Patient/BookingModal.vue';
    const appointment=useAppointmentStore()

    onMounted(async()=>{
        const today = appointment.formatDate(appointment.today)
        appointment.selectedDate = today
        await appointment.fetchAllDoctorsAvailability(today)
    })

    async function fetchDoctorsByDate(date) {
        const res = await appointment.fetchAllDoctorsAvailability(date)
        
    }

    function onDateSelected(date){
        if (!date) return
        console.log(date);
        appointment.selectedDate = date
        fetchDoctorsByDate(date)
        
    }


    const showModal = ref(false)
    const selectedDoctor = ref(null)
    const selectedSlot = ref(null)
    const appointmentType = ref('opd')
    const slotSession = ref("")

    function openBookingModal({ doctor, slot }) {
        selectedDoctor.value = doctor
        selectedSlot.value = slot.slot
        showModal.value = true
        slotSession.value=slot.session
    }
    async function confirmBooking(){
        await appointment.bookAppointment({
            doctor_id:selectedDoctor.value.doctor.id,
            date:appointment.selectedDate,
            start_time:selectedSlot.value.time,
            type:appointmentType.value
        })
        showModal.value = false
        await appointment.fetchAllDoctorsAvailability(appointment.selectedDate)
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
            <DoctorAppointCard v-for="doc in appointment.doctorsAvailability" :key="doc.doctor.id" :doctor="doc" @slot-selected="openBookingModal"/>
        </div>
        <BookingModal :show-modal="showModal" :selected-doctor="selectedDoctor" :selected-slot="selectedSlot",
        :slot-session="slotSession"
         v-model:appointment-type="appointmentType" @close="showModal = false" @confirm="confirmBooking" />

    </div>
</template> 