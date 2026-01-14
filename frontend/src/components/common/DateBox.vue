<script setup>
    const props=defineProps({
        date:Number,
        day:String,
        fullDate:String
    })
    const emit=defineEmits(['select'])
    function handleClick(){
        emit('select',{
            day:props.day,
            date:props.date,
            fullDate:props.fullDate
        })
    }
</script>
<template>
    <div class="date-box" @click="handleClick">
        <h4>{{ date }}</h4>
        <h5>{{ day }}</h5>
    </div>
</template>