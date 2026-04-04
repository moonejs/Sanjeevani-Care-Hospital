<script setup>
    import CheckBox from '../Form/BaseCheckbox.vue';
    import Label from '../Form/BaseLabel.vue';
    import BaseInput from '../Form/BaseInput.vue';
    import { watch ,computed} from 'vue';
    import { useField } from '@/reusable/useField';
    import { afterTime,timeMax,timeMin } from "@/utils/validators"



    const props=defineProps({
        session:String,
        isOnlineBookingEnabled:Boolean

    })
    const sessionDetail=defineModel()


    watch(() => props.isOnlineBookingEnabled,(enabled) => {
            if (!enabled) {
                sessionDetail.value.enabled = false
                sessionDetail.value.startTime = null
                sessionDetail.value.endTime = null
                sessionDetail.value.slotDuration = 15
                sessionDetail.value.maxPatients = 1
            }
        },{ immediate: true })

    watch(() => sessionDetail.value.enabled,(enabled) => {
        console.log("isSesssionEnabled"+enabled);
        
            if (!enabled) {
            sessionDetail.value.startTime = null
            sessionDetail.value.endTime = null
            }
        }
    )
    const SESSION_RULES = {
        Morning: { min: "05:00", max: "11:59" },
        Afternoon: { min: "12:00", max: "16:59" },
        Evening: { min: "00:00", max: "24:00" }
    }

    const rules = SESSION_RULES[props.session]

    const startTimeField = useField(
        computed(() => sessionDetail.value.startTime),
        [
            timeMin(rules.min, `Enter valid ${props.session} sessioin Time`),
            timeMax(rules.max, `Enter valid ${props.session} session Time `)
        ]
    )

    const endTimeField = useField(
    computed(() => sessionDetail.value.endTime),
        [
            afterTime(
                computed(() => sessionDetail.value.startTime),
                "End time must be after start time"
            ),
            timeMin(rules.min, `Enter valid ${props.session} sessioin Time `),
            timeMax(rules.max, `Enter valid ${props.session} sessioin Time`),
        ]
    )
    


    const disableInput=computed(()=>{
        return !props.isOnlineBookingEnabled || !sessionDetail.value.enabled;
    })

    const disableCheckbox=computed(()=>{
        return !props.isOnlineBookingEnabled;
    })
    const sessionIcon = computed(() => {
        if (props.session === "Morning") return "fa-solid fa-sun text-warning"
        if (props.session === "Afternoon") return "fa-solid fa-cloud-sun text-primary"
        if (props.session === "Evening") return "fa-solid fa-moon text-dark"
    })
</script>

<template>
  <div class="session-card" :class="{ disabled: !sessionDetail.enabled }">
    <div class="session-header">
      <div class="fw-bold">
        
        {{ session }} Session
      </div>
      <div class="form-check form-switch">
        <CheckBox v-model="sessionDetail.enabled" :disabled="disableCheckbox"  :id="props.session" />
      </div>
    </div>

    <div class="session-body">
      <div class="row g-4">
        <div class="col-md-6">
          <Label label="Start Time" for="start_time"/>
          <BaseInput type="time"  :id="`${props.session}-start`"v-model="sessionDetail.startTime" :disabled="disableInput" :error="startTimeField.error.value":valid="startTimeField.valid.value":show="startTimeField.show.value"/>
          
        </div>

        <div class="col-md-6">
          <Label label="End Time" for="end_time"/>
          <BaseInput type="time" :id="`${props.session}-end`" v-model="sessionDetail.endTime" :disabled="disableInput" :error="endTimeField.error.value":valid="endTimeField.valid.value":show="endTimeField.show.value"/>
        </div>

        <div class="col-md-6">
          <Label label="Slot Duration" for="slot_duration"/>
          <select class="form-select" v-model="sessionDetail.slotDuration" :disabled="disableInput">
              <option :value="15">15 minutes</option>
              <option :value="30">30 minutes</option>
              <option :value="45">45 minutes</option>
          </select>
        </div>

        <div class="col-md-6">
          <Label label="Max Patients/Slot" for="max_patients"/>
          <select class="form-select" v-model="sessionDetail.maxPatients" :disabled="disableInput">
              <option :value="1">1</option>
              <option :value="2">2</option>
          </select>
        </div>

      </div>

    </div>

  </div>
</template>

<style scoped>

.session-card{
  
  border:1px solid #e0e0e0;
  border-radius:8px;
  transition:all .2s ease;
}

.session-card:hover{
  border-color:#d2d6dc;
}

.session-header{
  display:flex;
  justify-content:space-between;
  align-items:center;
  padding:16px 18px;
  border-bottom:1px solid #f1f3f4;
}

.session-title{
  font-size:15px;
  font-weight:600;
  color:#3c4043;
  display:flex;
  align-items:center;
  gap:8px;
}

.session-body{
  padding:18px;
}

.session-label{
  font-size:11px;
  font-weight:600;
  color:#5f6368;
  text-transform:uppercase;
  letter-spacing:.4px;
  margin-bottom:6px;
  display:block;
}

.session-card.disabled{
  opacity:.55;
  background:#fafafa;
}

</style>