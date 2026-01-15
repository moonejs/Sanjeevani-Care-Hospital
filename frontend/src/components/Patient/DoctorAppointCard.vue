<script setup>
    import SlotBox from '../common/SlotBox.vue';
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
    <div class="bg-danger doctor-appoint-card container py-3">
        <div>
            <h2>Dr.{{ doctor.doctor.name }}</h2>
             <h5>{{ doctor.doctor.department }}</h5>
        </div>
        <hr>
        <div>
            <SlotBox session="Morning" :session-info="doctor.sessions.morning" @slotSelected="slotSelected"/>
        </div>
        <div>
            <SlotBox session="Afternoon" :session-info="doctor.sessions.afternoon" @slotSelected="slotSelected"/>
        </div>
        <div>
            <SlotBox session="Evening" :session-info="doctor.sessions.evening" @slotSelected="slotSelected"/>
        </div>
    
    </div>
</template>