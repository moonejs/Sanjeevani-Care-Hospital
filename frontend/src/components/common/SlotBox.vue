<script setup>
    import { onMounted ,ref,watch} from 'vue';
    import Badge from './Badge.vue';
    const props=defineProps({
        session:String,
        sessionInfo:Array
    })
    const emit = defineEmits(['slotSelected'])
    console.log(props.sessionInfo);

    function getColor(slot) {
        if (slot.status === 'available'){
            return 'success'
        } 
        if (slot.status === 'partial'){
            return 'warning'
        } 
            return 'danger'
    }
    // function generateSlots(startTime,endTime,slotDuration){
    //     const slots=[]
    //     const start=new Date()
    //     const end=new Date()
    //     const [sh,sm]=startTime.split(":").map(Number)
    //     const [eh,em]=endTime.split(":").map(Number)

    //     start.setHours(sh,sm,0,0)
    //     end.setHours(eh,em,0,0)

    //     while(start.getTime() + Number(slotDuration) *60000<=end.getTime()){
    //         slots.push(
    //             start.toLocaleTimeString("en-US", {
    //                 hour: "numeric",
    //                 minute: "2-digit",
    //                 hour12: true,
    //             })
    //         )
    //         start.setMinutes(start.getMinutes() + slotDuration);
    //     }
    //     return slots; 
    // }
    // watch(()=>props.sessionInfo,(info)=>{
    //      if (!info || !info.enabled) {
    //         slots.value = []
    //         return
    //     }
    //     slots.value=generateSlots(info.startTime,info.endTime,info.slotDuration)
    // },{ immediate: true })
    function selectSlot(slot) {
        if (slot.status === 'full'){
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
        <h4>{{ props.session }}</h4>
        <div v-if="!sessionInfo.length">
            <h6>No Slots</h6>
        </div>
        <div class="d-flex gap-2">
            <Badge v-for="slot in sessionInfo" :key="slot.time" :label="slot.time"
            :color="getColor(slot)"
            class="booking-badge"
            @click="selectSlot(slot)"/>
        </div>
  </div>
</template>