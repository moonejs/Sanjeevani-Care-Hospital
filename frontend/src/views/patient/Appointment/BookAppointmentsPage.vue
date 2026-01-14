<script setup>
    import DateBox from '@/components/common/DateBox.vue';
    import { useAppointmentStore } from '@/stores/appointment.store';
    import DoctorAppointCard from '@/components/Patient/DoctorAppointCard.vue';
    import { onMounted } from 'vue';
    const appointment=useAppointmentStore()

    onMounted(async()=>{
        const res=await appointment.fetchAllDoctorsAvailability(appointment.formatDate(appointment.today))
    })
    
</script>

<template>
    <div class="">

        <div class="search-box bg-success">
            
        </div>
        <div class="date-section bg-warning">
            <div class="d-flex justify-content-center gap-5">
                <DateBox v-for="value in appointment.days" :day="value.day" :date="value.date" :full-date="value.fullDate"/>
            </div>
            <div>
                
            </div>
        </div>
        <div class="appointment-section bg-info">
            <DoctorAppointCard v-for="doc in appointment.doctorsAvailability" :key="doc.doctor.id" :doctor="doc"/>
        </div>
    </div>
</template>