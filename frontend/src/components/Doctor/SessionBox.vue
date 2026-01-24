<script setup>
    import CheckBox from '../Form/BaseCheckbox.vue';
    import Label from '../Form/BaseLabel.vue';
    import Input from '../Form/BaseInput.vue';
    import { watch ,computed} from 'vue';



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

    const disableInput=computed(()=>{
        return !props.isOnlineBookingEnabled || !sessionDetail.value.enabled;
    })

    const disableCheckbox=computed(()=>{
        return !props.isOnlineBookingEnabled;
    })
</script>
<template>
    <div class="session-box bg-success mb-4">
        <div class="bg-info">
            <Label class="session-box-session-label" :label="props.session" :for="props.session"/>
            <CheckBox v-model="sessionDetail.enabled" :id="props.session" :disabled="disableCheckbox"   />
        </div>
        <div>
            <div class="row">
                <div class="col">
                    <Label label="Start Time" for="start_time"/>
                    <Input type="time"  :id="`${props.session}-start`"v-model="sessionDetail.startTime" :disabled="disableInput" placeholder="9:00 AM"/>
                    
                </div>
                <div class="col">
                    <Label label="End Time" for="end_time"/>
                    <Input type="time" :id="`${props.session}-end`" v-model="sessionDetail.endTime" :disabled="disableInput" />
                </div>
                <div class="col">
                    <Label label="Slot Duration" for="slot_duration"/>
                    <select class="form-select" v-model="sessionDetail.slotDuration" :disabled="disableInput">
                        <option :value="15">15 minutes</option>
                        <option :value="30">30 minutes</option>
                        <option :value="45">45 minutes</option>
                    </select>
                </div>
                <div class="col">
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