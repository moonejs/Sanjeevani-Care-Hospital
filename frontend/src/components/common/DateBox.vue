<script setup>
    import { ref } from 'vue'
    const props=defineProps({
        date:Number,
        day:String,
        fullDate:String,
        isActive:Boolean
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
<!-- <template>
    <div class="date-box" @click="handleClick">
        <h4>{{ date }}</h4>
        <h5>{{ day }}</h5>
    </div>
</template> -->

<template>

  <div class="d-flex align-items-center gap-3 px-4 py-3 pointer border-bottom-1 nav-link rounded-0"  @click="handleClick" >
    <div class="date-circle">
      {{ date }}
    </div>

    <div class="date-text">

      <div class="date-day">
        {{ day }}
      </div>

      <div class="date-full">
        {{ fullDate }}
      </div>

    </div>

  </div>

</template>

<style scoped>



.date-circle{
  width:34px;
  height:34px;
  border-radius:50%;
  border:1px solid #dadce0;
  display:flex;
  align-items:center;
  justify-content:center;
  font-weight:600;
  font-size:13px;
}

.date-text{
  display:flex;
  flex-direction:column;
}

.date-day{
  font-size:14px;
  font-weight:600;
}

.date-full{
  font-size:11px;
  color:#70757a;
}


</style>