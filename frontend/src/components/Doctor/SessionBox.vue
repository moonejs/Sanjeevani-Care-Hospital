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
        Evening: { min: "17:00", max: "22:00" }
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
</script>
<template>
    <div class="session-box bg-success-subtle mb-4">
        <div class="bg-info">
            <Label class="session-box-session-label" :label="props.session" :for="props.session"/>
            <CheckBox v-model="sessionDetail.enabled" :id="props.session" :disabled="disableCheckbox"   />
        </div>
        <div>
            <div class="row">
                <div class="col">
                    <Label label="Start Time" for="start_time"/>
                    <BaseInput type="time"  :id="`${props.session}-start`"v-model="sessionDetail.startTime" :disabled="disableInput" :error="startTimeField.error.value":valid="startTimeField.valid.value":show="startTimeField.show.value"/>
                    
                </div>
                <div class="col">
                    <Label label="End Time" for="end_time"/>
                    <BaseInput type="time" :id="`${props.session}-end`" v-model="sessionDetail.endTime" :disabled="disableInput" :error="endTimeField.error.value":valid="endTimeField.valid.value":show="endTimeField.show.value"/>
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