<script setup>
    import SlotBox from '../common/SlotBox.vue';
    const props=defineProps({
        doctor:Object
    })
</script>
<template>
    <div class="bg-danger doctor-appoint-card container py-3">
        <div>
            <h2>Dr.{{ doctor.doctor.name }}</h2>
             <h5>{{ doctor.doctor.department }}</h5>
        </div>
        <hr>
        <div>
            <SlotBox session="Morning" :session-info="doctor.sessions.morning"/>
        </div>
        <div>
            <SlotBox session="Afternoon" :session-info="doctor.sessions.afternoon"/>
        </div>
        <div>
            <SlotBox session="Evening" :session-info="doctor.sessions.evening"/>
        </div>
    
    </div>
</template>