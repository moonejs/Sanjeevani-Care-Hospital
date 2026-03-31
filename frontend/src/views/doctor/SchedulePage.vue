<script setup>
    import TableTopBox from '@/components/Doctor/TableTopBox.vue';
    import ScheduleForm from '@/components/Doctor/ScheduleForm.vue';
    import Btn from '@/components/common/Btn.vue';
    import { useAppointmentStore } from '@/stores/appointment.store';
    import { useFormValidation } from '@/reusable/useFormValidation';
    import { ref,onMounted, watch,computed } from 'vue';
    import { useToastStore } from '@/stores/toast.store';

 
    const toast = useToastStore()
    function getToday() {
    return new Date().toISOString().split('T')[0]
    }

    const appointment=useAppointmentStore()
    const currentTabDate=ref("")
    
    onMounted(() => {
        currentTabDate.value = getToday()
    }) 

    const availability = ref({
        date: getToday(),
        onlineBooking: false,

        morning: {
            enabled: false,
            startTime: null,
            endTime: null,
            slotDuration: 15,
            maxPatients: 1
        },

        afternoon: {
            enabled: false,
            startTime: null,
            endTime: null,
            slotDuration: 15,
            maxPatients: 1
        },

        evening: {
            enabled: false,
            startTime: null,
            endTime: null,
            slotDuration: 15,
            maxPatients: 1
        }
    })

    async function save(){
         console.log(availability.value);
         await appointment.saveDoctorAvailability(availability.value)
         toast.addToast({
          message: 'Appointment Scheduled Successfully.',
          type: 'success'
        })
         
    }
    function validateSession(session) {
        return (
            session.enabled &&
            session.startTime &&
            session.endTime &&
            session.slotDuration != null &&
            session.maxPatients != null
        );
    }

    function canSave(){
        if(!availability.value.onlineBooking){
            save()
            return
        }
        const sessions=["morning","afternoon","evening"]
        for (const s of sessions){
            const session=availability.value[s]
            if(session.enabled){
                if(!validateSession(session)){
                    console.log(`All fields required for the ${s} session`);
                    return
                    
                }
            }
        }
        save()
    }
    function onDateSelected(date){
        currentTabDate.value=date
        availability.value.date=date
    }

    async function fetchCurrentAvailability(date){
        const data=await appointment.fetchDoctorAvailability(date)
        availability.value=data
    }

    watch(()=>currentTabDate.value,(d)=>{
        console.log(d);
        
        fetchCurrentAvailability(d)    
    })

    const formattedDate = computed(() => {
      return new Date(currentTabDate.value).toLocaleDateString(
        "en-US",
        {
          weekday: "long",
          month: "long",
          day: "numeric"
        }
      )
    })

</script>
<template>
<div class="container-fluid">
  <div class=" container-fluid px-3">
    <div class="d-flex justify-content-between align-items-center">
      <div>
        <h4 class="">Doctor Availability</h4>
        <p class=" size">
          Configure your consulting hours for each day
        </p>
      </div>
      <Btn label="Save" @click="canSave" class="btn-outline-secondary  px-4 animate-up-2"/>
    </div>

  </div>

  <div class="d-flex flex-grow-1 overflow-hidden">
    <div class="date-sidebar border-end ">
      <TableTopBox @selected-date="onDateSelected"/>

    </div>
    <main class="container-fluid">
      <div class="">
        <h2 class="mt-3">
          {{ formattedDate }}
        </h2>

        <ScheduleForm v-model="availability"/>

      </div>
    </main>
  </div>
</div>

</template>

<style scoped>
  .size{
    font-size: 15px;
  }
  .date-sidebar {
    width: 280px;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
  }
</style>