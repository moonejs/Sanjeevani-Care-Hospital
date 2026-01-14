<script setup>
    import CheckBox from '../Form/CheckBox.vue';
    import Label from '../Form/Label.vue';
    import SessionBox from './SessionBox.vue';
    import Badge from '../common/Badge.vue';
    import { computed ,watch,ref} from 'vue';

    const form=defineModel()
    const color=ref("danger")

    const isOnlineBookingEnabled=computed(()=>{
        return form.value.onlineBooking 
    })

    const badgeLabel = computed(() => {
        if (!form.value.onlineBooking) {
            color.value="danger"
            return 'Closed'
        }

        const enabledSessions =
            form.value.morning.enabled +
            form.value.afternoon.enabled +
            form.value.evening.enabled

        if (enabledSessions === 0) {
            color.value="danger"
            return 'Closed'
        }

        if (enabledSessions === 3) {
            color.value="success"
            return 'Open'
        }
        color.value="warning"
        return 'Partially Open'
    })



</script>
<template>
    <form>
        <div class="bg-danger form-check d-flex justify-content-between">
            <div>
                <CheckBox  v-model="form.onlineBooking" id="onlineBooking" />
                <Label label="Enable Online Booking" for="onlineBooking"/>
            </div>
            <Badge :label="badgeLabel" :color="color"/>
        </div>
        <div class="session-div">
            <SessionBox v-model="form.morning" session="Morning" :isOnlineBookingEnabled="isOnlineBookingEnabled" />
            <SessionBox v-model="form.afternoon" session="Afternoon" :isOnlineBookingEnabled="isOnlineBookingEnabled"/>
            <SessionBox v-model="form.evening" session="Evening" :isOnlineBookingEnabled="isOnlineBookingEnabled"/>
        </div>
    </form>
</template>