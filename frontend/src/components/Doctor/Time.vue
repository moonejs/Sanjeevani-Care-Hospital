<script setup>
    import { ref, onMounted, onUnmounted, computed } from 'vue'

    const now = ref(new Date())
    let timer = null
    onMounted(()=>{
        timer=setInterval(()=>{
            now.value=new Date()
        },1000)
    })
    
    onUnmounted(()=>{
        clearInterval(timer)
    })

    const formattedDate=computed(()=>{
        return now.value.toLocaleDateString('en-In',{
            weekday: 'long',
            day: 'numeric',
            month: 'short',
            year: 'numeric'
        })
    })
    const formattedTime = computed(()=>{
        return now.value.toLocaleTimeString('en-In',{
            hour: 'numeric',
            minute: '2-digit',
            second: '2-digit',
            hour12: true
        })
    })
    


</script>

<template>
  <div class="bg-info time">
      <h4>{{ formattedTime }}</h4>
    <h4>{{ formattedDate }}</h4>
    
  </div>
</template>
