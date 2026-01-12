<script setup>
    import TableTopBox from '@/components/Doctor/TableTopBox.vue';
    import ScheduleForm from '@/components/Doctor/ScheduleForm.vue';
    import Btn from '@/components/common/Btn.vue';
</script>

<template>
    <div>
        <div class="pt-5 px-8">
            <div class="schedule-page-dates container-fluid bg-success-subtle">
                <TableTopBox label="Today"/>
            </div>
            <div class="schedule-div container-fluid bg-warning">
                <ScheduleForm/>
            </div>
        </div>
        <div class="schedule-page-btm bg-danger d-flex justify-content-end px-3">
            <Btn label="Save"/>
        </div>
    </div>
</template> 