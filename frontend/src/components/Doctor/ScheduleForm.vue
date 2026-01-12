<script setup>
    import CheckBox from '../Form/CheckBox.vue';
    import Label from '../Form/Label.vue';
    import SessionBox from './SessionBox.vue';
</script>
<template>
    <form>
        <div class="bg-danger form-check">
            <CheckBox  name="isEnabled" id="checkBox1"/>
            <Label label="Enable Online Booking" for="checkBox1"/>
        </div>
        <div class="session-div">
            <SessionBox session="Morning" />
            <SessionBox session="Afternoon"/>
            <SessionBox session="Evening"/>
        </div>
    </form>
</template>