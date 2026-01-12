<script setup>
    import CheckBox from '../Form/CheckBox.vue';
    import Label from '../Form/Label.vue';
    import Input from '../Form/Input.vue';
    defineProps({
        session:String,

    })
</script>
<template>
    <div class="session-box bg-success mb-4">
        <div class="bg-info">
            <Label class="session-box-session-label" :label="session" :for="session"/>
            <CheckBox :name="session" :id="session"/>
        </div>
        <div>
            <div class="row">
                <div class="col">
                    <Label label="Start Time" for="start_time"/>
                    <Input type="time" id="start_time"  />
                    
                </div>
                <div class="col">
                    <Label label="End Time" for="end_time"/>
                    <Input type="time" id="end_time" />
                </div>
                <div class="col">
                    <Label label="Slot Duration" for="slot_duration"/>
                    <select class="form-select">
                        <option selected>15 minutes</option>
                        <option value="1">30 minutes</option>
                        <option value="2">45 minutes</option>
                    </select>
                </div>
                <div class="col">
                    <Label label="Max Patients/Slot" for="max_patients"/>
                    <select class="form-select">
                        <option selected>1</option>
                        <option value="1">2</option>
                    </select>
                </div>
            </div>
        </div>
    </div>
</template>