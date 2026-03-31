<script setup>
    import { onMounted ,ref,watch} from 'vue';
    import Badge from './Badge.vue';
    const props=defineProps({
        session:String,
        sessionInfo:Array,
        doctor:Object
    })
    const emit = defineEmits(['slotSelected'])
    console.log(props.sessionInfo);

    function getColor(slot) {
        if (slot.status === "booked_by_me") return "primary" 
        if (slot.status === "available") return "success"
        if (slot.status === "partial") return "warning"
        if (slot.status === "full") return "danger"
        if (slot.status === "past") return "secondary"
    }
    function selectSlot(slot) {
        if (slot.status == 'past' ||slot.status=='full'){
            return  
        }
        emit('slotSelected', {
            session:props.session,
            slot:slot
        })
    }
</script>
<template>
    <div class="mb-3">
        <h6 class="fw-semibold mb-2">{{ session }}</h6>
        <div v-if="!sessionInfo.length" class="text-muted small">
            No slots available
        </div>
        <div class="d-flex gap-2 flex-wrap">
            <Badge v-for="slot in sessionInfo" :key="slot.time" :label="slot.time" :color="getColor(slot)" class="booking-badge" @click="selectSlot(slot)" :class="{ disabled:  slot.status == 'full' ||slot.status=='past'  ,'opacity-50': slot.status === 'past'}" />
        </div>
  </div>
</template>

