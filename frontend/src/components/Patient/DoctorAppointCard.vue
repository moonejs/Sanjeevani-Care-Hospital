<script setup>
    import SlotBox from '../common/SlotBox.vue';
    import Badge from '../common/Badge.vue';
    import { useAppointmentStore } from '@/stores/appointment.store';
    const appointment=useAppointmentStore()

    const props=defineProps({
        doctor:Object
    })
    const emit = defineEmits(['slotSelected'])

    function slotSelected(slot) {
        emit('slotSelected', {
            doctor:props.doctor,
            slot:slot
        })
    }

</script>
<template>
    <div class=" doctor-appoint-card v rounded-start-1   mb-3 py-1" v-if="doctor.doctor.is_bookable">
        <div class="card-body border-bottom">
            <div class="d-flex align-items-center gap-3 appointment-doctor-card-header">
                <img :src="doctor.doctor.profile_image" />
                <div class="flex-grow-1">
                    <h5 class="mb-1">Dr. {{ doctor.doctor.name }}</h5>

                    <div class="text-muted small">
                        {{ doctor.doctor.specialization }}
                        <span v-if="doctor.doctor.roles">
                        , {{ doctor.doctor.roles }}
                        </span>
                    </div>

                    <div class="small text-primary fw-semibold">
                        Department: <mark>{{ doctor.doctor.department }}</mark>
                    </div>
                </div>
                <div v-if="(appointment.activeAppointment && appointment.activeAppointment.doctor.id == props.doctor.doctor.id)" >
                    <Badge label="Active Booking" color="info" class="d-block mb-2" />
                    <Badge label="Reschedule Only" color="warning"  />
                    
                </div>
                <Badge label="Booking Open" color="success" v-else />
                

            </div>
        </div>
        <div class="card-body">
            <SlotBox session="Morning" :session-info="doctor.sessions.morning" @slotSelected="slotSelected" :doctor="doctor.doctor"/>
            <SlotBox session="Afternoon" :session-info="doctor.sessions.afternoon" @slotSelected="slotSelected" :doctor="doctor.doctor"/>
            <SlotBox session="Evening" :session-info="doctor.sessions.evening" @slotSelected="slotSelected" :doctor="doctor.doctor"/>
        </div>
        
    </div>
</template>

<style scoped>
.v:hover{
    background-color: #f1f3f5;
}
.v{
    border-left: 3px solid #242E4C;
    
}
</style>
