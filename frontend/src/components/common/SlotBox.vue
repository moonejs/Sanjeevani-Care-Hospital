<script setup>
    import { onMounted ,ref} from 'vue';
    import Badge from './Badge.vue';
    const props=defineProps({
        session:String,
        sessionInfo:Object
    })
    console.log(props.sessionInfo);
    
    const startTime=props.sessionInfo.startTime
    const endTime=props.sessionInfo.endTime
    const slotDuration=props.sessionInfo.slotDuration
    const slots=ref([])
    function generateSlots(startTime,endTime,slotDuration){
        const slots=[]
        const start=new Date()
        const end=new Date()
        const [sh,sm]=startTime.split(":").map(Number)
        const [eh,em]=endTime.split(":").map(Number)

        start.setHours(sh,sm,0,0)
        end.setHours(eh,em,0,0)

        while(start.getTime() + Number(slotDuration) *60000<=end.getTime()){
            slots.push(
                start.toLocaleTimeString("en-US", {
                    hour: "numeric",
                    minute: "2-digit",
                    hour12: true,
                })
            )
            start.setMinutes(start.getMinutes() + slotDuration);
        }
        return slots; 
    }
    onMounted(()=>{
         if (!props.sessionInfo || !props.sessionInfo.enabled) {
            slots.value = []
            return
        }
        slots.value=generateSlots(startTime,endTime,slotDuration)
    })
</script>
<template>
    <div class="mb-3">
        <h4>{{ props.session }}</h4>
        <div v-if="!slots.length">
            <h3>No appointments</h3>
        </div>
        <div class="d-flex gap-2">
            <Badge v-for="slot in slots" :key="slot" :label="slot"/>
        </div>
  </div>
</template>